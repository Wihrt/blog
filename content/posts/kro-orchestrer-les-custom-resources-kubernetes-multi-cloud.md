---
title: "Kro : orchestrer les custom resources Kubernetes multi-cloud"
slug: "kro-orchestrer-les-custom-resources-kubernetes-multi-cloud"
date: 2026-11-11T18:55:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "AWS, Google et Microsoft s'associent sur Kro, projet open source alpha pour standardiser l'orchestration des CRDs Kubernetes."
tags:
  - kubernetes
  - open-source
  - platform-engineering
  - cloud
  - devops
series:
  - Veille techno
series_order: 168
showTableOfContents: true
---

## Introduction

Quand AWS, Google et Microsoft décident de collaborer sur un projet open source, le sujet mérite qu'on s'y arrête. Kro cible un point de friction bien connu des équipes platform engineering : l'orchestration des custom resources dans Kubernetes.

## Ce que propose Kro

Kro est un projet open source actuellement en phase alpha, né d'une collaboration entre les trois principaux fournisseurs cloud. Son objectif est double :

- **Simplifier l'orchestration des Custom Resources** dans Kubernetes, en proposant une couche d'abstraction commune plutôt que de laisser chaque organisation construire la sienne.
- **Rester cloud-agnostique**, ce qui permet de conserver la flexibilité nécessaire dans des environnements multi-cloud ou hybrides.

Le projet est né d'un constat partagé côté clients : les organisations qui construisent des plateformes internes sur Kubernetes se heurtent toutes aux mêmes problèmes d'orchestration entre CRDs. Kro veut standardiser ces patterns. La communauté a répondu présent, avec un intérêt significatif dès les premières annonces.

## Analyse

Dans la pratique quotidienne, la gestion des custom resources à l'échelle est un vrai sujet. Chaque équipe finit par développer ses propres opérateurs, ses propres conventions, sa propre glue entre les ressources. Le résultat : de la dette technique, des efforts dupliqués, et une maintenance qui devient lourde.

Avoir un outil commun porté par les trois hyperscalers, c'est potentiellement un moyen de **sortir de ces bricolages individuels** et de s'appuyer sur un socle partagé. Pour les équipes qui font du platform engineering, c'est le type de brique qui peut réduire significativement la complexité opérationnelle.

Mais il faut rester pragmatique. Le projet est en alpha. La collaboration entre trois concurrents directs n'est jamais garantie sur le long terme — les priorités stratégiques peuvent diverger. Il faudra observer si le projet atteint une gouvernance stable et une communauté suffisamment autonome pour survivre à d'éventuels désengagements.

L'automatisation des plateformes passe par de meilleurs outils d'orchestration. Si Kro arrive à maturité avec une API propre et un modèle extensible, il pourrait s'intégrer naturellement aux stacks existantes aux côtés de Crossplane ou des opérateurs maison. À surveiller de près dans les prochains mois.

## Source

https://thenewstack.io/the-kro-project-giving-kubernetes-users-what-they-want/
