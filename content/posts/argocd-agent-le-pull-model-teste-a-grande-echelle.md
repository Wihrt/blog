---
title: "ArgoCD Agent : le pull model testé à grande échelle"
slug: "argocd-agent-le-pull-model-teste-a-grande-echelle"
date: 2026-11-19T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Red Hat teste argocd-agent sur 480 clusters : performances, limites et bottlenecks du pull model GitOps."
tags:
  - kubernetes
  - gitops
  - argocd
  - devops
  - platform-engineering
series:
  - Veille techno
series_order: 196
showTableOfContents: true
---

## Un test de charge grandeur nature pour le pull model GitOps

Le modèle push (hub-and-spoke) reste la norme pour beaucoup de déploiements ArgoCD, mais il pose des problèmes connus : exposition réseau des clusters managés et charge centralisée sur le hub. Red Hat propose depuis peu argocd-agent, une architecture pull intégrée à OpenShift GitOps, et vient de publier les résultats d'un test de charge poussé.

## Ce que dit l'article

Les équipes Red Hat ont monté un lab de 42 machines physiques pour simuler jusqu'à 500 clusters spoke. Ils ont poussé le test jusqu'à 480 clusters actifs, 31 200 applications et 3,1 millions de ressources gérées.

Les résultats mesurés :

- Bootstrap sync : environ 13 minutes

- Sync-to-commit : environ 13 minutes

- Suppression en cascade de toutes les applications : moins de 5 minutes

- Réduction du trafic réseau cross-cluster : jusqu'à 80% par rapport au modèle push classique

Le test a aussi mis en lumière plusieurs points de friction : limites de débit de l'API Kubernetes et d'etcd, traitement lent des informers, tempêtes de retry sur l'event writer, et surcharge mémoire du contrôleur ApplicationSet. Ces constats alimentent directement les prochaines optimisations d'OpenShift GitOps.

## Ce que ça change concrètement

L'objectif reste toujours le même : trouver des outils qui facilitent l'automatisation sans sacrifier la sécurité ni la stabilité. Le modèle pull répond à un vrai besoin sur les fleets à grande échelle : plus besoin d'exposer les clusters managés vers le hub, et la charge de calcul se distribue sur les agents plutôt que de saturer un point central.

Pour une équipe Platform Engineering qui gère des dizaines ou centaines de clusters, ces chiffres donnent une base concrète pour évaluer la migration. Mais les bottlenecks identifiés (etcd, informers, ApplicationSet) rappellent qu'une architecture pull bien pensée ne dispense pas d'un travail de tuning continu sur les couches sous-jacentes de Kubernetes.

Source : https://developers.redhat.com/articles/2026/09/24/scaling-gitops-pull-architecture-global-fleets
