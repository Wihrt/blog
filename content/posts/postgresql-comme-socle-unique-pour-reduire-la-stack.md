---
title: "PostgreSQL comme socle unique pour réduire la stack"
slug: "postgresql-comme-socle-unique-pour-reduire-la-stack"
date: 2026-11-11T18:44:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Cache, cron, vecteurs, GraphQL : ce que PostgreSQL peut absorber avant d'ajouter un nouveau service tiers."
tags:
  - postgresql
  - database
  - devops
  - platform-engineering
  - self-hosted
series:
  - Veille techno
series_order: 157
showTableOfContents: true
---

## Contexte

Les stacks modernes ont tendance à s'allonger : un service pour le cache, un autre pour les jobs planifiés, un autre pour la recherche vectorielle, encore un pour l'authentification. Chaque brique ajoutée a un coût réel — en intégration, en maintenance, en surface d'erreur. Cette vidéo pose une question simple : est-ce que PostgreSQL ne pourrait pas absorber une bonne partie de ces besoins ?

## Ce que couvre l'article

La vidéo passe en revue les capacités de PostgreSQL souvent ignorées ou sous-estimées :

- **Types de données avancés** : JSON, arrays, types composites
- **Extensions pour les cron jobs** : `pg_cron` pour planifier des tâches directement dans la base
- **Cache en mémoire** : via `pg_prewarm` et la gestion du buffer pool
- **Stockage vectoriel** : `pgvector` pour les cas d'usage IA/embeddings
- **GraphQL** : `pg_graphql` pour exposer un schéma GraphQL depuis les tables
- **Synchronisation temps réel** et **authentification** : via des extensions dédiées
- **Analytics** : agrégations, fenêtres, et extensions columnar pour les workloads analytiques

L'argument central : avant d'externaliser un besoin vers un service tiers, évaluer honnêtement ce que PostgreSQL peut faire.

## Point de vue

L'idée résonne directement avec une approche d'automatisation sobre : moins d'outils, moins de glue code, moins de points de défaillance. Chaque service externe qu'une équipe plateforme doit opérer ou intégrer représente de la charge cognitive et opérationnelle. Si PostgreSQL peut couvrir le besoin avec un niveau de fiabilité acceptable, c'est une option à peser sérieusement.

Cela ne veut pas dire tout concentrer dans la base par principe. `pgvector` ne remplacera pas Pinecone pour tous les cas d'usage. `pg_cron` a ses limites face à un orchestrateur dédié sur des workflows complexes. Mais dans beaucoup de projets, la stack est sur-dimensionnée par habitude ou par réflexe, pas par nécessité réelle.

Pour des équipes DevOps ou Platform Engineering, l'implication concrète est claire : moins de services à provisionner, monitorer, mettre à jour et sécuriser. Une base bien configurée et bien connue vaut souvent mieux qu'un ensemble hétérogène d'outils mal maîtrisés. Le bon outil, c'est celui qu'on sait opérer.

## Source

https://www.youtube.com/watch?v=3JW732GrMdg
