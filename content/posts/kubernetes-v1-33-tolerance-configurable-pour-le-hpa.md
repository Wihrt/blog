---
title: "Kubernetes v1.33 : tolérance configurable pour le HPA"
slug: "kubernetes-v1-33-tolerance-configurable-pour-le-hpa"
date: 2026-10-20T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Kubernetes v1.33 permet de configurer séparément la tolérance de scaleUp et scaleDown du HPA, pour un autoscaling plus fin."
tags:
  - kubernetes
  - devops
  - platform-engineering
  - automation
series:
  - Veille techno
series_order: 101
showTableOfContents: true
---

## Introduction

Kubernetes v1.33 introduit en alpha une fonctionnalité attendue par ceux qui opèrent de l'autoscaling à grande échelle : la possibilité de configurer la tolérance du Horizontal Pod Autoscaler (HPA). Un ajustement ciblé, mais qui répond à un vrai irritant opérationnel.

## Ce que dit l'article

Jusqu'à présent, le HPA utilisait une tolérance fixe de 10% pour évaluer s'il devait ajuster le nombre de réplicas en fonction de l'utilisation des ressources (CPU principalement). Impossible de modifier ce seuil sans intervenir dans le code ou contourner le mécanisme.

Avec le feature gate `HPAConfigurableTolerance`, Kubernetes v1.33 permet désormais de définir des tolérances distinctes pour le **scaleUp** et le **scaleDown**. Concrètement :

- On peut tolérer une marge plus large avant de scale-down, pour éviter le flapping.
- On peut réduire la tolérance en scale-up pour réagir plus vite à une montée de charge.
- Chaque configuration se fait au niveau du HPA, workload par workload.

La feature est encore en alpha et doit être activée explicitement.

## Avis

Ce type d'amélioration est exactement ce qui rend l'automatisation réellement exploitable en production. Le HPA avec sa tolérance fixe, c'est un outil qui marche bien dans les cas simples. Mais dès qu'on opère des déploiements conséquents — des dizaines ou centaines de pods — les effets de bord deviennent coûteux : scaling intempestif sur des micro-variations CPU, oscillations inutiles, ressources consommées pour rien.

Pouvoir découpler la sensibilité entre montée et descente en charge, c'est un vrai levier pour les équipes plateforme. Ça évite de devoir empiler des mécanismes externes (scripts, opérateurs custom, KEDA avec des hacks) pour compenser un comportement par défaut trop rigide.

C'est aussi révélateur d'une tendance dans l'écosystème Kubernetes : rendre les primitives natives plus configurables plutôt que de forcer les utilisateurs à aller chercher des solutions tierces. Pour les équipes DevOps/Platform Engineering, ça veut dire moins de complexité accidentelle dans la stack.

À surveiller dans les prochaines releases pour une promotion en beta. En attendant, c'est un bon candidat pour du test en environnement de staging sur des workloads à forte variabilité.

**Source :** [https://kubernetes.io/blog/2025/04/28/kubernetes-v1-33-hpa-configurable-tolerance/](https://kubernetes.io/blog/2025/04/28/kubernetes-v1-33-hpa-configurable-tolerance/)
