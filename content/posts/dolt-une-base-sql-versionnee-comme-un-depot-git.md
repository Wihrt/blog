---
title: "Dolt : une base SQL versionnée comme un dépôt Git"
slug: "dolt-une-base-sql-versionnee-comme-un-depot-git"
date: 2026-10-13T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Dolt combine compatibilité MySQL et primitives Git pour versionner schéma et données, utile en staging et CI/CD."
tags:
  - database
  - git
  - devops
  - gitops
  - automation
series:
  - Veille techno
series_order: 96
showTableOfContents: true
---

## Introduction

La gestion des changements de base de données reste l'un des points les plus délicats dans les pipelines CI/CD modernes. On version le code, les configurations, les infrastructures — mais les données elles-mêmes échappent souvent à cette discipline. Dolt propose une approche directe : une base SQL qui se comporte comme un repository Git.

## Ce que fait Dolt

Dolt est une base de données relationnelle **compatible MySQL** qui intègre nativement les primitives Git dans son moteur :

- `dolt commit`, `dolt branch`, `dolt merge`, `dolt push` fonctionnent comme leurs équivalents Git
- Une CLI puissante permet de gérer les changements de schéma et de données avec les mêmes réflexes qu'un repo de code
- **DoltHub** joue le rôle de GitHub pour les datasets : partage, collaboration, et même des bounties sur des jeux de données publics
- La compatibilité MySQL signifie que les outils existants (clients SQL, ORMs, connecteurs) fonctionnent sans réécriture

L'historique complet des modifications — schéma et données — est traçable, diffable et réversible.

## Avis

L'intérêt de Dolt se lit d'abord sous l'angle de l'automatisation. Dans un workflow GitOps, la cohérence entre l'état du code et l'état des données est un problème réel, souvent résolu par des scripts fragiles ou des outils de migration peu intégrés (Flyway, Liquibase) qui versionnent les *opérations* mais pas l'état réel des données.

Dolt inverse cette logique : l'état des données devient lui-même versionnable et auditable. Pour des **environnements de staging**, de la **gestion de données de référence**, ou des pipelines de test qui nécessitent des snapshots reproductibles, c'est une brique concrète.

La compatibilité MySQL réduit significativement la friction à l'adoption — pas besoin de tout réécrire. Cela dit, la prudence s'impose avant tout usage en production critique : les compromis sur les performances et la maturité du moteur méritent une évaluation sérieuse en conditions réelles.

L'outil ne révolutionne pas tout, mais il adresse un angle mort persistant dans les pratiques DevOps actuelles.

## Source

https://cult.honeypot.io/reads/dolt-a-sql-database-that-works-like-git
