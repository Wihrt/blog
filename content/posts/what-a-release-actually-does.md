---
title: "What Happens Between Writing a Post and Serving It"
slug: "what-a-release-actually-does"
date: 2026-08-21T16:00:00+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "The eleven steps between a pull request containing a Markdown file and a container serving it, and why each one exists."
tags:
  - automation
  - ci-cd
  - kubernetes
  - homelab
showTableOfContents: true
---

This post is the first one published entirely by the pipeline it describes. No
part of getting it onto the site involved a human decision, which is either
reassuring or alarming depending on how much you trust the checks.

## What runs before it merges

A pull request arrives containing exactly one Markdown file. Two things then
happen in parallel.

A guard classifies the author and confines it to what that author has business
changing. An automated writer may add articles and nothing else: not the chart,
not the container, not the workflows, and not the list of permitted tags. That
last exclusion matters more than it looks, because otherwise the automation
could invent a tag and authorise it in the same change.

Meanwhile the checks run. The front matter is validated against a schema that
rejects unknown fields, descriptions outside the length search engines display,
dates in the future, duplicate slugs, raw HTML, insecure links and bodies short
enough to suggest a truncated generation. The site is built with warnings
treated as errors. Every internal link is resolved against the built output.
The chart is linted, unit-tested and validated against real Kubernetes schemas.
The image is built and then actually run the way the cluster runs it, with a
read-only root filesystem and no capabilities, and probed on every route.

Only if all of that is green does the merge happen on its own.

## What runs after it merges

The version comes from the commit messages, not from a file anyone edits. A
multi-architecture image is built, signed, and its digest recorded. That digest
is written into the chart before the chart is packaged, so the published chart
resolves exactly one immutable build rather than whatever a tag points at
today.

The chart is pushed and signed. A release is cut with the changelog. Finally a
single line changes in the infrastructure repository: the chart version. The
deployment controller notices and rolls the pods.

## Why the digest matters

The infrastructure repository tracks one semantic version and nothing else. It
contains no digests, which keeps it readable and lets its dependency bot work.
The immutability lives one level down, inside the chart. Both properties hold
at once, which is the part that took the longest to get right.
