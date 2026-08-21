---
title: "Postgres Backups That I Actually Restored"
slug: "cnpg-backups-to-s3"
date: 2026-06-18T20:10:00+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "CloudNativePG scheduled backups to object storage, and why an untested backup is just a file that makes you feel better."
tags:
  - storage
  - kubernetes
  - security
  - self-hosted
showTableOfContents: true
---

I had backups for eight months before I found out they did not work. The
scheduled job ran, the objects appeared in the bucket, the size looked
plausible. What I had never done was restore one.

## The setup

CloudNativePG handles continuous archiving natively. You give a cluster a
barman object store, credentials, and a retention policy, and it streams write
ahead log segments continuously while taking periodic base backups. The
configuration is short enough to read in one go, which is part of why I chose
it.

```yaml
backup:
  retentionPolicy: 30d
  barmanObjectStore:
    destinationPath: s3://homelab-backups/postgres
    wal:
      compression: gzip
    data:
      compression: gzip
      immediateCheckpoint: true
```

## What was actually broken

The credentials I had given it were scoped to write, not to list. Backups
succeeded because writing succeeded. Recovery requires enumerating the archive
to find a base backup and replay point, and that call was denied. Nothing in
the backup path ever exercised it, so nothing ever complained.

This is the general shape of the problem. Backup systems verify the half of the
operation you run every day and leave the half you run once untested, and the
untested half is the one that matters.

## Restoring on a schedule

The fix was not better credentials, although that was part of it. The fix was
making restore a routine operation rather than an emergency one. A recovery
cluster is created from the object store, a query runs against it to confirm
the data is there and recent, and the cluster is deleted. If any step fails, an
alert fires.

It costs a few minutes of compute each week. It replaces a belief with a
measurement, and after eight months of being wrong I have stopped trusting
beliefs about backups.

## The rule I follow now

If a recovery path has never executed, assume it does not work. This applies to
database backups, to configuration exports, and to the disaster recovery
document nobody has read since it was written.
