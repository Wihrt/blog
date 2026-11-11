---
title: "DDEV et Colima : environnements de dev local conteneurisés"
slug: "ddev-et-colima-environnements-de-dev-local-conteneurises"
date: 2026-11-11T18:13:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "DDEV associé à Colima remplace WAMP/MAMP/XAMPP par des environnements locaux Docker versionnés et reproductibles par projet."
tags:
  - docker
  - devops
  - platform-engineering
  - self-hosted
  - automation
series:
  - Veille techno
series_order: 126
showTableOfContents: true
---

## Introduction

Les environnements de développement local sont souvent négligés dans les stratégies DevOps. Pourtant, c'est là que tout commence. DDEV, couplé à Colima sur macOS, propose une approche conteneurisée moderne pour remplacer les stacks monolithiques du type WAMP, MAMP ou XAMPP.

## Ce que dit l'article

DDEV s'appuie sur Docker pour fournir des environnements de développement local isolés et configurables par projet. Contrairement aux solutions traditionnelles, chaque projet définit ses propres versions de serveur web, de base de données ou d'autres services. Colima intervient comme runtime Docker léger sur macOS, en alternative à Docker Desktop.

Concrètement :

- Pas de conflit de versions entre projets
- La configuration est versionnée avec le code
- L'environnement est reproductible sur n'importe quelle machine
- Le onboarding d'un nouveau développeur se réduit à quelques commandes

## Avis

L'idée centrale ici, c'est que l'automatisation ne démarre pas dans le pipeline CI/CD — elle démarre sur le poste de travail. Un environnement local codifié, versionnable et partageable, c'est la base d'une chaîne DevOps cohérente.

Les stacks type XAMPP ont rendu service, mais elles imposent une configuration globale sur la machine, propice aux dérives et aux « ça marche chez moi ». DDEV déplace la responsabilité de la configuration au niveau du projet, ce qui est bien plus sain à l'échelle d'une équipe.

Pour une équipe Platform Engineering, ce type d'outil a des implications directes : moins de tickets de support liés aux envs locaux, un `README` d'installation qui reste crédible dans le temps, et une parité dev/prod améliorée sans surcoût infrastructure.

Ce n'est pas l'outil le plus visible dans une stack DevOps, mais c'est le genre d'investissement discret qui s'accumule en valeur sur la durée.

## Source

https://opensource.com/article/22/9/docker-desktop-colima
