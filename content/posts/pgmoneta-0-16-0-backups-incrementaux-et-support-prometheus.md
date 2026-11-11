---
title: "pgmoneta 0.16.0 : backups incrémentaux et support Prometheus"
slug: "pgmoneta-0-16-0-backups-incrementaux-et-support-prometheus"
date: 2026-11-11T18:58:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "pgmoneta 0.16.0 ajoute backups incrémentaux PostgreSQL 17+, images Docker/Podman et métriques Prometheus en HTTPS."
tags:
  - postgresql
  - backup
  - docker
  - monitoring
  - devops
  - open-source
series:
  - Veille techno
series_order: 171
showTableOfContents: true
---

## Introduction

pgmoneta, l'outil open source de backup et restore pour PostgreSQL, passe en version 0.16.0. Cette release marque un cap en termes d'intégration dans les environnements modernes, avec plusieurs ajouts qui parlent directement aux équipes DevOps et Platform Engineering.

## Ce que contient la release

Les points clés de pgmoneta 0.16.0 :

- **Backups incrémentaux** pour PostgreSQL 17+ : moins de données transférées et stockées entre chaque backup complet.
- **Images Docker et Podman** officielles : déploiement standardisé, compatible avec les pipelines CI/CD et les orchestrateurs.
- **Support Prometheus en HTTPS** : exposition de métriques sécurisée, prête pour une intégration directe dans une stack d'observabilité existante.
- **Filtrage avancé pour `pgmoneta-walinfo`** : meilleure visibilité sur les WAL segments.
- Corrections de bugs et améliorations diverses.

L'outil proposait déjà un périmètre fonctionnel solide : backups full, compression, chiffrement AES, WAL shipping, hot standby, gestion distante, mode offline, support TLS 1.2+, mode daemon et vault utilisateur.

## Avis

Quand on gère des plateformes, le nerf de la guerre sur les outils de backup, ce n'est plus seulement la fiabilité du restore. C'est la capacité de l'outil à **s'intégrer sans friction** dans le reste de l'écosystème.

pgmoneta 0.16.0 coche plusieurs cases importantes à ce niveau. Le support Prometheus natif en HTTPS signifie qu'on n'a plus besoin d'un exporter tiers ou d'un script custom pour remonter des métriques de backup dans Grafana. Les images container officielles, c'est un déploiement reproductible et testable dans un pipeline, au lieu d'un binaire compilé à la main sur une VM.

Les backups incrémentaux sur PostgreSQL 17+ sont également un ajout significatif. Sur des bases volumineuses, la différence en termes de fenêtre de backup et de coût stockage peut être conséquente. C'est une fonctionnalité que des outils comme **pgBackRest** proposent depuis longtemps, mais la voir arriver dans pgmoneta rend l'outil plus compétitif.

À surveiller de près si vous cherchez à **réduire le nombre de composants artisanaux** dans votre chaîne de backup PostgreSQL. L'automatisation passe aussi par le choix d'outils qui parlent nativement le langage de la plateforme.

[Source](https://www.postgresql.org/about/news/pgmoneta-016-3065/)
