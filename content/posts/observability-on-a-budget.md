---
title: "Observability on Three Nodes and No Budget"
slug: "observability-on-a-budget"
date: 2026-08-02T16:45:00+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Metrics, logs and uptime checks for a homelab, sized so the monitoring stack does not consume more resources than the things it monitors."
tags:
  - observability
  - monitoring
  - kubernetes
  - homelab
showTableOfContents: true
---

The default advice for cluster observability assumes a cluster considerably
larger than mine. Install the full stack on three nodes and the monitoring
consumes a visible fraction of everything you have, which is an absurd place to
end up.

## Deciding what not to collect

Retention was the first thing I cut. I do not need ninety days of per-second
metrics for a home network. Fifteen days at a coarser interval answers every
question I have actually asked, and it fits comfortably in memory.

Scrape targets were the second. The default rules collect metrics from
components I do not run and cannot act on. Trimming that list halved ingestion
without losing a single dashboard I look at.

## Three layers, different purposes

Metrics tell me a thing is degrading. Logs tell me why. Uptime checks tell me
something is broken from the outside, which is the only perspective that
matches how I actually notice problems.

The last one is easy to skip and the one I would keep if I could only have one.
An external check that fetches a health endpoint every minute catches the class
of failure where every internal signal looks fine and the service is
nonetheless unreachable, because the ingress is misconfigured or a certificate
has expired.

```yaml
conditions:
  - "[STATUS] == 200"
  - "[RESPONSE_TIME] < 400"
```

## Alerting that I do not ignore

An alert I ignore is worse than no alert, because it teaches me to ignore the
next one. The rule I settled on is that an alert must be actionable and it must
be rare. If something fires more than once a week and the action is always to
wait, it is not an alert, it is a metric, and it belongs on a dashboard.

The result is a small number of alerts that I trust. When one arrives, I look.
That is the entire measure of whether this works, and it took removing far more
than I added to get there.
