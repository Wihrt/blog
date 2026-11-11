---
title: "L'IA génère du code, elle ne conçoit pas de logiciel"
slug: "l-ia-genere-du-code-elle-ne-concoit-pas-de-logiciel"
date: 2026-11-11T18:54:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Pourquoi confondre génération de code et conception logicielle est risqué pour les équipes DevOps et Platform Engineering."
tags:
  - ai
  - devops
  - platform-engineering
series:
  - Veille techno
series_order: 167
showTableOfContents: true
---

## Introduction

Le discours ambiant sur l'IA qui remplacerait les développeurs revient régulièrement. Derrière ce raccourci, il y a une confusion fondamentale entre **écrire du code** et **construire un système logiciel**. Une distinction qui a des implications directes pour les équipes DevOps et Platform Engineering.

## Ce que dit l'article

Swizec réagit à un essai sur "l'industrialisation de l'IT" qui imagine un futur où le design logiciel serait optimisé pour être consommé par l'IA. L'auteur pointe un problème de fond : la plupart des concepts présentés comme des innovations — **domain-oriented design**, **stream-aligned teams**, séparation claire des responsabilités — sont des pratiques établies dans l'industrie depuis des années.

Le constat central est net : l'IA peut générer du code, parfois efficacement. Mais elle ne sait pas **concevoir** un logiciel. La valeur d'un ingénieur ne réside pas dans la production de lignes de code, mais dans sa capacité à créer des **systèmes fonctionnels** — avec tout ce que ça implique en termes de modélisation, de compromis d'architecture, de résilience et de maintenabilité.

## Mon avis

En tant qu'ingénieur plateforme, la question de l'IA s'inscrit dans une logique plus large : **trouver des outils pour automatiser ce qui peut l'être**. C'est exactement ce qu'on fait depuis des années avec le CI/CD, l'Infrastructure as Code, le policy-as-code, les tests automatisés. L'IA générative est un levier supplémentaire dans cette chaîne.

Mais il faut être lucide sur ce qu'elle automatise réellement. Générer un boilerplate, scaffolder un service, écrire des tests unitaires basiques — oui, c'est du gain de temps concret. Arbitrer entre un déploiement blue-green et un canary selon le profil de risque d'un service, dimensionner une architecture event-driven pour un domaine métier complexe, gérer la dette technique d'un système en production depuis 5 ans — non, on n'y est pas.

Le risque pour les équipes, c'est de **surinvestir dans l'IA comme solution magique** au lieu de consolider les fondamentaux : un bon domain modeling, des interfaces claires entre équipes, une plateforme interne qui réduit la charge cognitive des développeurs. L'IA amplifie ce qui existe déjà. Si les bases sont fragiles, elle amplifiera aussi la fragilité.

L'enjeu n'est pas pour ou contre l'IA. C'est de **l'intégrer au bon endroit** dans la chaîne de valeur, sans confondre accélération de tâches et remplacement de compétences.

[Source : Swizec — Re: The industrialization of IT](https://swizec.com/blog/re-the-industrialization-of-it/)
