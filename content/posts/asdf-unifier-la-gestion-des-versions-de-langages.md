---
title: "asdf : unifier la gestion des versions de langages"
slug: "asdf-unifier-la-gestion-des-versions-de-langages"
date: 2026-10-07T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "asdf remplace pyenv, nvm, rbenv et goenv par un outil unique, avec des bénéfices pour la cohérence des environnements DevOps."
tags:
  - devops
  - automation
  - platform-engineering
  - cli
series:
  - Veille techno
series_order: 92
showTableOfContents: true
---

## Contexte

Dans un environnement de développement ou d'intégration continue, la gestion des versions de langages est souvent sous-estimée. On finit par empiler `pyenv` pour Python, `nvm` pour Node.js, `rbenv` pour Ruby, `goenv` pour Go… chacun avec sa logique d'installation, ses variables d'environnement, ses fichiers de configuration.

## Ce que propose asdf

`asdf` est un gestionnaire de versions polyglotte qui unifie cette gestion sous une interface commune. Les points clés :

- Un seul outil à installer et à maintenir, via `git` ou un package manager système.
- Un fichier `.tool-versions` par projet, versionnable, qui déclare les versions nécessaires pour chaque langage utilisé.
- Un système de plugins extensible qui couvre bien au-delà de Python, Node.js, Ruby et Go.
- Une documentation officielle complète disponible sur [asdf-vm.com](https://asdf-vm.com/core-manage-asdf).

## Analyse

L'intérêt d'`asdf` ne se limite pas au confort du développeur individuel. Dans une perspective DevOps ou Platform Engineering, standardiser le gestionnaire de versions a des implications concrètes.

Premièrement, **la cohérence des environnements**. Un fichier `.tool-versions` commité dans chaque dépôt, c'est une source de vérité partagée entre le poste local, les environnements de test et les pipelines CI. Moins de divergences, moins de bugs liés à une version de runtime inattendue.

Deuxièmement, **la réduction de la surface d'outillage**. Chaque outil supplémentaire dans la chaîne est un point de maintenance, une dépendance à mettre à jour, une documentation à connaître. Consolider vers `asdf` réduit cette charge, surtout dans des équipes avec des profils multi-langages.

Troisièmement, **l'automatisation de l'onboarding**. Un script de bootstrap qui installe `asdf` et ses plugins devient le point d'entrée unique pour préparer un environnement de développement, quel que soit le stack.

La vraie difficulté reste l'adoption : migrer des habitudes installées demande de l'évangélisation interne et un accompagnement. Mais dans une logique de platform engineering, c'est exactement le type de standardisation qui paie sur la durée.

## Source

https://jinyuz.dev/posts/tips-and-tricks/Switching-from-pyenv,-rbenv,-goenv-and-nvm-to-asdf
