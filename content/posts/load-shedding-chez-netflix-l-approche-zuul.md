---
title: "Load shedding chez Netflix : l'approche Zuul"
slug: "load-shedding-chez-netflix-l-approche-zuul"
date: 2026-11-11T18:05:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Netflix protège son API Gateway Zuul via un load shedding basé sur la concurrence plutôt que le CPU ou la latence."
tags:
  - api
  - platform-engineering
  - devops
  - monitoring
series:
  - Veille techno
series_order: 118
showTableOfContents: true
---

## Contexte

Le load shedding est une technique connue, mais son implémentation au niveau d'un API Gateway reste moins documentée que côté applicatif. Netflix détaille son approche avec **Zuul**, et les choix d'architecture méritent qu'on s'y arrête.

## Ce que dit l'article

Zuul agit comme point d'entrée entre les clients et les services backend. Il gère le routing, l'authentification, le rate limiting et le monitoring.

Face à une surcharge, Netflix a choisi d'implémenter le load shedding directement dans Zuul plutôt qu'au niveau applicatif. Le mécanisme : throttle les requêtes qui tombent sous un certain **seuil de priorité**. L'objectif premier est de protéger le gateway lui-même.

Les métriques utilisées pour déclencher ce throttling global sont basées sur la **concurrence** — le nombre de requêtes traitées simultanément. C'est un choix délibéré : la concurrence reflète mieux l'état réel du système que le CPU ou la latence seuls.

## Analyse

Ce qui est intéressant dans cette approche, c'est la philosophie sous-jacente : **automatiser la décision de protection plutôt que de la laisser à l'humain sous pression**.

Pour une équipe Platform Engineering, c'est une direction claire. Un composant d'infrastructure qui sait se protéger lui-même réduit mécaniquement la charge cognitive des équipes lors des incidents. On ne gère plus un système qui subit — on opère un système qui réagit de manière prévisible.

La vraie complexité ne réside pas dans le code du mécanisme, mais dans la **définition des priorités et des seuils**. Quelles requêtes sont critiques ? Quel niveau de concurrence est acceptable avant de commencer à délester ? Ces décisions impliquent le produit, le SRE et l'infra. Ce n'est pas une config, c'est une politique.

Pour les équipes qui cherchent à aller vers plus d'automatisation, ce pattern est une brique utile : intégrer des comportements défensifs dans la plateforme plutôt que de réagir en prod.

## Source

https://blog.quastor.org/p/netflix-implements-load-shedding
