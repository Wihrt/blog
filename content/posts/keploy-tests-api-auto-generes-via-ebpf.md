---
title: "Keploy : tests API auto-générés via eBPF"
slug: "keploy-tests-api-auto-generes-via-ebpf"
date: 2026-11-17T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Keploy génère tests et mocks API/E2E depuis le trafic réseau réel via eBPF, sans SDK ni modification de code."
tags:
  - automation
  - api
  - ci-cd
  - open-source
  - ai
  - go
series:
  - Veille techno
series_order: 194
showTableOfContents: true
---

## Le problème des tests d'intégration

Écrire et maintenir des tests d'intégration et E2E reste une des tâches les plus chronophages sur des systèmes avec de nombreuses dépendances externes (bases de données, queues, APIs tierces). Keploy propose une approche différente : générer ces tests automatiquement à partir du trafic réel, sans toucher au code.

## Ce que fait Keploy

Keploy est une plateforme open-source qui capture le trafic au niveau réseau via eBPF. Concrètement, ça veut dire :

- Pas de SDK à installer, pas de modification de code applicatif.

- Capture et rejeu non seulement des appels HTTP, mais aussi des interactions avec des bases de données (Postgres, MySQL, MongoDB) et des systèmes de messaging (Kafka, RabbitMQ).

- Rejeu déterministe des scénarios, sans avoir besoin de reprovisionner toute l'infrastructure à chaque test.

L'outil ajoute aussi un reporting de couverture combinant statements, branches et schémas API, une fonctionnalité d'expansion de couverture pilotée par IA, une intégration CI/CD, du time freezing, et un registre de mocks. Comme l'interception se fait au niveau réseau plutôt que via des SDK spécifiques à un langage, Keploy fonctionne en théorie avec n'importe quel langage ou framework.

## Pourquoi ça compte pour les équipes Platform

L'automatisation des tests d'intégration est un vrai angle mort dans beaucoup d'organisations : ça prend du temps, ça demande de maintenir des environnements de test complexes, et ça finit souvent négligé. Une approche qui capture le trafic réel pour générer tests et mocks réduit directement cette friction.

Le point fort ici, c'est l'indépendance vis-à-vis du langage. Sur des stacks hétérogènes (ce qui est la norme dans la plupart des organisations), ne pas avoir à instrumenter chaque service avec un SDK spécifique facilite grandement l'adoption et la maintenance à long terme.

Reste à valider en conditions réelles la robustesse des mocks générés sur des flux complexes, et l'overhead de la capture eBPF en production ou en environnement de staging à fort trafic. Mais l'idée de fond — s'appuyer sur ce qui existe déjà plutôt que de tout écrire à la main — va clairement dans le bon sens pour qui cherche à automatiser davantage son pipeline de tests.

Source : https://github.com/keploy/keploy
