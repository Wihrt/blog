---
title: "dockcheck : surveiller les mises à jour Docker sans pull"
slug: "dockcheck-surveiller-les-mises-a-jour-docker-sans-pull"
date: 2026-10-01T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Outil CLI bash qui vérifie les mises à jour d'images Docker sans pull, avec notifications et intégrations Prometheus/Zabbix."
tags:
  - docker
  - cli
  - self-hosted
  - monitoring
  - automation
  - homelab
series:
  - Veille techno
series_order: 87
showTableOfContents: true
---

## Introduction

Garder ses containers Docker à jour est un sujet récurrent en self-hosting comme en production. Entre les outils trop intrusifs qui appliquent les mises à jour automatiquement et la vérification manuelle, il manquait une brique intermédiaire. C'est exactement le créneau que vise **dockcheck**.

## Ce que fait dockcheck

`dockcheck` est un outil CLI écrit en **bash** qui vérifie si des mises à jour d'images sont disponibles pour vos containers Docker — **sans pull préalable**. Concrètement :

- **Traitement parallèle** pour accélérer la vérification sur des setups avec beaucoup de containers.
- **Filtres d'exclusion** pour ignorer certains containers.
- **Notifications multi-canaux** : Matrix, Telegram, et d'autres.
- **Configuration flexible** : flags CLI, fichier de config, ou **labels Docker Compose** pour un contrôle granulaire par service.
- **Planification via cron** pour des workflows automatisés.
- **Option de délai** avant mise à jour, pour laisser les releases se stabiliser avant de les appliquer.

Côté communauté, des intégrations ont été ajoutées pour **Prometheus**, **Zabbix**, **Unraid** et **Synology DSM**, ce qui élargit pas mal le spectre d'utilisation.

## Mon avis

Ce qui rend `dockcheck` intéressant, c'est sa simplicité assumée. Un script bash, pas de dépendance lourde, pas de service à maintenir. Il s'inscrit dans une logique d'**automatisation progressive** : on vérifie, on notifie, on décide ensuite. C'est plus sain que du full-auto sur des mises à jour d'images.

L'option de délai avant application des updates est un vrai plus. En production, même légère, appliquer une release le jour de sa sortie c'est prendre un risque inutile. Pouvoir dire "attends 48h avant de me proposer cette mise à jour" change la donne côté fiabilité.

Les intégrations Prometheus et Zabbix montrent que l'outil a trouvé sa place dans des stacks d'observabilité existantes. Pour des équipes plateforme qui gèrent du self-hosting ou des environnements de staging avec beaucoup de containers, c'est le type d'outil qu'on branche en 10 minutes et qui rend service durablement.

À noter : ça ne remplace pas un **Renovate** ou un workflow GitOps complet pour des environnements critiques. Mais pour tout le reste — homelab, pré-prod, services internes — c'est une brique d'automatisation légère et pragmatique.

🔗 [Article source](https://selfh.st/post/dockcheck-cli-container-updates/)
