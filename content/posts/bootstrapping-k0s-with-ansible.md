---
title: "Bootstrapping a k0s Cluster with Ansible"
slug: "bootstrapping-k0s-with-ansible"
date: 2026-03-04T18:20:00+01:00
lastmod: 2026-03-11T09:15:00+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Turning three bare machines into a working k0s control plane with a single Ansible playbook, and the ordering mistakes that cost me an evening."
tags:
  - homelab
  - kubernetes
  - ansible
  - linux
series:
  - Building the homelab cluster
series_order: 1
showTableOfContents: true
---

The cluster started as three second-hand mini PCs on a shelf. What I wanted was
a repeatable path from a freshly imaged disk to a joined node, because the
interesting part of a homelab is not the first install, it is the fourth one
after you have broken something badly enough to start over.

## Why k0s

I looked at k3s and kubeadm first. k3s is excellent and I would recommend it to
most people, but it bundles opinions I wanted to make myself, particularly
around the CNI and the ingress controller. kubeadm goes the other way and asks
you to assemble everything. k0s sits between the two: a single binary, no
control-plane components running as workloads by default, and a declarative
cluster definition that describes the whole topology in one file.

## Playbook ordering

The playbook has four roles and the order matters more than I expected.
Prerequisites go first: kernel modules, sysctl values, disabling swap, and the
handful of packages the kubelet expects to find. Then container runtime
configuration. Then the tooling role that installs the binaries. Only then does
the cluster definition get applied.

My mistake was applying the cluster definition before the sysctl role had run
its handlers. Nodes joined, then failed their health checks minutes later with
errors that pointed at networking rather than at the real cause. The fix was a
single `meta: flush_handlers` in the right place, which is the kind of thing
that is obvious in hindsight and invisible while you are staring at it.

## Idempotence is the whole point

Every role has to survive being run against a node that is already configured.
That means no shell commands without a `creates` guard, no blind appends to
configuration files, and no tasks that succeed the first time and fail the
second. I test this by running the playbook twice in a row and requiring the
second run to report zero changes. It is a crude check and it has caught real
bugs every time I have added a role.

The next part covers the network layer, which is where the cluster stopped
being a collection of machines and started behaving like one.
