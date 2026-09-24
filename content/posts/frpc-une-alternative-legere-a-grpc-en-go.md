---
title: "fRPC : une alternative légère à gRPC en Go"
slug: "frpc-une-alternative-legere-a-grpc-en-go"
date: 2026-09-24T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Présentation de fRPC, framework RPC en early alpha de Loophole Labs, pensé pour la légèreté et l'automatisation."
tags:
  - go
  - api
  - platform-engineering
  - automation
  - open-source
series:
  - Veille techno
series_order: 81
showTableOfContents: true
---

## Introduction

Alors que gRPC s'est imposé comme standard de facto pour la communication inter-services en environnement cloud-native, sa complexité et son poids peuvent devenir des obstacles dans des contextes orientés outillage ou automatisation. `fRPC` est une tentative de réponse à ce problème, avec une approche pensée dès la conception pour la légèreté et la performance.

## Ce que propose fRPC

`fRPC` est un framework RPC développé par Loophole Labs, écrit en Go, actuellement disponible en **early alpha** sous licence Apache 2. Voici les points clés :

- **Format de messagerie entièrement custom** : pas de dépendance à Protobuf ou à un sérialiseur tiers.
- **Génération de code optimisée** : le client et le serveur générés sont conçus pour minimiser les allocations et maximiser le débit.
- **Benchmarks sur réseau local** : le choix de ce contexte permet d'isoler les performances intrinsèques du framework, sans bruit lié à la latence réseau.
- **Extensibilité** : l'architecture est pensée pour être modulaire et adaptable.

## Analyse

Dans une logique d'automatisation et de platform engineering, la communication entre composants internes est souvent sous-estimée. On intègre gRPC parce que c'est le standard, sans forcément questionner si son overhead est justifié pour le cas d'usage.

`fRPC` soulève une question pertinente : est-ce qu'un framework RPC plus ciblé, avec moins d'abstractions, peut réduire la friction dans la construction d'outils internes ou de pipelines de traitement ?

L'angle extensibilité est particulièrement intéressant pour des équipes plateforme qui construisent des agents, des controllers ou des CLI communiquant avec des backends Go. Moins de boilerplate, un protocole maîtrisé de bout en bout, c'est une surface d'intégration plus prévisible.

Cela dit, **l'alpha est une limite réelle**. Pas de stabilité d'API garantie, écosystème embryonnaire, interopérabilité non prouvée à grande échelle. Ce n'est pas un outil pour demain en production, mais c'est un projet à suivre pour quiconque cherche à optimiser ses couches de communication dans des contextes d'automatisation.

## Source

https://loopholelabs.io/blog/announcing-frpc
