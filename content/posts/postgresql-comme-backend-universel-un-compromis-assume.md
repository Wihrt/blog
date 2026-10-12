---
title: "PostgreSQL comme backend universel : un compromis assumé"
slug: "postgresql-comme-backend-universel-un-compromis-assume"
date: 2026-10-12T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Postgres peut remplacer Kafka, Redis ou MongoDB à petite échelle, réduisant le coût opérationnel d'une stack complexe."
tags:
  - postgresql
  - database
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 95
showTableOfContents: true
---

## Introduction

L'idée de consolider sa stack technique autour de PostgreSQL n'est pas nouvelle, mais elle revient régulièrement — et pour de bonnes raisons. Stephan Schmidt, CTO et coach CTO, publie un article qui pose clairement le cadre : Postgres peut remplacer beaucoup de choses, mais c'est un compromis, pas une solution miracle.

## Ce que dit l'article

L'argument central : jusqu'à quelques millions d'utilisateurs, PostgreSQL peut se substituer à un nombre surprenant de composants backend. **Kafka**, **RabbitMQ**, **MongoDB**, **Redis** — autant de briques que Postgres couvre au moins partiellement grâce à ses fonctionnalités natives :

- **LISTEN/NOTIFY** pour du messaging léger
- **JSONB** pour du stockage document
- Des extensions comme `pg_cron` ou `pgmq` pour du job scheduling et du queuing
- Le cache applicatif via des stratégies de requêtage adaptées

Schmidt insiste : ce n'est pas un dogme. C'est un **tradeoff** conscient, particulièrement pertinent pour les startups et les équipes réduites qui n'ont pas les moyens d'opérer une stack à 10 composants.

## Avis

D'un point de vue platform engineering, cet article tape juste sur un sujet souvent sous-estimé : **le coût opérationnel de chaque brique technique**.

Chaque composant ajouté dans une stack, c'est un déploiement à automatiser, un monitoring à configurer, des alertes à calibrer, des secrets à gérer, une doc à maintenir, une montée de version à planifier. La complexité ne vient pas d'un seul outil — elle vient de la **glue** entre tous ces outils.

Consolider autour de Postgres quand le volume le permet, c'est directement réduire cette surface. Moins de briques à orchestrer, c'est moins de pipelines, moins de Helm charts, moins de runbooks. C'est de l'automatisation **par soustraction**.

Évidemment, il y a des limites. Au-delà d'un certain débit de messages ou de certains patterns d'accès, Kafka ou Redis restent incontournables. Mais la question à se poser avant chaque ajout devrait toujours être : *est-ce que Postgres ne fait pas déjà le job pour notre échelle actuelle ?*

Le piège classique, c'est de designer une stack pour le scale qu'on n'a pas encore. Et de payer le coût opérationnel **maintenant** pour un problème qu'on aura peut-être **jamais**.

[Source : amazingcto.com](https://www.amazingcto.com/postgres-for-everything/)
