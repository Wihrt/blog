---
title: "Automating the Boring Parts with n8n"
slug: "self-hosting-n8n"
date: 2026-07-09T11:30:00+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Running n8n in the cluster and handing it the small recurring jobs that were quietly eating an hour of my week."
tags:
  - n8n
  - automation
  - self-hosted
  - homelab
showTableOfContents: true
---

Most of what I automate is not impressive. It is a handful of tasks that each
take four minutes and happen often enough to add up. Checking whether a
certificate is close to expiry. Collecting release notes for the charts I run.
Turning a captured note into a draft article and opening a pull request.

## Why a workflow tool rather than scripts

I wrote these as cron jobs first. The scripts were fine; the operational story
was not. When one failed at three in the morning, I found out days later. When
I wanted to change a schedule, I edited a crontab on a machine I had to
remember the name of. There was no history, no retry, and no way to see what
had run.

A workflow engine gives you those for free. Every execution is recorded with
its inputs and outputs, failures are visible without going looking, and
retrying a step does not mean re-running the whole thing.

## Keeping state out of the container

The instinct is to give it a volume and move on. I resisted, because a workflow
engine with local state is a workflow engine you cannot move. Credentials live
in a secret store and are injected at runtime. Execution history lives in
Postgres. The container itself holds nothing that matters, which means
rescheduling it onto another node is uneventful.

```yaml
env:
  - name: DB_TYPE
    value: postgresdb
  - name: N8N_ENCRYPTION_KEY
    valueFrom:
      secretKeyRef:
        name: n8n-secrets
        key: encryption-key
```

## The blog pipeline

The workflow that matters most opens a pull request against this repository
with a Markdown file in it. Validation runs, the front matter is checked
against a schema, the site builds, and if everything passes the change merges
without me. A release then publishes a container image and raises a version in
the GitOps repository.

The interesting design constraint was deciding what the automation is not
allowed to touch. It can add articles. It cannot change the build, the chart,
or the list of permitted tags. That boundary is enforced in continuous
integration rather than by trust, which is the only way it means anything.
