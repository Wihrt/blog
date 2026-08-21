---
title: "Single Front Door : la porte d'entrée unique des devs de Mercari"
slug: "single-front-door-mercari"
date: 2025-12-25T08:00:03+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Mercari a consolidé outils et workflows derrière un point d'entrée unique, avec Argo Workflows et des intégrations IDE via MCP."
tags:
  - platform-engineering
  - gitops
  - devops
  - ai
series:
  - Veille techno
series_order: 58
showTableOfContents: true
---

## Introduction

Dans le monde du développement logiciel, la diversité des outils et des flux de travail peut souvent être déroutante. En tant que développeur, je cherche constamment à simplifier mes processus tout en maintenant un haut niveau d'efficacité. C'est là qu'intervient Single Front Door (SFD) de Mercari, une interface unifiée pour gérer et intégrer nos outils de développement.

## Résumé

Mercari a construit la plateforme Single Front Door (SFD), qui consolide divers outils et flux de travail des développeurs en un point d'entrée unique. SFD utilise Argo Workflows pour exécuter les opérations GitOps via le CLI ou des intégrations IDE alimentées par l'IA, grâce au Model Context Protocol. Les défis techniques incluaient la gestion des identifiants basés sur OAuth pour assurer un contrôle d'accès approprié à grande échelle, et la configuration de l'IAM avec RBAC Kubernetes pour un accès sécurisé aux services externes comme GCP et GitHub.

## Utilité pros tech

Ce système vise à devenir un moteur de flux de travail modulaire avec des blocs de construction réutilisables pour la provision d'infrastructure, la configuration de services et les opérations CI/CD. En tant que professionnel de la tech, je trouve cette approche particulièrement utile pour sa capacité à simplifier les tâches complexes et à réduire les erreurs humaines.

## Mon expérience

Intégrer SFD dans mon flux de travail a été une révélation. La transition vers une interface unique m'a non seulement fait gagner du temps, mais a également réduit les frictions entre différents outils que j'utilisais auparavant. Grâce à l'intégration fluide avec mon IDE préféré, j'ai pu automatiser davantage de processus, ce qui m'a permis de me concentrer sur l'essentiel : coder.

## Conclusion

En somme, l'interface SFD de Mercari représente une avancée significative dans le monde du développement. Elle offre une solution efficace aux développeurs cherchant à rationaliser leurs opérations. Je recommande à tout professionnel du développement de l'adopter pour améliorer ses pratiques et gagner en efficacité.

[Lire l'article complet](https://api.daily.dev/r/veG1qnzxV)
