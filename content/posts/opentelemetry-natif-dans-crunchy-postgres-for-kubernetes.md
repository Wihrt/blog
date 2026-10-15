---
title: "OpenTelemetry natif dans Crunchy Postgres for Kubernetes"
slug: "opentelemetry-natif-dans-crunchy-postgres-for-kubernetes"
date: 2026-10-15T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Crunchy Data ajoute l'export de logs OpenTelemetry natif à son opérateur, unifiant l'observabilité PostgreSQL sur Kubernetes."
tags:
  - postgresql
  - kubernetes
  - observability
  - monitoring
  - database
series:
  - Veille techno
series_order: 98
showTableOfContents: true
---

## Introduction

L'observabilité des bases de données sur Kubernetes reste un sujet souvent sous-estimé. Quand il s'agit de PostgreSQL, la centralisation des logs passe encore trop souvent par des montages artisanaux. Crunchy Data vient d'intégrer le support natif d'OpenTelemetry pour le logging dans son opérateur Kubernetes, et c'est une avancée qui mérite qu'on s'y attarde.

## Ce que propose cette mise à jour

Crunchy Postgres for Kubernetes intègre désormais un export automatisé des logs via **OpenTelemetry**, directement depuis l'opérateur. Concrètement :

- Activation via des **feature gates** dans la configuration de l'opérateur
- Configuration d'**exporters** vers la plateforme d'observabilité cible (Google Cloud Logging, Grafana Cloud, ou tout backend compatible OTel)
- Approche **vendor-agnostic** : le format est standardisé, pas de lock-in sur un outil de collecte
- Couverture des **logs et métriques** de l'ensemble des clusters Postgres gérés par l'opérateur
- Cohérence du signal entre les différents composants du cluster (instances, pgBouncer, backups)

L'objectif affiché est de fournir une stratégie de logging unifiée sans avoir à déployer et maintenir des composants tiers spécifiques.

## Avis

Sur le terrain, l'observabilité PostgreSQL sur Kubernetes reste un point de friction. Entre les sidecars `fluentbit` ou `vector`, les parsers de logs custom pour gérer les formats multilignes de Postgres, et la corrélation avec les métriques de l'opérateur, on passe du temps sur de la plomberie qui n'apporte pas de valeur directe.

Avoir ce signal standardisé **à la source**, au niveau de l'opérateur lui-même, c'est la bonne approche. Ça élimine une couche de glue code, ça réduit les divergences entre environnements (dev, staging, prod), et ça facilite l'automatisation du déploiement de la stack complète. Un `helm upgrade` et l'observabilité suit, sans configuration annexe à maintenir.

Le choix d'OpenTelemetry plutôt qu'une intégration propriétaire est aussi pertinent. OTel devient le standard de fait pour l'instrumentation. Ancrer les composants d'infrastructure sur ce standard, c'est se donner de la flexibilité pour changer de backend d'observabilité sans retoucher la couche de collecte.

Ça ne remplacera pas une réflexion globale sur la stratégie d'observabilité, mais ça retire un irritant concret pour les équipes plateforme qui gèrent du Postgres à l'échelle.

**Source** : [Crunchy Data Blog – OpenTelemetry Observability in Crunchy Postgres for Kubernetes](https://www.crunchydata.com/blog/opentelemetry-observability-in-crunchy-postgres-for-kubernetes)
