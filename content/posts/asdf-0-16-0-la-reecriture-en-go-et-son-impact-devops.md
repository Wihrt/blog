---
title: "asdf 0.16.0 : la réécriture en Go et son impact DevOps"
slug: "asdf-0-16-0-la-reecriture-en-go-et-son-impact-devops"
date: 2026-11-11T18:40:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "asdf passe au Go : gains de performance, compatibilité des plugins et ce que ça change pour les pipelines CI et le Platform Engineering."
tags:
  - go
  - devops
  - ci-cd
  - platform-engineering
  - automation
  - cli
series:
  - Veille techno
series_order: 153
showTableOfContents: true
---

## Introduction

`asdf` est un gestionnaire de versions d'outils largement utilisé dans les environnements de développement et les pipelines CI. Sa version 0.16.0 marque une étape importante : une réécriture complète en Go, avec des implications concrètes pour les équipes qui s'appuient dessus au quotidien.

## Ce que dit l'article

La réécriture en Go de `asdf` apporte plusieurs changements notables :

- **Performance** : les opérations courantes sont 2x à 7x plus rapides selon les cas.
- **Qualité** : des bugs présents dans la version Shell ont été corrigés.
- **Accessibilité** : la base de code en Go est plus lisible et plus facile à contribuer pour de nouveaux mainteneurs.
- **Compatibilité** : les plugins existants et les données des versions précédentes sont supportés, mais une lecture du guide de migration est recommandée car l'API a évolué.

La migration est documentée et conçue pour être progressive, sans rupture brutale.

## Avis

Dans une logique d'automatisation et de Platform Engineering, `asdf` fait partie de ces outils de socle dont on parle peu mais qui ont un impact réel : standardiser les versions d'outils entre les environnements locaux et les pipelines CI, c'est réduire une catégorie entière de problèmes — les "ça marche chez moi" et les dérives silencieuses de version en production.

Le choix de Go n'est pas surprenant. C'est le langage dominant de l'écosystème DevOps (`kubectl`, `terraform`, `gh`...) et il facilite la distribution sous forme de binaire unique, sans dépendance. Pour un outil de gestion d'environnement, c'est une décision cohérente.

Les gains de performance (jusqu'à 7x) peuvent sembler anecdotiques sur un poste local, mais dans un pipeline CI qui tourne des dizaines de fois par jour, ou lors de l'initialisation d'un environnement de développement conteneurisé, ça devient mesurable. Et une base de code plus maintenable, c'est un outil qui va continuer à évoluer — ce qui compte pour des équipes qui misent sur la durabilité de leur stack.

À surveiller si vous êtes sur `mise` ou `rtx` comme alternatives : la dynamique de contribution autour de `asdf` pourrait se relancer avec cette refonte.

## Source

https://stratus3d.com/blog/2025/02/03/asdf-has-been-rewritten-in-go/
