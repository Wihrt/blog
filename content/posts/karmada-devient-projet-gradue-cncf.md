---
title: "Karmada devient projet gradué CNCF"
slug: "karmada-devient-projet-gradue-cncf"
date: 2026-11-27T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Karmada, orchestrateur multi-cluster Kubernetes, atteint la graduation CNCF avec la v1.19 et une roadmap IA/GPU."
tags:
  - kubernetes
  - open-source
  - platform-engineering
  - automation
  - devops
series:
  - Veille techno
series_order: 199
showTableOfContents: true
---

## Karmada passe le cap de la graduation CNCF

La Cloud Native Computing Foundation a annoncé la graduation de Karmada, un projet open source qui étend les APIs Kubernetes pour orchestrer des applications sur plusieurs clusters, clouds et régions, sans nécessiter de modification des applications elles-mêmes. Ce statut de "graduated" marque le plus haut niveau de maturité reconnu par la CNCF.

## Ce que dit l'article

Karmada a rejoint la CNCF en tant que projet Sandbox en septembre 2021, puis est passé en Incubating en décembre 2023. La graduation intervient après un audit de sécurité tiers et la mise en place d'une gouvernance formelle.

La version 1.19 apporte deux avancées notables :

- Un scheduling multi-composants pour les jobs d'entraînement IA distribués.
- Le passage en Beta, activé par défaut, du scheduling basé sur la priorité.

Le projet est adopté par Bloomberg, Wellhub, Alibaba Cloud, Huawei et Trip.com. Il compte aujourd'hui plus de 1214 contributeurs, 292 organisations contributrices et plus de 5600 stars GitHub. La roadmap 2026 prévoit la préemption basée sur la priorité, du queuing multi-cluster pour l'entraînement IA, et le support multi-cluster pour Kubernetes Dynamic Resource Allocation sur GPU.

## Mon avis

L'intérêt principal de Karmada, c'est de rendre l'automatisation du multi-cluster transparente au niveau API. Pas besoin de réécrire les manifests ou d'ajouter une couche applicative spécifique : le placement, le scaling et maintenant la priorisation se gèrent directement via les mécanismes Kubernetes étendus.

Pour une équipe Platform Engineering qui gère du multi-cloud ou du multi-région, ça change la donne sur la charge opérationnelle. Gérer manuellement le placement de workloads sur plusieurs clusters devient vite intenable dès qu'on dépasse quelques environnements.

La graduation CNCF, avec audit de sécurité et gouvernance formelle, est un signal de confiance pour l'adoption en production. La roadmap orientée IA (queuing, GPU via DRA) montre aussi que Karmada s'aligne sur les besoins actuels des infrastructures d'entraînement distribué, ce qui en fait un candidat sérieux à surveiller pour les équipes qui commencent à scaler leurs workloads IA sur plusieurs clusters.

Source : https://www.cncf.io/announcements/2026/09/07/cloud-native-computing-foundation-announces-karmada-graduation
