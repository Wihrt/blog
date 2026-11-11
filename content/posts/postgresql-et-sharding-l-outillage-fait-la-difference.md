---
title: "PostgreSQL et sharding : l'outillage fait la différence"
slug: "postgresql-et-sharding-l-outillage-fait-la-difference"
date: 2026-11-11T18:48:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Le sharding rend PostgreSQL scalable, mais sans automatisation l'effort d'ingénierie devient vite un fardeau opérationnel."
tags:
  - postgresql
  - database
  - devops
  - platform-engineering
  - automation
series:
  - Veille techno
series_order: 161
showTableOfContents: true
---

## Introduction

PostgreSQL reste une référence pour les bases de données relationnelles, mais sa scalabilité horizontale en écriture est souvent perçue comme un point faible face à des alternatives NoSQL. L'article de PgDog démontre que c'est techniquement faisable — à condition d'accepter la complexité que ça implique.

## Ce que dit l'article

L'approche décrite repose sur le **sharding** : distribuer la charge d'écriture sur plusieurs instances PostgreSQL indépendantes. Les points clés abordés sont :

- La mise en place de multiples replicas pour la haute disponibilité.
- La gestion de l'**intégrité des données** pendant la réplication entre shards.
- La configuration de la couche applicative pour router les requêtes vers le bon shard.
- Le volume d'ingénierie nécessaire pour rendre l'ensemble cohérent et opérable.

L'article est honnête sur l'effort : ce n'est pas une solution clé en main, c'est un chantier d'ingénierie sérieux.

## Analyse

Le sharding PostgreSQL n'est pas une nouveauté. Ce qui l'est davantage, c'est la recherche d'outils capables d'**automatiser** les étapes les plus coûteuses de cette architecture.

Sans outillage adapté, la complexité opérationnelle s'accumule rapidement : scripts fragiles, dépendance à l'expertise individuelle, procédures manuelles non reproductibles. Ce type de dette technique est particulièrement dangereux dans des environnements qui évoluent vite.

Pour des équipes Platform ou DevOps, la question n'est pas seulement « est-ce que PostgreSQL peut scaler ? » mais « est-ce qu'on peut opérer ce système sans que ça devienne un fardeau ? ». La réponse passe par :

- Un **provisioning automatisé** des shards.
- Un **routage transparent** des requêtes au niveau middleware ou proxy.
- Des mécanismes de vérification de cohérence intégrés, pas ajoutés après coup.

L'approche outils-first, c'est ce qui permet de garder une architecture ambitieuse sous contrôle sur le long terme, et de ne pas dépendre uniquement des personnes qui l'ont construite.

## Source

https://pgdog.dev/blog/you-can-make-postgres-scale
