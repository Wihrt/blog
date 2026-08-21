# syntax=docker/dockerfile:1

# ---- build ------------------------------------------------------------------
# hugomods/hugo:exts ships Hugo extended plus Go, which Hugo Modules require to
# resolve the PaperMod dependency declared in go.mod.
# renovate: datasource=docker depName=hugomods/hugo
ARG HUGO_IMAGE=hugomods/hugo:0.165.0
# renovate: datasource=docker depName=caddy
ARG CADDY_IMAGE=caddy:2.11.4-alpine

FROM ${HUGO_IMAGE} AS build

WORKDIR /src

# Resolve modules first so a content-only change reuses this layer. Content
# changes are the common case here: every n8n post rebuilds this image.
# hugo.toml comes along because Hugo refuses to run module commands outside a
# project; it changes far less often than content, so the layer still holds.
COPY go.mod go.sum hugo.toml ./
# `get` with no arguments resolves exactly what go.mod pins (no -u, so nothing
# is upgraded at build time); `verify` then fails if a module's content does not
# match go.sum.
RUN hugo mod get && hugo mod verify

COPY archetypes/ ./archetypes/
COPY assets/ ./assets/
COPY content/ ./content/
COPY data/ ./data/
COPY layouts/ ./layouts/
COPY static/ ./static/

ARG HUGO_BASEURL=https://blog.brokenbymega.ovh/
# --panicOnWarning turns a missing shortcode, broken ref or missing page
# resource into a failed build instead of a silently broken page in production.
RUN hugo --gc --minify --panicOnWarning --baseURL "${HUGO_BASEURL}" --destination /public

# ---- runtime ----------------------------------------------------------------
FROM ${CADDY_IMAGE}

# Caddy writes its cache and (unused) data under these paths. Pointing them at
# /tmp is what allows readOnlyRootFilesystem: true with only a /tmp emptyDir.
ENV XDG_CONFIG_HOME=/tmp \
    XDG_DATA_HOME=/tmp \
    XDG_CACHE_HOME=/tmp

# The upstream image grants the binary cap_net_bind_service so it can bind :443.
# This container only ever binds :8080, and a binary carrying file capabilities
# cannot be exec'd once the pod drops ALL capabilities -- the kernel returns
# EPERM. Stripping it is what makes the hardened securityContext work.
RUN setcap -r /usr/bin/caddy && \
    [ -z "$(getcap /usr/bin/caddy)" ]

COPY Caddyfile /etc/caddy/Caddyfile
COPY --from=build /public /srv

RUN caddy validate --config /etc/caddy/Caddyfile

# Matches the securityContext in charts/blog: non-root, unprivileged port.
USER 1000:1000
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["wget", "--quiet", "--tries=1", "--spider", "http://127.0.0.1:8080/healthz"]

ENTRYPOINT ["caddy"]
CMD ["run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
