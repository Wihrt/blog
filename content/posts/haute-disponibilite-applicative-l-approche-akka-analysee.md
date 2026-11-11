---
title: "Haute disponibilité applicative : l'approche Akka analysée"
slug: "haute-disponibilite-applicative-l-approche-akka-analysee"
date: 2026-11-11T18:39:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Akka détaille comment intégrer la résilience au niveau applicatif pour viser 99,9999% de disponibilité multi-région."
tags:
  - platform-engineering
  - devops
  - automation
  - cloud
series:
  - Veille techno
series_order: 152
showTableOfContents: true
---

## Contexte

Atteindre 99.9999% de disponibilité — soit moins de 32 secondes de downtime annuel — n'est plus réservé aux GAFAM. Des secteurs comme la finance, la santé ou les infrastructures critiques en font une exigence contractuelle ou réglementaire. La question n'est plus *pourquoi*, mais *comment* sans exploser la complexité opérationnelle.

## Ce que propose l'article

Akka publie un article détaillant leur approche pour construire et opérer des applications à très haute disponibilité. Les points clés :

- **Résilience embarquée au niveau applicatif** : plutôt que de tout faire reposer sur l'infra (load balancers, failover DNS, etc.), la logique de tolérance aux pannes est intégrée dans le modèle de l'application.
- **Architecture multi-région** : les applications sont conçues pour continuer à fonctionner même si une région entière tombe, sans intervention manuelle.
- **Réduction des coûts** : l'argument avancé est qu'une approche applicative bien pensée peut être moins coûteuse qu'une infrastructure redondante classique.
- **Conformité réglementaire** : le sujet de l'uptime est de plus en plus présent dans les audits et les SLA imposés par certaines régulations sectorielles.

## Avis

L'angle qui retient l'attention ici, c'est celui de l'automatisation de la résilience. En Platform Engineering, on passe beaucoup de temps à construire des runbooks, des alertes, des procédures de bascule — autant de processus qui restent partiellement manuels et donc sources de latence en cas d'incident.

Un outil qui permet d'encapsuler cette logique directement dans l'application, avec des comportements de failover automatiques et déterministes, va dans la bonne direction. Moins de dépendance à l'humain en prod, c'est moins de MTTR et moins de risque d'erreur sous pression.

Cela dit, il faut rester lucide sur le compromis : ajouter Akka dans la stack, c'est adopter un modèle de programmation spécifique (le modèle acteur), ce qui implique une courbe d'apprentissage et de la compétence à maintenir dans l'équipe. La résilience ne s'obtient pas gratuitement — elle se déplace. L'objectif est de la rendre plus prévisible et plus automatisée, pas de la faire disparaître.

Pour des équipes qui gèrent des workloads critiques multi-régions, la piste mérite d'être évaluée sérieusement, en particulier si l'infra actuelle repose encore trop sur des interventions manuelles pour les basculements.

## Source

https://akka.io/blog/build-and-run-apps-with-6-9s-availability
