---
title: "Runloom : concurrence façon Go en Python avec GIL désactivé"
slug: "runloom-concurrence-facon-go-en-python-avec-gil-desactive"
date: 2026-10-19T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Runloom apporte des coroutines stackful et un scheduler M:N à Python 3.13t, sans réécrire le code en async/await."
tags:
  - python
  - automation
  - platform-engineering
  - open-source
series:
  - Veille techno
series_order: 100
showTableOfContents: true
---

## Introduction

Runloom est une bibliothèque Python expérimentale qui cible Python 3.13t+ avec le GIL désactivé. Elle apporte un modèle de concurrence inspiré des goroutines Go directement dans l'écosystème Python — sans `async/await`, sans réécriture du code existant.

## Ce que fait Runloom

Les points clés à retenir :

- **Coroutines stackful** : contrairement aux coroutines Python classiques, chaque fiber conserve sa propre stack, ce qui permet d'utiliser du code bloquant standard.
- **Scheduler M:N work-stealing en C** : les fibers sont multiplexées sur les threads OS disponibles avec un context switch écrit en assemblage.
- **Netpoll intégré** : les I/O réseau sont gérées de façon non-bloquante de manière transparente.
- **Benchmarks solides** : 2,29M spawns/s (vs 2,10M pour Go en C pur), ~596k req/s (vs 603k pour Go). La parité est quasi atteinte.
- **Monkey-patch API** : rend le code `stdlib` bloquant coopératif sans modifier une ligne de code existant.
- **Bridge asyncio** : migration progressive depuis du code `async/await`.

Le principal compromis : une fiber suspendue consomme ~3,3× plus de RAM qu'une goroutine Go, à cause du frame d'évaluation CPython.

## Avis

L'automatisation reste le cas d'usage central de Python dans beaucoup de stacks DevOps et Platform Engineering. Et le problème récurrent, c'est la concurrence : soit on reste sur du code séquentiel simple mais lent, soit on bascule sur `asyncio` avec la friction que ça implique — réécriture des appels, librairies compatibles uniquement, complexité de debug accrue.

Runloom adresse exactement ce point de friction. Le monkey-patch API est la fonctionnalité la plus concrète pour des équipes existantes : du code de scripts d'automatisation déjà en prod peut potentiellement gagner en concurrence sans toucher à la logique métier.

Le surcoût mémoire (~3,3×) est à surveiller sérieusement si on envisage des workloads à haute concurrence — des milliers de fibers simultanées dans un contexte containerisé, ça peut rapidement poser des questions de sizing. Ce n'est pas rédhibitoire, mais c'est un paramètre à intégrer dès la conception.

L'outil est clairement expérimental et dépend de Python 3.13t+ avec free-threaded mode, ce qui n'est pas encore la norme en prod. Mais la direction est intéressante : si la maturité suit, ça pourrait réellement simplifier la façon dont on écrit des outils d'automatisation concurrents en Python.

## Source

https://github.com/robertsdotpm/runloom
