---
title: "Limbo : SQLite réécrit en Rust par Turso"
slug: "limbo-sqlite-reecrit-en-rust-par-turso"
date: 2026-11-11T18:27:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Turso réécrit SQLite en Rust avec Limbo : asynchrone natif, sécurité mémoire et tests par simulation déterministe."
tags:
  - rust
  - database
  - open-source
  - automation
series:
  - Veille techno
series_order: 140
showTableOfContents: true
---

## Introduction

SQLite est partout — dans les outils CLI, les pipelines d'automatisation, les agents locaux, les applications embarquées. Turso vient d'annoncer Limbo, une réécriture complète en Rust, et les choix techniques méritent qu'on s'y arrête au-delà du simple effet d'annonce.

## Ce que dit l'article

Limbo est une réécriture intégrale de SQLite en Rust, maintenant une compatibilité totale avec le format de fichier `.sqlite` et le dialecte SQL existant. Les points clés du projet :

- **Sécurité mémoire** : profiter des garanties de Rust pour éliminer une catégorie entière de bugs liés à la gestion manuelle de la mémoire.
- **Asynchrone natif** : contrairement à SQLite qui est synchrone par conception, Limbo intègre l'asynchrone dès la base, ce qui facilite l'intégration dans des runtimes modernes.
- **Tests par simulation déterministe** : une approche de test qui rejoue les scénarios de manière reproductible pour valider le comportement sous conditions variées.
- **Performances** : les premiers benchmarks montrent des résultats prometteurs, sans que cela soit encore consolidé à grande échelle.
- **Open source et communauté active** : le projet grandit avec des contributions externes.

## Avis

L'angle qui m'intéresse ici n'est pas "Rust est mieux" — c'est une conclusion trop rapide. Ce qui compte, c'est ce que les choix d'architecture apportent concrètement.

L'**asynchrone by design** est un vrai point de différenciation. SQLite en contexte synchrone peut devenir un goulot dans des outils qui orchestrent plusieurs opérations en parallèle. Une version async-native ouvre des usages plus propres dans des pipelines d'automatisation ou des agents qui font du stockage local.

La **simulation déterministe** est peut-être encore plus intéressante du point de vue plateforme. Pouvoir tester le comportement d'une base de données locale de manière reproductible, c'est réduire la surface d'incertitude dans les tests d'intégration. Pour des équipes qui construisent des outils internes ou des composants d'infrastructure légère, c'est un critère de fiabilité non négligeable.

Cela dit, Limbo est encore jeune. La compatibilité affichée est prometteuse, mais une migration en production demande du recul. À surveiller sur la durée, pas à adopter à la légère maintenant.

## Source

https://turso.tech/blog/introducing-limbo-a-complete-rewrite-of-sqlite-in-rust
