---
title: "pg_duckdb 1.0 : l'analytique DuckDB dans PostgreSQL"
slug: "pg-duckdb-1-0-analytique-postgresql"
date: 2025-10-20T09:00:10+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Interroger ses tables PostgreSQL avec le moteur DuckDB, et joindre les données locales à des fichiers Parquet, CSV ou JSON distants."
tags:
  - postgresql
  - database
  - open-source
  - storage
series:
  - Veille techno
series_order: 16
showTableOfContents: true
---

## Introduction

Je suis ravi de partager que Pg_duckdb version 1.0 est enfin là. Cette version représente une avancée remarquable en intégrant le moteur analytique vectorisé de DuckDB directement dans PostgreSQL, permettant ainsi des requêtes analytiques bien plus rapides sans avoir besoin de recourir à des entrepôts de données distincts ou à des processus ETL complexes.

## Résumé

Avec cette extension, on peut désormais interroger les tables PostgreSQL tout en bénéficiant des avantages de performance de DuckDB. Elle offre la possibilité d'accéder à des fichiers de lacs de données externes, tels que Parquet, CSV et JSON, et de lier les données locales de PostgreSQL avec des fichiers de stockage cloud distants dans des requêtes uniques.

## Utilité pros tech

Pour les professionnels de la technologie, cette intégration se traduit par un gain de performance allant jusqu'à 4 fois plus rapide avec des index et des améliorations significatives pour des requêtes qui, auparavant, échouaient. L'extension facilite également l'intégration avec MotherDuck pour un scalage serverless des analyses.

## Mon expérience

En tant qu'utilisateur régulier de PostgreSQL, cette mise à jour a transformé ma manière d’aborder les requêtes analytiques. Fini le temps perdu à attendre que les analyses complexes se terminent.

## Conclusion

La version 1.0 de Pg_duckdb est sans doute l'une des sorties les plus attendues pour ceux d'entre nous qui utilisent PostgreSQL au quotidien. L'intégration avec DuckDB promet un gain d'efficacité considérable et ouvre de nouvelles possibilités pour les analyses de données. Pour en savoir plus, consultez cet article : [Lire l'article complet](https://api.daily.dev/r/OoMjdpjvJ).
