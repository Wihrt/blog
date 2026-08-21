---
title: "Hello World: This Blog Now Runs on Hugo, Caddy and Kubernetes"
slug: "hello-world"
date: 2026-08-21T09:00:00+02:00
lastmod: 2026-08-21T09:00:00+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "How this blog moved off a paid SaaS onto a fully automated Hugo, Caddy and ArgoCD pipeline running in my own homelab cluster."
tags:
  - homelab
  - hugo
  - kubernetes
  - automation
showTableOfContents: true
---

This post exists for two reasons. It is the first article on the new stack, and
it is the reference format that the automation pipeline validates every future
post against. If you are looking at it because a validation error pointed you
here, copy its front matter and adjust the values.

## Why move

The previous home for these notes was a hosted platform that moved its useful
features behind a paid tier. Rather than pay for something I already run the
infrastructure for, the content moved into a git repository and the rendering
moved into the cluster that was already there.

The result is a blog with no runtime dependencies worth speaking of: a static
site compiled ahead of time and handed to a web server that does nothing but
read files off a read-only filesystem.

## How a post gets published

Nothing about publishing is manual. An automation workflow opens a pull request
containing a single Markdown file. Continuous integration then checks that the
front matter matches a JSON schema, that every tag already exists in the
controlled vocabulary, that the slug is unique, that the site still builds with
warnings treated as errors, and that no internal link is broken.

A separate guard verifies that the pull request touches only content. If it
tries to modify the Helm chart, the container image, or the workflows
themselves, the check fails and auto-merge never engages.

Once the pull request merges, a release workflow computes the next semantic
version from the commit history, builds a multi-architecture container image,
signs it, records its digest inside the Helm chart, publishes the chart to the
registry, and opens a pull request against the infrastructure repository to
raise the chart version. ArgoCD notices the change and rolls the deployment.

## What runs in the cluster

The container is a two-stage build. The first stage compiles the site. The
second stage copies the compiled output next to a small web server
configuration and throws everything else away. The running container holds no
build tooling, no source, and no writable filesystem outside a scratch
directory.

That server sets long immutable cache headers on fingerprinted assets, revalidates
HTML on every request, serves compressed responses, and answers a dedicated
health endpoint that the cluster probes. It listens on an unprivileged port as
an unprivileged user, which is what lets the pod run with a read-only root
filesystem and every capability dropped.

## What comes next

More notes on the homelab itself: the cluster bootstrap, the GitOps layout, the
observability stack, and the parts of all of it that turned out to be harder
than the documentation suggested.
