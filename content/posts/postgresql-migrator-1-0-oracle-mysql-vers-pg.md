---
title: "PostgreSQL Migrator 1.0 : Oracle/MySQL vers PG"
slug: "postgresql-migrator-1-0-oracle-mysql-vers-pg"
date: 2026-11-25T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Dalibo sort PostgreSQL Migrator 1.0, outil open-source pour migrer Oracle et MySQL vers PostgreSQL."
tags:
  - postgresql
  - database
  - open-source
  - automation
  - devops
series:
  - Veille techno
series_order: 197
showTableOfContents: true
---

## Un nouvel outil pour un vieux problème

Migrer une base Oracle ou MySQL vers PostgreSQL reste un chantier lourd, souvent traité à coups de scripts maison et d'audits manuels interminables. Dalibo vient de publier la version stable 1.0 de PostgreSQL Migrator, un outil open-source qui vise justement à outiller ce processus de bout en bout.

## Ce que propose l'outil

PostgreSQL Migrator est distribué sous forme de binaire Go unique, sans dépendance runtime. Il embarque plusieurs briques :

- inspection offline des catalogues sources,
- scoring de complexité pour estimer l'effort avant de se lancer,
- une UI web interactive pour piloter la migration,
- conversion de schéma et de données,
- transpilation SQL/PL-SQL via un outil compagnon, transqlate,
- copie de données en streaming à haut débit.

Côté compatibilité, il gère Oracle 11g à 26ai et MySQL 8.4+/MariaDB 10+ comme sources, avec PostgreSQL 16 à 19 comme cibles. La 1.0 couvre l'inspection complète des catalogues, mais la conversion active se limite pour l'instant aux rôles, schémas, séquences, tables, colonnes virtuelles, contraintes et index. Les vues et objets procéduraux (packages, triggers, procédures stockées) sont annoncés pour une prochaine version. Le projet a mis un an en beta et release candidates avant d'atteindre cette stabilité, et Dalibo s'engage sur la compatibilité de configuration, CLI et projet sur toute la branche 1.x.

## Pourquoi ça compte pour les équipes plateforme

Ce type d'outil s'inscrit dans une logique claire : automatiser ce qui est aujourd'hui artisanal. Le scoring de complexité en amont permet de chiffrer un projet de migration avant de s'engager, ce qui manque cruellement dans la plupart des audits actuels. L'UI web facilite aussi la collaboration entre DBA et développeurs sur un même périmètre.

La limite actuelle sur les objets procéduraux reste le vrai test : c'est souvent là que se cachent les dépendances les plus complexes dans les bases Oracle historiques. À suivre sur les prochaines releases, mais la base technique et l'engagement de compatibilité posent de bonnes fondations pour l'intégrer dans une stratégie de migration outillée.

Source : https://www.postgresql.org/about/news/postgresql-migrator-10-first-stable-release-3377
