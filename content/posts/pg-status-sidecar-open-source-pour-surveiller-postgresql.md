---
title: "pg-status : sidecar open-source pour surveiller PostgreSQL"
slug: "pg-status-sidecar-open-source-pour-surveiller-postgresql"
date: 2026-11-11T19:15:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Un micro-service léger qui détecte master, replicas et lag de réplication via HTTP pour vos hôtes PostgreSQL."
tags:
  - postgresql
  - database
  - open-source
  - monitoring
  - platform-engineering
series:
  - Veille techno
series_order: 188
showTableOfContents: true
---

## Introduction

Surveiller l'état de ses instances PostgreSQL dans un setup multi-hôtes reste un sujet étonnamment mal outillé. Entre les TTL DNS qui traînent et les health checks bricolés, la détection fiable du master et des replicas est souvent un point de friction. **pg-status** est un nouveau micro-service open-source qui s'attaque à ce problème précis.

## Ce que fait pg-status

pg-status est un **sidecar léger** qui poll vos hôtes PostgreSQL à intervalle configurable et expose leur statut via une **interface HTTP**. Concrètement, il permet de :

- Identifier quels hôtes sont **vivants** ou non
- Distinguer le **master** des **replicas**
- Suivre le **lag de réplication** en temps réel
- Exposer toutes ces informations via des endpoints HTTP consommables par n'importe quel composant d'infrastructure

Le projet est né d'un besoin concret : contourner la lenteur du failover DNS dans les architectures PostgreSQL multi-hôtes. Il se positionne comme une brique utile pour la détection de master, la configuration de proxies, ou des scénarios de load-balancing custom.

## Avis

Ce type d'outil s'inscrit dans une logique que je trouve essentielle en platform engineering : **disposer de briques d'automatisation simples, composables et sans dépendance lourde**.

La détection du master PostgreSQL est un problème récurrent. Les solutions existent — Patroni expose son API, certains proxies comme `pgbouncer` ou `HAProxy` intègrent des checks — mais elles sont souvent couplées à un écosystème plus large. pg-status prend le parti inverse : un composant unique, une responsabilité unique.

Le format sidecar est pertinent. Ça s'intègre dans un pod Kubernetes, dans un `docker-compose`, ou même sur une VM classique sans remettre en cause l'architecture existante. L'exposition HTTP rend l'information consommable par **n'importe quel orchestrateur, proxy ou script maison** — c'est cette interopérabilité qui fait la valeur d'un tel outil.

À évaluer évidemment sur la robustesse en production et la gestion des cas limites (split-brain, timeout de connexion, faux positifs), mais le concept est sain et l'approche minimaliste rassurante.

🔗 [Article source](https://www.postgresql.org/about/news/pg-status-microservice-for-checking-the-status-of-postgresql-hosts-3222/)
