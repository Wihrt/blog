---
title: "Kener : pages de statut open-source auto-hébergées"
slug: "kener-pages-de-statut-open-source-auto-hebergees"
date: 2026-11-11T18:36:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Kener génère des pages de statut Docker-ready, open-source, pensées pour s'intégrer aux pipelines d'alerting et CI/CD."
tags:
  - self-hosted
  - open-source
  - docker
  - platform-engineering
  - monitoring
series:
  - Veille techno
series_order: 149
showTableOfContents: true
---

## Contexte

Les pages de statut sont souvent traitées comme un accessoire. Pourtant, en production, c'est l'un des premiers points de contact entre une équipe technique et ses utilisateurs lors d'un incident. Kener propose une approche simple : open-source, auto-hébergeable, et prêt à tourner dans un conteneur Docker.

## Ce que fait Kener

Kener est un outil de génération de pages de statut lancé en janvier 2024. Ses points clés :

- **Auto-hébergé** : pas de dépendance à un SaaS tiers, vous gardez le contrôle des données.
- **Docker-ready** : déploiement rapide dans un environnement conteneurisé existant.
- **Open-source** : code disponible sur GitHub, maintenable et adaptable selon les besoins.
- **Interface soignée** : pensé pour être lisible par des utilisateurs non techniques.

L'outil vise à remplacer des solutions bricolées ou des abonnements à des plateformes comme Statuspage.io, avec un coût d'infrastructure réduit au minimum.

## Avis

L'intérêt de Kener se lit surtout à travers le prisme de l'automatisation. Une page de statut qui se met à jour manuellement pendant un incident, c'est une charge cognitive supplémentaire au pire moment. L'enjeu réel, c'est l'intégration : est-ce que l'outil expose une API suffisamment simple pour être piloté depuis un pipeline CI/CD, un système d'alerting comme Alertmanager, ou un workflow d'incident management ?

Si c'est le cas, Kener devient un composant légitime dans une stack Platform Engineering : déployé une fois, alimenté automatiquement, et visible sans nécessiter d'accès aux outils internes de monitoring. C'est exactement ce type de découplage qui réduit la friction lors des incidents.

Le fait qu'il soit open-source et Docker-ready enlève les obstacles habituels à l'adoption : pas de contrat, pas de lock-in, et une image à ajouter dans un `docker-compose.yml` ou un manifeste Kubernetes. Pour des équipes qui cherchent à consolider leur outillage sans augmenter leur surface de dépendance externe, ça mérite au moins une évaluation.

## Source

https://www.producthunt.com/posts/kener-2
