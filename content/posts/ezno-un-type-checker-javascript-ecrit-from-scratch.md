---
title: "Ezno : un type checker JavaScript écrit from scratch"
slug: "ezno-un-type-checker-javascript-ecrit-from-scratch"
date: 2026-10-02T11:51:43+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Ezno propose un compilateur JS avec type checker maison, pensé pour la correction et la performance en full-stack."
tags:
  - typescript
  - platform-engineering
  - ci-cd
  - open-source
series:
  - Veille techno
series_order: 89
showTableOfContents: true
---

## Introduction

Ezno est un compilateur JavaScript expérimental qui embarque son propre type checker, écrit from scratch et compatible avec les annotations TypeScript. Dans un écosystème JS déjà chargé d'outils, ce qui distingue Ezno, c'est son ambition de reconstruire la vérification de types sans dépendre de `tsc` — avec des objectifs affichés de correction et de performance.

## Ce que fait Ezno

Voici les points clés du projet :

- **Type checker maison** : pas un wrapper autour du compilateur TypeScript officiel, une implémentation indépendante compatible avec les annotations TS existantes.
- **Orienté correctness** : l'objectif n'est pas seulement de parser du JS, mais de garantir un niveau de rigueur plus élevé sur la vérification statique.
- **Full-stack** : le compilateur cible les deux contextes d'exécution — client et serveur — ce qui le positionne sur des architectures comme SSR ou les frameworks hybrides.
- **Performance** : la réécriture from scratch vise aussi à améliorer les temps de traitement, un point critique sur les gros projets JS.

## Avis

L'intuition derrière cet article est simple : trouver des outils qui facilitent l'automatisation. Et c'est exactement le prisme sous lequel Ezno devient intéressant pour des équipes DevOps ou Platform Engineering.

Un type checker plus strict et plus performant, c'est d'abord un outil qui **déplace la détection d'erreurs vers la gauche du pipeline** — avant les tests d'intégration, avant le déploiement. Dans une logique de CI/CD, chaque erreur remontée au moment de la compilation plutôt qu'en production, c'est du temps gagné et un cycle de feedback réduit.

Ezno n'est pas encore un outil de production mature, et il serait prématuré de l'intégrer dans des pipelines critiques aujourd'hui. Mais la direction prise — construire un compilateur où **correctness et performance sont des contraintes de premier rang** — est cohérente avec ce qu'on attend d'un outillage sérieux pour des stacks full-stack JS.

À surveiller particulièrement si vous gérez des projets où la frontière client/serveur est un point de friction récurrent, et où un type checking plus agressif pourrait réduire les bugs liés aux incompatibilités de types entre les deux contextes.

## Lien source

https://kaleidawave.github.io/posts/introducing-ezno
