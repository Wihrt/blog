---
title: "Kro : un orchestrateur de ressources pour Kubernetes"
slug: "kro-un-orchestrateur-de-ressources-pour-kubernetes"
date: 2026-11-11T18:43:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Kro introduit les ResourceGraphDefinitions pour composer des ressources Kubernetes liées, soutenu par AWS, Google Cloud et Microsoft."
tags:
  - kubernetes
  - helm
  - gitops
  - devops
  - platform-engineering
series:
  - Veille techno
series_order: 156
showTableOfContents: true
---

## Introduction

L'écosystème Kubernetes continue de s'enrichir d'outils visant à réduire la complexité opérationnelle. Kro, le Kube Resource Orchestrator, est le dernier en date à tenter de répondre à une question récurrente : comment rendre les configurations Kubernetes complexes plus maintenables et reproductibles ?

## Ce que fait Kro

Kro introduit le concept de **ResourceGraphDefinitions (RGD)**, qui permettent de regrouper plusieurs ressources Kubernetes en unités cohérentes et réutilisables. Concrètement, au lieu de gérer des manifests éparpillés ou des charts Helm difficiles à composer, on définit un graphe de ressources avec leurs dépendances.

Pour la gestion de la logique conditionnelle et des dépendances entre ressources, Kro s'appuie sur le **Common Expression Language (CEL)** — le même langage utilisé dans les admission webhooks et les CRD Kubernetes. Ce choix est cohérent avec l'écosystème existant.

Le projet bénéficie du soutien d'AWS, Google Cloud et Microsoft, ce qui lui confère une base de maintenance crédible dès le départ.

## Analyse

L'intention derrière Kro rejoint une problématique bien réelle pour les équipes plateforme : les outils actuels ont des angles morts. Helm gère bien le templating mais la gestion des dépendances entre ressources reste laborieuse. Kustomize est puissant pour les overlays mais peu adapté à la composition de ressources interdépendantes.

Si Kro tient ses promesses, il pourrait apporter une vraie valeur sur les cas d'usage où l'on doit orchestrer des ensembles de ressources avec des relations explicites — typiquement des stacks applicatives complètes avec RBAC, ConfigMaps, Deployments et Services liés.

Cela dit, l'enjeu reste la **charge cognitive**. Un outil d'automatisation qui simplifie le déploiement mais complexifie la compréhension du système ne résout pas le problème de fond. La lisibilité des RGD et la facilité de debugging en cas d'erreur seront déterminantes pour l'adoption en équipe.

À surveiller en conditions réelles avant d'envisager une intégration dans une plateforme interne.

## Source

https://thenewstack.io/kubernetes-gets-a-new-resource-orchestrator-in-the-form-of-kro/
