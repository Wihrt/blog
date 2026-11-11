---
title: "chaoskube : tester la résilience Kubernetes simplement"
slug: "chaoskube-tester-la-resilience-kubernetes-simplement"
date: 2026-11-11T18:26:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "chaoskube tue des pods aléatoirement pour tester la résilience Kubernetes, avec filtres et mode dry-run."
tags:
  - kubernetes
  - devops
  - helm
  - open-source
  - platform-engineering
series:
  - Veille techno
series_order: 139
showTableOfContents: true
---

## Introduction

Tester la résilience d'un cluster Kubernetes ne devrait pas nécessiter un outillage complexe pour commencer. `chaoskube` propose une approche directe : tuer des pods de façon aléatoire et périodique pour observer comment le système se comporte face à des défaillances arbitraires.

## Ce que fait chaoskube

`chaoskube` est un outil open source qui s'exécute dans un cluster Kubernetes et supprime des pods à intervalles configurables. Les principales fonctionnalités :

- **Filtrage des cibles** : par namespace, labels, annotations, et âge du pod
- **Exclusions temporelles** : possibilité de bloquer certaines heures ou jours (pas de chaos le vendredi soir, c'est raisonnable)
- **Installation simple** via Helm
- **Configuration par flags** : intervalle de chaos, cluster cible, comportement en mode dry-run

Le mode dry-run permet de simuler sans agir, utile pour valider la configuration avant de passer en conditions réelles.

## Avis

L'automatisation de la résilience est souvent traitée comme un chantier secondaire dans les équipes plateforme. Les outils comme LitmusChaos ou Chaos Mesh sont puissants, mais leur surface de configuration peut décourager une adoption rapide. `chaoskube` ne cherche pas à concurrencer ces solutions : il fait une chose, il la fait bien, et il s'intègre dans un pipeline existant sans friction.

Ce qui est particulièrement bien pensé, c'est le filtre par âge de pod. Éviter de cibler des pods qui viennent de démarrer, c'est éviter des faux positifs dans les alertes et des situations confuses lors des tests. Ce genre de détail révèle une réflexion terrain.

Pour une équipe qui veut commencer à valider sa résilience applicative sans investissement lourd, `chaoskube` est un point d'entrée sérieux. Il s'inscrit dans une logique d'automatisation progressive : on commence simple, on mesure, on complexifie si le besoin est réel. C'est souvent le bon ordre.

## Source

https://github.com/linki/chaoskube
