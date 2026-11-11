---
title: "eks-node-viewer : visualiser la capacité des nœuds EKS"
slug: "eks-node-viewer-visualiser-la-capacite-des-n-uds-eks"
date: 2026-11-11T18:29:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Outil CLI d'AWS Labs pour visualiser les ressources demandées par les pods sur chaque nœud EKS, utile avant scaling."
tags:
  - kubernetes
  - cloud
  - devops
  - platform-engineering
  - cli
series:
  - Veille techno
series_order: 142
showTableOfContents: true
---

## Introduction

Dans un cluster EKS actif, comprendre ce qui est schedulé sur chaque nœud — et ce qui reste disponible — est une étape clé avant toute décision d'automatisation. `eks-node-viewer` est un outil en ligne de commande développé par AWS Labs qui répond précisément à ce besoin de lisibilité.

## Ce que fait eks-node-viewer

`eks-node-viewer` est un outil de visualisation dynamique des nœuds d'un cluster EKS. Il affiche, pour chaque nœud, les ressources demandées par les pods schedulés (CPU, mémoire) en regard de la capacité allocatable du nœud.

Quelques points clés :

- Il ne mesure **pas** l'usage effectif des ressources (pas de métriques temps réel type Prometheus).
- Installation via `brew install eks-node-viewer` ou `go install`.
- Support de labels personnalisés pour enrichir l'affichage par nœud.
- Options CLI pour filtrer par ressource, trier, et adapter l'affichage au contexte.

C'est un outil d'inspection ponctuelle, pas un système de monitoring continu.

## Pourquoi c'est pertinent pour les équipes Platform/DevOps

L'automatisation du scaling dans Kubernetes — via Karpenter, Cluster Autoscaler ou des politiques custom — repose sur une bonne compréhension de l'état réel du cluster. Or, cette lisibilité manque souvent dans les outils du quotidien.

`eks-node-viewer` s'insère bien dans plusieurs cas d'usage concrets :

- **Identifier des nœuds sous-utilisés** avant d'ajuster une politique de consolidation.
- **Diagnostiquer des pods pending** en visualisant rapidement où la capacité est consommée.
- **Valider une configuration Karpenter** en observant la distribution des demandes après un changement.

Ce n'est pas un outil de remplacement pour Prometheus ou Grafana. C'est un complément d'analyse rapide, pensé pour le terminal, qui accélère les investigations sans nécessiter de setup complexe. Dans une démarche d'automatisation, ce type d'outillage léger a sa place : mieux observer ponctuellement, c'est prendre de meilleures décisions structurelles.

## Source

https://github.com/awslabs/eks-node-viewer
