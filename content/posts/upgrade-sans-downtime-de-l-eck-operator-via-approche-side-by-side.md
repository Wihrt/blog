---
title: "Upgrade sans downtime de l'ECK Operator via approche side-by-side"
slug: "upgrade-sans-downtime-de-l-eck-operator-via-approche-side-by-side"
date: 2026-11-11T19:00:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Mercari détaille une méthode d'upgrade d'opérateur Kubernetes basée sur la coexistence de deux versions, appliquée à ECK."
tags:
  - kubernetes
  - platform-engineering
  - devops
  - automation
series:
  - Veille techno
series_order: 173
showTableOfContents: true
---

## Introduction

Mettre à jour un opérateur Kubernetes qui pilote des clusters Elasticsearch en production, c'est le type d'opération qui génère du stress à tous les étages. L'équipe Search Infrastructure de Mercari propose une approche side-by-side qui mérite qu'on la regarde de près.

## Ce que propose l'article

Abhishek Munagekar détaille une méthode d'upgrade de l'ECK Operator basée sur la **coexistence de deux versions** de l'opérateur sur le même cluster Kubernetes. Les points clés :

- **Modification de l'opérateur** pour supporter le fonctionnement en dual version, chaque instance ne gérant que les ressources qui lui sont assignées.
- **Gestion des CRDs** : les Custom Resource Definitions doivent rester compatibles entre les deux versions, ce qui impose une séquence de mise à jour précise.
- **Validating webhooks** : adaptation pour éviter les conflits entre les deux opérateurs.
- **Rollout progressif** : migration cluster par cluster en production, avec validation à chaque étape.
- **Tests de coexistence** approfondis pour garantir que les deux versions n'interfèrent pas.

## Avis

Ce qui rend cette approche intéressante, ce n'est pas tant la technique en soi — le side-by-side existe depuis longtemps comme pattern de déploiement — c'est son application aux **opérateurs Kubernetes stateful**.

Dans la plupart des organisations, l'upgrade d'un opérateur critique reste une opération semi-manuelle, planifiée en maintenance window, avec un rollback plan qu'on espère ne jamais utiliser. L'approche de Mercari pousse vers quelque chose de plus industriel : on réduit le blast radius, on valide en continu, et surtout on rend l'opération **reproductible et automatisable**.

C'est exactement l'état d'esprit qu'il faut avoir en Platform Engineering. Chaque opération manuelle récurrente est une dette. Si un upgrade d'opérateur nécessite un runbook de 40 étapes et une équipe en astreinte, c'est qu'on n'a pas assez outillé le processus. Le pattern side-by-side, combiné à une bonne CI/CD sur les composants infra, pourrait devenir un standard pour tout opérateur gérant des workloads stateful — pas seulement ECK, mais aussi des opérateurs PostgreSQL, Kafka, Redis.

La limite reste la complexité de maintenir un opérateur forké ou modifié. Mercari a les moyens de porter cette charge. Pour des équipes plus petites, il serait pertinent de pousser ce pattern en upstream.

[Article source](https://engineering.mercari.com/en/blog/entry/20250428-upgrading-eck-operator-a-side-by-side-kubernetes-operator-upgrade-approach/)
