---
title: "Rybbit : des analytics open source et self-hosted"
slug: "rybbit-des-analytics-open-source-et-self-hosted"
date: 2026-11-11T19:06:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Rybbit, alternative à Google Analytics sans cookies, conforme GDPR, déployable en self-hosted et automatisable."
tags:
  - open-source
  - self-hosted
  - platform-engineering
  - observability
  - automation
series:
  - Veille techno
series_order: 179
showTableOfContents: true
---

## Introduction

Dans un contexte où la conformité privacy devient un prérequis et où les équipes plateforme cherchent à maîtriser chaque composant de leur stack, les outils d'analytics méritent qu'on s'y attarde. Rybbit est un projet open source qui propose une alternative concrète à Google Analytics, avec le self-hosting comme option native.

## Ce que propose Rybbit

Rybbit est un outil d'analytics web **sans cookies et sans tracking utilisateur**, conforme GDPR et CCPA par design. Parmi les fonctionnalités clés :

- **Dashboards temps réel** avec des métriques classiques (pages vues, sessions, sources, etc.)
- **Goals personnalisables** pour suivre des conversions ou des événements spécifiques
- **Filtrage avancé** sur l'ensemble des dimensions collectées
- **Support multi-sites** avec gestion par organisation
- **Déploiement rapide** : SaaS ou self-hosted

Le projet est hébergé sur GitHub et semble activement maintenu.

## Mon avis

Ce qui retient mon attention sur ce type d'outil, c'est son potentiel d'intégration dans une logique d'automatisation. Quand on construit une plateforme interne, chaque service déployé doit pouvoir être provisionné, configuré et maintenu comme du code. Un analytics self-hosted coche cette case : on le déploie via Terraform ou Helm, on le branche sur son reverse proxy, on maîtrise la rétention des données.

Concrètement, pour des équipes qui exposent des **developer portals**, des **docs internes** ou des **outils en self-service**, avoir un analytics maîtrisé évite de dépendre d'un Google Analytics souvent mal configuré, ou pire, bloqué par les politiques internes de l'entreprise.

À noter : le projet est encore jeune. Avant de l'adopter en production, il faut évaluer la maturité du modèle de données, les options d'export, et la capacité à tenir la charge. Mais comme brique d'observabilité orientée usage, c'est une piste à suivre.

## Source

https://github.com/rybbit-io/rybbit
