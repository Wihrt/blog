---
title: "Turso : SQLite réécrit en Rust pour le Platform Engineering"
slug: "turso-sqlite-reecrit-en-rust-pour-le-platform-engineering"
date: 2026-11-11T19:12:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Turso réécrit SQLite en Rust avec I/O async, MVCC et CDC natif, réduisant la complexité des architectures edge et IA."
tags:
  - rust
  - database
  - platform-engineering
  - open-source
  - devops
series:
  - Veille techno
series_order: 185
showTableOfContents: true
---

## Introduction

SQLite est partout. C'est probablement le moteur de base de données le plus déployé de la planète. Mais son architecture — single-writer, I/O synchrone, extensibilité limitée — pose des problèmes concrets dès qu'on sort du cas d'usage mono-processus en lecture. Turso propose une réécriture complète en Rust pour lever ces contraintes.

## Ce que propose Turso

L'article publié sur The New Stack détaille les motivations et les choix techniques du projet :

- **I/O asynchrone** pour ne plus bloquer sur les opérations disque
- **Écritures concurrentes via MVCC**, là où SQLite impose un verrou global en écriture
- **Chiffrement natif** intégré au moteur
- **Recherche vectorielle** pour les cas d'usage IA/ML
- **CDC (Change Data Capture)** natif, permettant de streamer les changements sans outillage externe
- **Vues matérialisées live** pour le streaming analytics

Le tout reste compatible avec l'écosystème SQLite. Le projet est open source, porté par plus de 150 contributeurs.

## Analyse : ce que ça implique côté plateforme

Quand on construit des plateformes internes ou qu'on automatise des pipelines de données, le choix du moteur embedded a des conséquences directes sur la complexité de l'architecture globale.

SQLite classique force souvent à ajouter des couches : un broker pour le CDC, un proxy pour gérer la concurrence, un système externe pour le chiffrement at-rest. Chaque couche ajoutée, c'est du middleware à déployer, monitorer, maintenir.

Turso intègre ces primitives directement dans le moteur. Pour du **edge computing**, où chaque dépendance supplémentaire coûte cher en complexité opérationnelle, c'est un vrai gain. Pour des **agents IA** qui écrivent en parallèle dans une base locale, le MVCC natif évite des contorsions. Et le CDC intégré ouvre la porte à des architectures event-driven sans middleware dédié.

Le choix de Rust n'est pas anodin non plus : sécurité mémoire, performances, et un écosystème qui attire des contributeurs compétents.

Ce n'est pas un remplacement universel de PostgreSQL ou d'une base distribuée. Mais dans les cas où SQLite était déjà le bon choix — et qu'on se heurtait à ses limites — Turso mérite clairement d'être évalué.

🔗 [Article source — The New Stack](https://thenewstack.io/why-we-created-turso-a-rust-based-rewrite-of-sqlite/)
