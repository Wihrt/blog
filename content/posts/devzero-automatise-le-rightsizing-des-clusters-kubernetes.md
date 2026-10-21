---
title: "DevZero automatise le rightsizing des clusters Kubernetes"
slug: "devzero-automatise-le-rightsizing-des-clusters-kubernetes"
date: 2026-10-21T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "DevZero lance une plateforme de rightsizing continu pour Kubernetes, promettant 30 à 60% d'économies via profiling et migration live."
tags:
  - kubernetes
  - platform-engineering
  - automation
  - cloud
series:
  - Veille techno
series_order: 102
showTableOfContents: true
---

## Contexte

Le surprovisionnement des clusters Kubernetes est un problème connu, documenté, et pourtant persistant. DevZero vient de lancer une plateforme qui tente d'y répondre par l'automatisation continue plutôt que par des ajustements ponctuels.

## Ce que fait la plateforme

Le fonctionnement repose sur du **profiling continu** combiné à de la **modélisation statistique** pour rightsizer les workloads en temps réel. Concrètement :

- Ajustement dynamique de CPU, mémoire et GPU
- Couverture de 3 000+ types d'instances sur 80 régions cloud
- Promesse de réduction de coûts entre **30 et 60 %**
- Mécanisme de **checkpoint-restore** permettant la migration de workloads live sans redémarrage

Ce dernier point est techniquement non trivial : déplacer un workload sans interruption de service sur Kubernetes reste un défi, surtout en production.

## Pourquoi ce sujet est pertinent maintenant

DevZero cite un chiffre significatif : les équipes IT surdimensionnent leurs clusters Kubernetes de **53 % en moyenne**. Les causes sont bien connues — complexité de la plateforme, manque de visibilité sur les coûts réels, et une inertie culturelle qui pousse à provisionner large par précaution.

Ce phénomène s'aggrave avec la prolifération des workloads IA dépendants de GPU, dont le coût horaire est sans commune mesure avec une instance de compute classique. Provisionner un GPU A100 à 50 % d'utilisation réelle, c'est du gaspillage immédiatement visible sur la facture.

## Point de vue

L'orientation est bonne. L'automatisation du rightsizing est exactement le type de tâche qui devrait être sortie des mains des équipes — répétitive, technique, mais sans valeur ajoutée directe quand elle est faite manuellement.

Ce qui mérite attention avant d'adopter ce type d'outil en production :

- **La confiance dans le modèle** : un ajustement automatique de ressources sur un workload critique demande une validation sérieuse du comportement du système avant de lui laisser la main.
- **L'observabilité associée** : est-ce qu'on garde une traçabilité claire des décisions prises automatiquement ?
- **Les cas limites** : workloads avec des pics brutaux, jobs batch, workloads GPU intermittents — le modèle statistique doit savoir gérer la variance.

L'idée de fond reste solide : moins d'ajustements manuels, plus d'automatisation pilotée par les données. C'est la direction cohérente pour des équipes Platform Engineering qui veulent tenir leur FinOps sans y passer leurs journées.

## Source

https://cloudnativenow.com/features/devzero-launches-automation-platform-to-dynamically-rightsize-kubernetes-clusters
