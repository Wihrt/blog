# blog

Source and packaging for [blog.brokenbymega.ovh](https://blog.brokenbymega.ovh).

A Hugo site (Blowfish theme) served by Caddy, shipped as a container image and a Helm chart, and
deployed to a homelab Kubernetes cluster by ArgoCD. Articles arrive as pull
requests from an n8n workflow and are published without human intervention.

## How a post reaches production

```text
pull request (content/posts/*.md)
  ├─ Guard      only content changed, conventional title, one post
  └─ CI         front matter schema, tags, links, site build, chart, image, scan
        ↓ auto-merge once both are green
main
  └─ Release    version from commit history
                → multi-arch image → ghcr.io/wihrt/blog:X.Y.Z (signed, digest recorded)
                → chart pinned to that digest → ghcr.io/wihrt/charts/blog:X.Y.Z
                → pull request on Wihrt/homelab raising the chart version
        ↓
ArgoCD syncs → Caddy pods roll → the article is live
```

The homelab repository tracks **only a chart version**. The image digest lives
inside the chart, so a single semver there still resolves to one immutable
build — and the `# renovate:` convention used across that repository stays
intact.

## Getting set up

Everything is installed by [mise](https://mise.jdx.dev):

```bash
mise trust && mise install
mise run bootstrap
```

## Everyday commands

| Command | What it does |
| --- | --- |
| `mise run dev` | Dev server with drafts on <http://localhost:1313> |
| `mise run new my-slug` | Scaffold `content/posts/my-slug.md` from the archetype |
| `mise run build` | Production build into `public/`; warnings are fatal |
| `mise run validate` | Check every post against `schemas/post.schema.json` |
| `mise run links` | Link-check the built site |
| `mise run lint` | Every pre-commit hook over the whole repo |
| `mise run helm:test` | Chart unit tests |
| `mise run docker:build` / `docker:run` | Build and run the image as Kubernetes does |
| `mise run ci` | The full pipeline, in the order CI runs it |

Run `mise run ci` before pushing; it is the same set of checks the pull request
will run.

## Writing a post

`mise run new my-post` creates a file from `archetypes/posts.md`. The front
matter contract is `schemas/post.schema.json`, and `content/posts/hello-world.md`
is a working reference.

The rules that trip people up:

- `description` must be 50–160 characters. It is the search and social summary.
- Every tag must already exist in `data/tags.yaml`. Adding a tag is a separate,
  human-authored change — automated pull requests cannot widen the vocabulary.
- `slug` must match the filename and must never change after publication. If it
  has to, add the old path to `aliases`.
- No raw HTML, no `http://` links, no remotely hosted images. Commit images
  next to the post.
- The body needs at least 200 words; a shorter one usually means a truncated
  generation.

`mise run validate` reports all of this by file and field.

## What automation may and may not change

`.github/workflows/guard-content.yml` restricts any pull request not authored by
the repository owner to `content/`, `assets/images/` and `static/images/`. A
pull request touching the chart, the Dockerfile, the workflows or
`data/tags.yaml` fails the check, and branch protection blocks the merge. The
guard fails closed: no green check, no merge.

## Repository layout

| Path | Contents |
| --- | --- |
| `content/` | Posts and pages |
| `data/tags.yaml` | The allowed tag vocabulary |
| `layouts/` | Theme overrides (empty; Blowfish needs none) |
| `schemas/` | Front matter contract |
| `scripts/` | `validate_content.py` |
| `charts/blog/` | Helm chart, its unit tests and generated docs |
| `Dockerfile`, `Caddyfile` | The runtime image |
| `.github/workflows/` | Guard, CI, release, homelab bump |

## One-time setup outside this repository

- Branch protection on `main` requiring the `Guard`, `Lint and validate`,
  `Build site`, `Helm chart` and `Container image` checks.
- "Allow auto-merge" enabled on this repository and on `Wihrt/homelab`.
- A GitHub App installed on `Wihrt/homelab` with `contents: write` and
  `pull-requests: write`, its credentials stored here as `HOMELAB_APP_ID` and
  `HOMELAB_APP_PRIVATE_KEY`.
- The `blog` application added once to
  `kubernetes/bootstrap/argocd/homelab.yaml` in the homelab repository; see
  `docs/homelab-integration.md`.
