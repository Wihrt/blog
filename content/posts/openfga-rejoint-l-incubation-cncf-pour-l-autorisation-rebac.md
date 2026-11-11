---
title: "OpenFGA rejoint l'incubation CNCF pour l'autorisation ReBAC"
slug: "openfga-rejoint-l-incubation-cncf-pour-l-autorisation-rebac"
date: 2026-11-11T19:13:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "OpenFGA passe incubating à la CNCF : moteur d'autorisation ReBAC API-first, adopté en production, intégré à Helm et Prometheus."
tags:
  - platform-engineering
  - security
  - api
  - helm
  - open-source
series:
  - Veille techno
series_order: 186
showTableOfContents: true
---

## Introduction

OpenFGA, moteur d'autorisation open source inspiré du modèle Zanzibar de Google, vient d'être promu au statut **incubating** par la CNCF. Pour les équipes platform engineering qui cherchent à automatiser toujours plus de briques d'infrastructure, c'est un signal à ne pas ignorer.

## Ce qu'il faut retenir

OpenFGA implémente du **ReBAC** (Relationship-Based Access Control) avec une approche **API-first**. L'idée : centraliser toute la logique d'autorisation dans un moteur dédié, découplé des services applicatifs.

Depuis son entrée en sandbox CNCF en 2022, le projet affiche une traction solide :

- **37 adopteurs en production**
- SDKs disponibles en Python, Java, Go, .NET et JavaScript
- Maintainers issus de **Grafana Labs** et **GitPod**
- Intégrations natives avec **OpenTelemetry**, **Helm** et **Prometheus**
- 4 300+ stars GitHub, 96 contributeurs

La roadmap prévoit de nouveaux SDKs (Ruby, Rust, PHP), le support du standard **AuthZen**, et des améliorations de performance.

## Analyse

Quand on regarde l'état de l'art sur la plupart des plateformes, l'autorisation reste un des derniers domaines où l'automatisation est en retard. On provisionne les clusters automatiquement, on déploie en continu, on a de l'observabilité as code… mais la gestion des droits d'accès est encore souvent codée en dur, dupliquée entre services, ou gérée via des middlewares maison difficiles à maintenir.

Un moteur comme OpenFGA, exposé en API, permet d'intégrer l'autorisation comme une brique à part entière dans les pipelines et les workflows de provisioning. Le modèle ReBAC est plus expressif que du RBAC classique — on peut modéliser des relations complexes (organisation → équipe → projet → ressource) sans exploser la matrice de rôles.

Le fait que le projet s'intègre déjà dans l'écosystème CNCF (métriques Prometheus, traces OpenTelemetry, déploiement Helm) réduit la friction d'adoption. On ne rajoute pas un outil isolé, on branche une capacité dans une stack existante.

Le point de vigilance : la modélisation ReBAC demande un investissement initial. Il faut penser son modèle d'autorisation en amont, ce qui est en réalité une bonne chose — mais c'est un changement de posture par rapport au `if user.role == admin` qu'on retrouve partout.

À suivre de près, surtout avec l'arrivée du SDK Rust et du support AuthZen qui pourrait faciliter l'interopérabilité entre moteurs d'autorisation.

🔗 [Article source – CNCF Blog](https://www.cncf.io/blog/2025/11/11/openfga-becomes-a-cncf-incubating-project/)
