# blog

![Version: 0.1.1](https://img.shields.io/badge/Version-0.1.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.1](https://img.shields.io/badge/AppVersion-0.1.1-informational?style=flat-square)

Static blog served by Caddy, built with Hugo

**Homepage:** <https://blog.brokenbymega.ovh>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Arnaud Hatzenbuhler |  | <https://github.com/Wihrt> |

## Source Code

* <https://github.com/Wihrt/blog>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity rules. |
| autoscaling.enabled | bool | `false` | Create a HorizontalPodAutoscaler. |
| autoscaling.maxReplicas | int | `4` | Maximum replicas. |
| autoscaling.minReplicas | int | `2` | Minimum replicas. |
| autoscaling.targetCPUUtilizationPercentage | int | `80` | Target average CPU utilisation. |
| containerPort | int | `8080` | Container port. Must match the `:8080` site block in the image's Caddyfile. |
| extraEnv | list | `[]` | Extra environment variables. |
| extraVolumeMounts | list | `[]` | Extra volume mounts. |
| extraVolumes | list | `[]` | Extra volumes. `/tmp` is always mounted because the root filesystem is read-only and Caddy needs a writable XDG directory. |
| fullnameOverride | string | `"blog"` | Override the full generated resource name. |
| gatus.conditions | list | `["[STATUS] == 200","[RESPONSE_TIME] < 400"]` | Conditions the response must satisfy. |
| gatus.enabled | bool | `true` | Create a GatusEndpoint for external uptime monitoring. |
| gatus.group | string | `"external"` | Endpoint group. |
| gatus.interval | string | `"1m"` | Check interval. |
| image.digest | string | `"sha256:963d1cf12001a0a1527deb5ce1538b081b38e0fd77299a17a9804c30deb06d55"` | Image digest (`sha256:...`). When set it is appended to the tag, which pins the deployment to one immutable build even though the homelab repo only ever tracks a chart version. Rewritten by the release workflow. |
| image.pullPolicy | string | `"IfNotPresent"` | Image pull policy. |
| image.repository | string | `"ghcr.io/wihrt/blog"` | Image repository. |
| image.tag | string | `"0.1.1"` | Image tag. Rewritten by the release workflow; defaults to `.Chart.AppVersion`. |
| imagePullSecrets | list | `[]` | Image pull secrets. |
| ingress.annotations | object | `{"cert-manager.io/cluster-issuer":"letsencrypt-prod","kubernetes.io/tls-acme":"true"}` | Extra annotations. cert-manager issues the certificate named in `tls`. |
| ingress.className | string | `"traefik"` | IngressClass to use. |
| ingress.enabled | bool | `true` | Create an Ingress. |
| ingress.hosts[0].host | string | `"blog.brokenbymega.ovh"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| ingress.tls[0].hosts[0] | string | `"blog.brokenbymega.ovh"` |  |
| ingress.tls[0].secretName | string | `"blog-tls"` |  |
| livenessProbe | object | `{"failureThreshold":3,"httpGet":{"path":"/healthz","port":"http"},"initialDelaySeconds":3,"periodSeconds":20,"timeoutSeconds":2}` | Liveness probe. Targets the dedicated `/healthz` endpoint in the Caddyfile. |
| nameOverride | string | `""` | Override the chart name portion of resource names. |
| nodeSelector | object | `{}` | Node selector. |
| podAnnotations | object | `{}` | Extra annotations for the pod. |
| podDisruptionBudget.enabled | bool | `true` | Create a PodDisruptionBudget. Ignored when `replicaCount` is below 2. |
| podDisruptionBudget.minAvailable | int | `1` | Minimum available pods during a voluntary disruption. |
| podLabels | object | `{}` | Extra labels for the pod. |
| podSecurityContext | object | `{"fsGroup":1000,"runAsGroup":1000,"runAsNonRoot":true,"runAsUser":1000,"seccompProfile":{"type":"RuntimeDefault"}}` | Pod-level security context. Matches the image: it runs as uid/gid 1000 and the Caddy binary has its file capabilities stripped at build time. |
| readinessProbe | object | `{"failureThreshold":3,"httpGet":{"path":"/healthz","port":"http"},"initialDelaySeconds":1,"periodSeconds":10,"timeoutSeconds":2}` | Readiness probe. |
| replicaCount | int | `2` | Number of replicas. Two by default so a node drain never takes the blog down. |
| resources | object | `{"limits":{"memory":"64Mi"},"requests":{"cpu":"10m","memory":"32Mi"}}` | Resource requests and limits. A static file server needs very little; no CPU limit on purpose, so a traffic spike is not throttled. |
| securityContext | object | `{"allowPrivilegeEscalation":false,"capabilities":{"drop":["ALL"]},"privileged":false,"readOnlyRootFilesystem":true}` | Container-level security context. |
| service.annotations | object | `{}` | Extra annotations for the Service. |
| service.port | int | `8080` | Service port. |
| service.type | string | `"ClusterIP"` | Service type. |
| serviceAccount.annotations | object | `{}` | Annotations for the ServiceAccount. |
| serviceAccount.automountServiceAccountToken | bool | `false` | The blog never talks to the API server, so it needs no token. |
| serviceAccount.create | bool | `true` | Create a dedicated ServiceAccount. |
| serviceAccount.name | string | `""` | Name to use. Generated from the fullname when empty. |
| startupProbe | object | `{"failureThreshold":15,"httpGet":{"path":"/healthz","port":"http"},"periodSeconds":2}` | Startup probe. |
| tolerations | list | `[]` | Tolerations. |
| topologySpreadConstraints | list | `[{"labelSelector":{"matchLabels":{}},"maxSkew":1,"topologyKey":"kubernetes.io/hostname","whenUnsatisfiable":"ScheduleAnyway"}]` | Topology spread constraints. Defaults to spreading replicas across nodes. |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
