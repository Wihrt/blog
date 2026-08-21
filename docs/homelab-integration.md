# Wiring the blog into the homelab repository

The release pipeline can only *bump* an existing entry. The entry itself is
added once, by hand, in [`Wihrt/homelab`](https://github.com/Wihrt/homelab).
This page is the exact change to make.

## Why a chart version and not an image tag

Every version in the homelab repository is a plain semver on the line following
a `# renovate:` comment; `grep -rn "sha256:" kubernetes/` returns nothing. A
digest there would be inconsistent with the rest of the repository and would
break the regex manager that Renovate relies on.

So the digest lives one level down. `charts/blog/values.yaml` carries both
`image.tag` and `image.digest`, and the chart renders
`ghcr.io/wihrt/blog:X.Y.Z@sha256:…`. The homelab repository tracks a single
chart version, and that version still resolves to exactly one immutable build.

## 1. Register the application

In `kubernetes/bootstrap/argocd/homelab.yaml`, under `applications:`:

```yaml
  blog:
    enabled: true
    syncWave: "100"
    namespace: blog
    helm:
      enabled: true
      chart:
        name: blog
        # renovate: datasource=docker depName=ghcr.io/wihrt/charts/blog
        repoURL: ghcr.io/wihrt/charts
        version: "0.1.0"
    # The chart ships the Ingress and the GatusEndpoint. Set this to true and
    # add kubernetes/argocd/applications/blog/static/network-policy.yaml if you
    # want a CiliumNetworkPolicy, which is where the other apps keep theirs.
    static:
      enabled: false
```

The keys must match `kubernetes/charts/app-of-apps/values.schema.json`, which
sets `additionalProperties: false`.

## 2. Overrides, if any

The chart's defaults already target this cluster: `traefik` ingress class,
`letsencrypt-prod` cluster issuer, host `blog.brokenbymega.ovh`. Only create
`kubernetes/argocd/applications/blog/helm/values.yaml` if you need to diverge:

```yaml
---
ingress:
  hosts:
    - host: blog.example.org
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: blog-tls
      hosts:
        - blog.example.org
```

## 3. Let Renovate group the app

In `renovate.json`, alongside the existing per-app groups:

```json
{
  "description": "blog",
  "groupName": "blog",
  "matchPackageNames": ["ghcr.io/wihrt/charts/blog", "ghcr.io/wihrt/blog"]
}
```

Renovate is the fallback here, not the primary path: `bump-homelab.yml` commits
the new version within seconds of the release. Renovate only catches a release
whose bump never landed -- because the push kept losing a race, or the App token
could not be minted.

## 4. Grant the pipeline access

The workflow needs to push to a *different* repository. The built-in
`GITHUB_TOKEN` is scoped to the repository that runs the workflow, so it cannot
do this regardless of the permissions declared -- a separate credential is
required.

Since the bump is a plain commit, nothing calls the GitHub API. Clone, fetch
and push are the whole requirement.

1. Go to **Settings → Developer settings → Personal access tokens →
   Fine-grained tokens → Generate new token**.
2. Repository access: **Only select repositories** → `Wihrt/homelab`.
3. Repository permissions: **Contents: Read and write**. Nothing else.
4. Store it in the **blog** repository:

   ```bash
   gh secret set HOMELAB_TOKEN
   ```

`main` in the homelab repository must accept a push from that token. If you
protect the branch later, exempt it or switch this workflow back to a pull
request.

**A fine-grained token expires** -- a year at most. When it does, releases will
publish their image and chart and then fail at this last step, with a clear
error rather than a silent no-op. Put a reminder in the calendar, or move to a
deploy key or GitHub App, neither of which expires.

## What a release does to this repository

`bump-homelab.yml` rewrites one line:

```text
.applications.blog.helm.chart.version = "<new version>"
```

and commits it directly to `main`, so ArgoCD sees the new version within
seconds of the release. If the push is rejected because someone else pushed
first, it rebases and retries up to five times rather than failing a release
whose artifacts are already published.

If the `blog` entry is missing, the workflow fails with a message pointing back
here rather than inventing one.

The trade-off of committing directly is that the homelab repository's own
checks never run on the bump. Only one line changes and this repository's
pipeline has already linted, templated, unit-tested and kubeconform-validated
the chart it points at, but it is a real gap: a broken chart version reaches
the cluster without a second opinion.

## Verifying a deployment

```bash
kubectl -n blog get pods,ingress
kubectl -n blog get deploy blog -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
argocd app get blog
curl -sI https://blog.brokenbymega.ovh/healthz
```

The image reference must contain an `@sha256:` digest. If it does not, the
release that produced it did not go through `release.yml`.
