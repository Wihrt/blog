---
title: "Crossplane v2 en preview : compositions simplifiées"
slug: "crossplane-v2-en-preview-compositions-simplifiees"
date: 2026-11-11T18:49:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Aperçu de Crossplane v2 : schémas de composition allégés, ressources namespace-scoped et nettoyage de l'API."
tags:
  - kubernetes
  - gitops
  - platform-engineering
  - cloud
  - automation
series:
  - Veille techno
series_order: 162
showTableOfContents: true
---

## Contexte

Crossplane s'est imposé comme l'un des outils de référence pour le provisioning d'infrastructure depuis Kubernetes. La v2, actuellement en phase de preview, marque une évolution significative dans sa maturité et son ergonomie.

## Ce que la v2 apporte

Plusieurs changements concrets sont au programme :

- **Schémas de composition simplifiés** : moins de verbosité pour définir ses abstractions.
- **Ressources scopées au namespace** : plus de flexibilité dans l'organisation multi-tenant.
- **Nouvelles versions d'API** : alignement et modernisation des contrats.
- **Suppression des fonctionnalités dépréciées** : la surface d'API est nettoyée, ce qui réduit la dette technique implicite.
- **Composition directe de ressources** : il n'est plus nécessaire d'envelopper les ressources dans des managed resources, ce qui simplifie les compositions existantes.

La stabilité de la preview laisse penser qu'une release générale est imminente.

## Pourquoi c'est pertinent pour les équipes Platform Engineering

L'automatisation de l'infrastructure reste un enjeu central. Crossplane répond à une problématique précise : offrir une interface Kubernetes-native pour provisionner et gérer des ressources cloud, sans multiplier les outils en dehors du cluster.

La v2 va dans le sens d'une réduction de la friction opérationnelle. Simplifier les schémas de composition, c'est directement alléger la charge des équipes qui maintiennent ces abstractions. Moins de boilerplate, moins de cas limites à contourner. La suppression des dépréciations, souvent repoussée dans les projets open source, est un signal positif sur la gouvernance du projet.

Pour les équipes qui évaluent ou utilisent déjà Crossplane, tester la v2 en preview sur un environnement non-critique est une démarche raisonnable avant la stable. La direction prise confirme l'intérêt de l'outil pour qui cherche à centraliser le provisioning cloud dans une logique GitOps.

## Source

https://www.youtube.com/watch?v=jw8mMslpqOI
