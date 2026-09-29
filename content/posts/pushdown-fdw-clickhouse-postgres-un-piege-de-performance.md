---
title: "Pushdown FDW ClickHouse-Postgres : un piège de performance"
slug: "pushdown-fdw-clickhouse-postgres-un-piege-de-performance"
date: 2026-09-29T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Comment la négociation de pushdown entre ClickHouse et Postgres peut faire exploser le trafic réseau silencieusement."
tags:
  - postgresql
  - database
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 85
showTableOfContents: true
---

## Introduction

Quand on connecte ClickHouse à PostgreSQL via un Foreign Data Wrapper, on s'attend à ce que le gros du travail analytique soit exécuté côté ClickHouse. En pratique, le mécanisme de pushdown est bien plus subtil — et un seul détail peut ruiner silencieusement les performances.

## Ce que dit l'article

ClickHouse a publié un walkthrough complet du fonctionnement interne de `pg_clickhouse` FDW, en suivant une seule requête analytique réaliste à travers **7 étapes incrémentales** :

- **Scan et WHERE** : le pushdown de base, filtres simples envoyés à ClickHouse.
- **JOIN** : conditions de jointure et leur traductibilité.
- **GROUP BY et agrégats** : où les choses se compliquent.
- **Percentiles, opérateurs JSON, window functions** : chaque expression non supportée bloque le plan groupé entier.

Le point central : **le pushdown est tout-ou-rien au niveau upper-relation**. Si une seule sous-expression n'est pas traduisible vers ClickHouse, PostgreSQL rapatrie l'intégralité des données brutes pour les traiter localement. On passe de 100 lignes résultantes à des millions de lignes sur le réseau.

L'article explique aussi pourquoi certains pushdowns sont **révoqués** quand la sémantique ne correspond pas entre les deux moteurs, et détaille l'architecture de **callbacks FDW** (`GetForeignRelSize`, `GetForeignPaths`, `GetForeignUpperPaths`…) qui rend cette négociation possible.

## Avis

Ce type de documentation est précieux pour quiconque automatise des pipelines data au-dessus de PostgreSQL. On a souvent tendance à traiter les FDW comme des connecteurs transparents : on branche, la requête retourne les bons résultats, on passe à la suite. Le problème, c'est que "correct" et "performant" sont deux choses très différentes ici.

Pour des équipes plateforme qui exposent des abstractions data à d'autres équipes, comprendre cette mécanique est essentiel. Un utilisateur qui ajoute un `percentile_cont` ou un opérateur `->>`  dans sa requête peut, sans le savoir, multiplier le trafic réseau par un facteur énorme. Si on veut construire des garde-fous ou des checks automatisés autour de ces patterns, il faut d'abord comprendre la grille de décision du planificateur.

L'architecture de callbacks décrite dans l'article est aussi réutilisable comme modèle mental pour évaluer d'autres FDW — `mysql_fdw`, `oracle_fdw`, `multicorn`, etc. La question est toujours la même : qu'est-ce qui est réellement pushé, et qu'est-ce qui ne l'est pas ?

---

**Source** : [https://clickhouse.com/blog/postgres-fdw-pushdown-negotiation](https://clickhouse.com/blog/postgres-fdw-pushdown-negotiation)
