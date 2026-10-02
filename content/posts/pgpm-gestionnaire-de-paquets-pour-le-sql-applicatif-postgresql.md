---
title: "pgpm : gestionnaire de paquets pour le SQL applicatif PostgreSQL"
slug: "pgpm-gestionnaire-de-paquets-pour-le-sql-applicatif-postgresql"
date: 2026-10-02T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "pgpm modularise la logique SQL de PostgreSQL : versionnement, dépendances et déploiement reproductible sans superuser."
tags:
  - postgresql
  - database
  - devops
  - ci-cd
  - open-source
series:
  - Veille techno
series_order: 88
showTableOfContents: true
---

## Introduction

La gestion de la logique applicative en base de données reste un point de friction dans beaucoup de pipelines DevOps. Entre les scripts de migration séquentiels et les dépendances implicites entre objets SQL, la reproductibilité et la modularité sont rarement au rendez-vous. `pgpm` propose une approche différente.

## Ce que fait pgpm

`pgpm` est un package manager pour PostgreSQL qui cible la **logique applicative** — schemas, tables, fonctions, policies, triggers — et non les extensions système. Quelques points clés :

- **Pur SQL, sans compilation** : pas besoin d'accès superuser ni de toolchain C. Ça fonctionne directement au niveau applicatif.
- **Modules versionnés** avec gestion explicite des dépendances et résolution automatique.
- **Ordre de déploiement déterministe** : la composition est récursive, les dépendances sont résolues proprement.
- **Support du TDD** avec des bases éphémères dédiées aux tests.
- **Intégration CI/CD** native, pensée dès le départ.
- **Inspiré de Sqitch**, mais avec une couche de packaging modulaire et de composition qui va au-delà du simple suivi de changements.

## Avis

Dans une chaîne d'automatisation, le code SQL applicatif est souvent le maillon faible. On versionne le code applicatif, on package les images, on gère les dépendances infra as code — mais côté base, on empile des fichiers de migration numérotés avec des dépendances documentées nulle part.

`pgpm` attaque ce problème avec les bons principes : **modularité, versionnement, résolution de dépendances, reproductibilité**. Le choix de rester au niveau applicatif est particulièrement pertinent pour les environnements cloud managés (RDS, Cloud SQL, etc.) où l'accès superuser n'existe pas ou est limité.

Le projet est encore jeune, et il faudra observer comment il se comporte sur des projets avec des dizaines de schemas interdépendants et des équipes multiples. La question de l'écosystème — combien de packages réutilisables émergeront — sera aussi déterminante. Mais l'approche est saine et répond à un vrai besoin d'outillage dans la gestion du cycle de vie des bases PostgreSQL.

À suivre de près pour quiconque cherche à industrialiser la gestion du SQL dans ses pipelines.

**Source** : [Introducing pgpm — a package manager for modular PostgreSQL](https://www.postgresql.org/about/news/introducing-pgpm-a-package-manager-for-modular-postgresql-3196/)
