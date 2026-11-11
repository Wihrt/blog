---
title: "GKE : un profil Performance HPA deux fois plus rapide"
slug: "gke-un-profil-performance-hpa-deux-fois-plus-rapide"
date: 2026-11-11T18:32:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Google lance un nouveau profil HPA sur GKE, deux fois plus rapide et scalable jusqu'à 1000 objets, pour limiter le sur-provisionnement."
tags:
  - kubernetes
  - cloud
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 145
showTableOfContents: true
---

## Contexte

L'Horizontal Pod Autoscaler de Kubernetes est un composant central dans la gestion des workloads dynamiques. Pourtant, sa latence de réaction a longtemps poussé les équipes à sur-provisionner par précaution. Google vient d'annoncer une évolution notable sur GKE.

## Ce que dit l'article

Google a introduit un nouveau profil pour le HPA de GKE, appelé **Performance HPA**. Les points clés :

- Vitesse de scaling **deux fois plus rapide** que le comportement par défaut.
- Support du **scaling linéaire jusqu'à 1000 objets HPA**, ce qui ouvre la voie à des clusters de grande taille sans dégradation des performances d'autoscaling.
- Disponible en **preview** sur GKE Standard et GKE Autopilot, sous forme d'opt-in.
- L'objectif affiché est de réduire le besoin de sur-provisionnement et d'améliorer la réactivité applicative.

## Analyse

Ce type d'amélioration s'inscrit dans une logique d'automatisation plus fiable. Quand un autoscaler met trop de temps à réagir, les équipes platform compensent souvent de deux façons : soit en sur-provisionnant les ressources de base, soit en ajustant manuellement les seuils pour déclencher le scaling plus tôt, au risque de le rendre trop agressif.

Un HPA deux fois plus rapide réduit mécaniquement cette friction. Moins besoin de prévoir large pour absorber le délai de montée en charge. Sur des environnements avec des pics de trafic courts et intenses — batch jobs, événements ponctuels — c'est la différence entre un scaling utile et un scaling qui arrive trop tard.

La montée en charge linéaire jusqu'à 1000 objets HPA est aussi un signal intéressant pour les équipes qui opèrent des plateformes multi-tenant avec de nombreux microservices indépendants. La limite de passage à l'échelle du plan de contrôle est souvent sous-estimée.

Cela dit, c'est encore en preview. Et un meilleur autoscaler ne dispense pas d'un travail rigoureux sur les métriques exposées et les seuils configurés. L'outil s'améliore, la responsabilité de configuration reste côté équipe.

## Source

https://cloud.google.com/blog/products/containers-kubernetes/rearchitected-gke-hpa-improves-scaling-performance/
