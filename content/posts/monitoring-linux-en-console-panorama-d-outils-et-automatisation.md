---
title: "Monitoring Linux en console : panorama d'outils et automatisation"
slug: "monitoring-linux-en-console-panorama-d-outils-et-automatisation"
date: 2026-11-11T18:31:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Tour d'horizon des outils console (top, htop, atop, btop...) pour surveiller Linux et automatiser sans stack lourd."
tags:
  - linux
  - monitoring
  - cli
  - automation
  - observability
  - platform-engineering
series:
  - Veille techno
series_order: 144
showTableOfContents: true
---

## Introduction

Sous Linux, le monitoring console reste une compétence fondamentale — que ce soit pour du debug rapide, de l'observation en environnement contraint, ou comme première brique d'automatisation. Jeff Geerling propose un tour d'horizon structuré des outils disponibles, du plus basique au plus complet.

## Ce que couvre l'article

L'article passe en revue une dizaine d'outils :

- **`top`** : l'utilitaire de base, présent partout, mais limité.
- **`htop`** : version améliorée, navigation interactive, plus lisible.
- **`atop`** : orienté historique et logging, utile pour l'analyse post-incident.
- **`iftop`** : focus réseau, visualisation des flux en temps réel.
- **`iotop`** : surveillance des I/O disque par processus.
- **`nvtop`** : monitoring GPU, utile dès qu'on touche à des workloads ML/AI.
- **`btop`** : interface moderne, tout-en-un, très lisible.

Pour chaque outil, Geerling donne les commandes d'installation et les situations où il est pertinent de l'utiliser.

## Avis

Ce type d'article est utile non pas parce qu'il révèle quelque chose de nouveau, mais parce qu'il pousse à reconsidérer comment on utilise ces outils au quotidien.

La tendance en Platform Engineering est de sauter directement vers des stacks d'observabilité complets — Prometheus, Grafana, OpenTelemetry. C'est légitime à l'échelle. Mais ça masque parfois une réalité terrain : ces outils console, bien utilisés, peuvent déjà faire beaucoup.

`atop` en mode logging continu sur un nœud critique, c'est de la rétention de métriques sans infrastructure supplémentaire. Un script shell qui appelle `iotop` en mode batch et déclenche une alerte sur un seuil, c'est de l'automatisation low-cost et efficace. Sur des environnements embarqués, edge, ou simplement sans accès à un stack centralisé, cette approche reste souvent la plus rapide à mettre en place.

L'idée centrale : **l'automatisation commence aussi par savoir ce qu'on peut faire avec les outils déjà disponibles**. Connaître précisément ce que fait chaque outil — et ses limites — permet de choisir le bon niveau d'investissement selon le contexte.

## Source

https://www.jeffgeerling.com/blog/2025/top-10-ways-monitor-linux-console
