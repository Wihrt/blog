---
title: "PostgreSQL 19 : simplifier ses requêtes avec GROUP BY ALL"
slug: "postgresql-19-group-by-all"
date: 2025-10-23T09:00:03+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "GROUP BY ALL inclut automatiquement toutes les colonnes non agrégées, ce qui évite de les énumérer une à une dans la clause."
tags:
  - postgresql
  - database
  - open-source
series:
  - Veille techno
series_order: 21
showTableOfContents: true
---

## Introduction

Je suis ravi de partager avec vous une nouveauté de PostgreSQL 19 : la syntaxe **GROUP BY ALL**. Ce changement simplifie considérablement l’écriture des requêtes SQL, rendant les analyses de données plus accessibles pour tous.

## Résumé

La fonctionnalité **GROUP BY ALL** introduite dans PostgreSQL 19 permet d’inclure automatiquement toutes les colonnes non agrégées et sans fonction fenêtre dans la clause GROUP BY. Cette avancée, récemment intégrée dans le standard SQL, élimine le besoin de lister explicitement les colonnes de regroupement. Plutôt que d'écrire `GROUP BY col1, col2`, il suffit maintenant d'utiliser `GROUP BY ALL` et PostgreSQL déterminera automatiquement les colonnes à regrouper selon l’instruction SELECT.

## Utilité pros tech

Pour les développeurs et analystes, la simplification apportée par GROUP BY ALL représente un gain de temps et une réduction des erreurs potentielles dans les requêtes. Plus besoin de se souvenir de chaque colonne utilisée, ce qui optimise le flux de travail.

## Mon expérience

J'ai eu l'occasion de tester cette fonctionnalité dans un projet récent, et cela m’a permis d’accélérer le processus de développement. Moins de lignes à écrire, c’est plus de temps consacré à l’analyse des résultats.

## Conclusion

La nouvelle syntaxe GROUP BY ALL de PostgreSQL 19 est un ajout bienvenu, simplifiant le quotidien de tous ceux qui manipulent régulièrement des bases de données. Je vous invite à essayer cette fonctionnalité dans vos propres projets et à visiter l'article complet pour plus de détails : [lien de l'article](https://api.daily.dev/r/DLPc62ACh).
