---
title: "Go internals : slices, maps et channels en mémoire"
slug: "go-internals-slices-maps-et-channels-en-memoire"
date: 2026-11-11T19:16:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Plongée dans les structures internes de Go : header de slice, Swiss Tables pour les maps, et mécanique des channels avec hchan."
tags:
  - go
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 189
showTableOfContents: true
---

## Introduction

Go est devenu le langage de référence pour l'outillage d'infrastructure : CLI, controllers Kubernetes, operators, outils d'automatisation. Pourtant, peu de développeurs prennent le temps de comprendre ce qui se passe réellement en mémoire quand ils manipulent des slices, des maps ou des channels. Cet article s'y attaque frontalement.

## Ce que couvre l'article

L'auteur détaille les structures internes des trois types built-in les plus courants en Go :

- **Slices** : un header de 24 bytes (pointeur vers le backing array, `len`, `cap`) alloué sur la heap. La stratégie de croissance double la capacité jusqu'à 256 éléments, puis passe à un facteur 1.25x.
- **Maps** : depuis Go 1.24, l'implémentation repose sur les **Swiss Tables**. L'architecture est une hiérarchie à trois niveaux — header, directory de tables, groupes de 8 slots avec un control word de 8 bytes. Les lookups utilisent un preview H2 du hash pour un matching rapide style SIMD. La croissance est locale : seule la table en overflow est rehashée.
- **Channels** : struct `hchan` avec un buffer circulaire et deux queues doublement chaînées de `sudog` pour les goroutines en attente. Quand un sender rencontre un receiver déjà en attente, la valeur est copiée directement entre goroutines, sans passer par le buffer.

L'article couvre aussi les pièges classiques : le partage de backing array entre sub-slices, et la distinction tombstone/empty lors de la suppression dans une map.

## Avis

Quand on fait du platform engineering, on produit des outils internes en Go au quotidien. Des operators, des reconcilers, des pipelines d'automatisation. Ce code tourne en continu, souvent sans supervision humaine directe. La robustesse n'est pas un luxe, c'est une exigence de base.

Comprendre comment une slice grandit ou comment une map se réorganise en mémoire, ça permet d'écrire du code qui ne réserve pas de surprises. Le piège du backing array partagé sur un sub-slice, par exemple, c'est un classique qui peut provoquer des corruptions de données silencieuses dans un controller qui tourne depuis des semaines. Même chose pour les maps : ne pas comprendre la mécanique des tombstones, c'est risquer des fuites mémoire lentes sur des workloads long-running.

Plus on pousse l'automatisation, plus la qualité et la prévisibilité du code Go qu'on écrit deviennent critiques. Ce type de deep dive est un investissement direct dans la fiabilité de l'outillage qu'on met en production.

[Article source](https://internals-for-interns.com/posts/go-runtime-slices-maps-channels)
