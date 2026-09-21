---
title: "go-clean-template : structurer un projet Go avec config explicite"
slug: "go-clean-template-structurer-un-projet-go-avec-config-explicite"
date: 2026-09-21T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Un template Go d'Evrone qui impose une déclaration explicite des variables de config, utile en DevOps."
tags:
  - go
  - devops
  - platform-engineering
  - automation
series:
  - Veille techno
series_order: 80
showTableOfContents: true
---

## Introduction

Structurer un projet Go de manière cohérente reste un sujet récurrent dans les équipes qui cherchent à industrialiser leurs développements. `go-clean-template`, maintenu par Evrone, propose une base concrète — pas juste théorique — avec des choix techniques assumés.

## Ce que propose le template

Le template expose deux serveurs distincts :

- Un serveur **REST HTTP** basé sur le framework **Gin**
- Un second serveur utilisant **RabbitMQ comme transport**, également avec Gin

La configuration est centralisée dans `config.go`. Le point notable : le tag `env-required: true` oblige à déclarer explicitement chaque variable de configuration, que ce soit via un fichier yaml ou via des variables d'environnement. Aucune valeur ne peut être silencieusement absente.

L'architecture suit les principes clean (séparation des couches, inversion de dépendance), ce qui facilite la testabilité et la lisibilité du code métier.

## Avis

L'objectif ici est de trouver des outils qui facilitent l'automatisation — et ce template coche cette case sur un point précis : la gestion de la config.

Forcer la déclaration explicite des variables d'environnement, c'est créer une **documentation vivante et vérifiable**. En contexte DevOps ou Platform Engineering, c'est loin d'être anodin. Lors d'un déploiement Kubernetes, d'une mise en place de pipeline CI/CD, ou de l'onboarding d'un nouveau service, connaître à l'avance ce qui est requis évite des erreurs silencieuses et des configurations incomplètes découvertes trop tard.

Ce type de contrainte est simple à implémenter, mais rarement systématisée. Le template donne un exemple concret de la façon de l'ancrer dès la structure du projet.

Cela reste un point de départ — pas une solution à copier-coller en production sans adaptation. Mais c'est précisément l'intérêt d'un template bien conçu : poser des conventions utiles sans imposer de la complexité inutile.

## Source

https://github.com/evrone/go-clean-template
