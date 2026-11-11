---
title: "Have I Been Pwned 2.0 : refonte UI, API stable"
slug: "have-i-been-pwned-2-0-refonte-ui-api-stable"
date: 2026-11-11T19:10:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "HIBP 2.0 modernise l'interface et le dashboard sans changer l'API, un atout pour les workflows DevOps automatisés."
tags:
  - security
  - api
  - automation
  - devops
  - platform-engineering
series:
  - Veille techno
series_order: 183
showTableOfContents: true
---

## Introduction

Have I Been Pwned (HIBP) est un outil incontournable dans l'écosystème sécurité. Troy Hunt vient de publier la version 2.0 de la plateforme, avec une refonte complète. Pour les équipes DevOps et Platform Engineering, la question est simple : qu'est-ce que ça change concrètement, notamment pour les usages automatisés ?

## Ce que contient la mise à jour

La version 2.0 de HIBP apporte plusieurs évolutions notables :

- **Nouvelle interface** : refonte complète du front, migration vers des technologies web modernes pour de meilleures performances.
- **Recherche améliorée** : la recherche par email et par domaine a été affinée, avec des résultats plus pertinents.
- **Pages de breach dédiées** : chaque breach dispose désormais d'une page avec des conseils ciblés.
- **Dashboard centralisé** : un tableau de bord unique qui consolide les fonctionnalités utilisateur (vérification email, gestion de domaine, etc.).
- **API inchangée** : c'est le point majeur — l'API publique reste identique, aucune migration nécessaire côté consommateurs.
- **Merch store** : anecdotique mais présent, Troy Hunt monétise aussi via du merchandising.

## Avis

Ce qui retient mon attention ici, c'est la stabilité de l'API. Dans un contexte DevOps ou Platform Engineering, HIBP s'intègre dans des workflows d'automatisation concrets : vérification de credentials compromis dans un pipeline CI/CD, monitoring de domaines d'entreprise, alertes automatisées sur de nouvelles breaches touchant des adresses internes.

Le fait que Troy Hunt ait choisi de moderniser toute la couche front et l'expérience utilisateur **sans toucher à l'interface programmatique** est un choix d'architecture qui mérite d'être souligné. C'est exactement ce qu'on attend d'un service qu'on consomme via API : pouvoir évoluer sans imposer de breaking changes.

Le domain search affiné et le dashboard centralisé sont aussi des pistes intéressantes pour outiller des équipes sécurité ou SRE qui veulent un point d'entrée simple, sans avoir à tout scripter. La combinaison des deux — interface humaine améliorée + API stable — permet de couvrir à la fois les usages manuels et automatisés sans compromis.

Un refresh propre, bien exécuté, qui ne casse rien. C'est suffisamment rare pour le noter.

**Source** : [https://www.troyhunt.com/have-i-been-pwned-2-0-is-now-live/](https://www.troyhunt.com/have-i-been-pwned-2-0-is-now-live/)
