---
title: "Impératif vs déclaratif : impact sur le Platform Engineering"
slug: "imperatif-vs-declaratif-impact-sur-le-platform-engineering"
date: 2026-11-11T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Pourquoi Terraform, Kubernetes et ArgoCD privilégient le paradigme déclaratif pour l'automatisation d'infrastructure."
tags:
  - platform-engineering
  - terraform
  - kubernetes
  - argocd
  - devops
  - gitops
series:
  - Veille techno
series_order: 115
showTableOfContents: true
---

## Introduction

La distinction entre paradigme impératif et déclaratif est souvent présentée comme un sujet académique. En réalité, elle structure une grande partie des choix d'outillage en DevOps et Platform Engineering. Comprendre cette différence, c'est mieux comprendre pourquoi l'écosystème d'automatisation a évolué dans la direction qu'on lui connaît.

## Ce que dit l'article

L'article d'Educative pose les fondations des deux paradigmes :

- **Impératif** : on décrit explicitement les étapes à suivre pour atteindre un résultat. Le développeur contrôle le flux d'exécution.
- **Déclaratif** : on décrit l'état ou le résultat attendu. C'est le langage, le compilateur ou le runtime qui détermine comment y parvenir.

Ces deux approches coexistent dans la plupart des environnements modernes. Des langages comme `Python` ou `C++` supportent les deux styles selon le contexte. La programmation fonctionnelle s'inscrit naturellement dans le paradigme déclaratif.

L'article identifie 5 différences clés : lisibilité, contrôle, abstraction, maintenabilité et débogage.

## Avis

En Platform Engineering, ce débat n'est pas théorique. L'orientation vers le déclaratif dans les outils d'infrastructure — Terraform, Kubernetes, Helm, ArgoCD — répond à un besoin concret : **réduire la charge cognitive liée à l'automatisation**.

Quand on décrit un état cible plutôt qu'une séquence d'actions, plusieurs choses deviennent plus simples :

- La **convergence** : l'outil sait ramener le système à l'état souhaité, quoi qu'il arrive.
- La **lisibilité** : un fichier de manifeste K8s est plus facile à relire en revue de code qu'un script Bash de 300 lignes.
- La **maintenabilité** : moins de logique conditionnelle à gérer, moins de bugs liés à l'ordre d'exécution.

Cela ne signifie pas que l'impératif n'a plus sa place. Pour des opérations ponctuelles, du scripting fin ou des cas où le contrôle d'exécution est critique, il reste pertinent. Mais en termes de posture par défaut pour l'automatisation à l'échelle, le déclaratif s'impose pour de bonnes raisons.

L'objectif reste constant : trouver les paradigmes et les outils qui réduisent la friction, accélèrent les livraisons et limitent les erreurs humaines.

## Source

https://dev.to/educative/declarative-vs-imperative-programming-5-key-differences-2m1
