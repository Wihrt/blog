---
title: "Dashy : un dashboard self-hosted pour centraliser ses outils"
slug: "dashy-un-dashboard-self-hosted-pour-centraliser-ses-outils"
date: 2026-09-28T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Dashy centralise l'accès aux services via un dashboard configurable en YAML, déployable en Docker, self-hosted."
tags:
  - self-hosted
  - docker
  - platform-engineering
  - gitops
  - homelab
  - open-source
series:
  - Veille techno
series_order: 84
showTableOfContents: true
---

## Introduction

Dans un contexte DevOps ou Platform Engineering, la multiplication des outils génère de la friction : trop d'interfaces, trop de navigation, trop de contexte à reconstruire. Dashy propose une réponse simple à ce problème avec un dashboard self-hosted, configurable et déployable en quelques minutes.

## Ce que fait Dashy

Dashy est une application web open source conçue pour centraliser l'accès à ses outils et services depuis une interface unique. Ses fonctionnalités principales :

- **Status-checking** : surveillance de la disponibilité des services exposés
- **Widgets** : intégration de données contextuelles (météo, flux RSS, métriques…)
- **Éditeur UI** : configuration via interface graphique, sans édition manuelle du fichier YAML obligatoire
- **Thèmes et icon packs** : personnalisation visuelle
- **Déploiement via `docker`** : mise en route rapide, intégrable dans un `docker-compose` existant

La configuration est déclarative (YAML), ce qui la rend versionnables et cohérente avec une approche GitOps.

## Analyse

L'intérêt de Dashy ne réside pas dans une fonctionnalité unique et spectaculaire, mais dans sa cohérence avec une démarche d'automatisation et de réduction de friction. Centraliser les points d'entrée d'un environnement, c'est une forme de documentation vivante : on expose ce qui tourne, on le rend accessible, on réduit le temps de navigation entre les outils.

Dans une logique Platform Engineering, ce type d'outil peut servir d'Internal Developer Portal léger, sans la complexité d'un Backstage. Ce n'est pas la même cible, mais pour des équipes petites ou des environnements homelab/staging, c'est une alternative pragmatique.

Le fait que ce soit self-hosted élimine la dépendance à un SaaS tiers et garde la maîtrise des données de topologie exposées. La configuration YAML versionnable permet de traiter le dashboard comme du code — ce qui est exactement ce qu'on attend dans ce type de stack.

À regarder si vous cherchez à améliorer la visibilité de vos environnements sans complexité supplémentaire.

## Source

https://noted.lol/dashy/
