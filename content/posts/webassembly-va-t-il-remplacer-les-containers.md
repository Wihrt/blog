---
title: "WebAssembly va-t-il remplacer les containers ?"
slug: "webassembly-va-t-il-remplacer-les-containers"
date: 2026-11-11T18:41:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "WASM promet un vrai write-once-run-anywhere, mais reste immature pour le stockage, réseau et l'observabilité en production."
tags:
  - platform-engineering
  - docker
  - cloud
  - rust
  - go
  - automation
series:
  - Veille techno
series_order: 154
showTableOfContents: true
---

## Introduction

WebAssembly (WASM) revient régulièrement dans les discussions sur l'avenir de l'infrastructure cloud. L'article de Creston.blog pose la question directement : et si WASM rendait les containers obsolètes ? Le sujet est sérieux, même si la réponse est encore nuancée.

## Ce que dit l'article

L'argument central est que WASM offre un vrai modèle **write-once-run-anywhere** — plus universel que ce que Docker a pu promettre. Les points clés :

- WASM s'exécute dans un sandbox léger, sans OS invité ni runtime lourd.
- Les limitations actuelles sont réelles : pas d'accès natif au système de fichiers, réseau limité. Mais les specs WASI progressent.
- Des plateformes comme **Cloudflare Workers** montrent déjà ce que ça donne en production.
- WASM combine certains avantages des microservices (isolation, déploiement granulaire) et des monolithes (simplicité d'exécution).
- Les langages à maîtriser pour s'y préparer : `Go` et `Rust`.

## Point de vue

L'angle qui retient l'attention ici n'est pas tant le remplacement de Docker — ce serait aller vite en besogne — que ce que WASM change pour **l'automatisation et les équipes platform**.

Un binaire WASM portable et léger, c'est potentiellement moins de couches d'infrastructure à configurer et maintenir. Pour des pipelines CI/CD, des workloads serverless ou des fonctions d'extension dans des outils platform, c'est une surface d'automatisation intéressante. L'effort se déplace : on passe de la gestion de l'environnement d'exécution à la logique métier elle-même.

Cela dit, il faut rester lucide sur la maturité. Les cas d'usage critiques — stockage, réseau, observabilité — ne sont pas encore couverts de manière stable. Les équipes qui veulent investir maintenant le font sur un pari technologique, pas sur une solution prête pour la production générale.

Pour une équipe platform engineering, la posture raisonnable est de **surveiller l'écosystème**, d'expérimenter sur des workloads non critiques, et de monter en compétence sur `Rust` ou `Go` dès maintenant. Ce sont des investissements utiles quelle que soit l'issue.

## Source

https://creston.blog/wasm-will-replace-containers/
