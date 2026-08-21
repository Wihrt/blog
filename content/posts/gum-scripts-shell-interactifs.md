---
title: "Gum : rendre ses scripts shell interactifs sans effort"
slug: "gum-scripts-shell-interactifs"
date: 2025-11-20T08:00:00+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Menus, saisies et confirmations en une ligne de commande, pour transformer un script shell ou des dotfiles en outil agréable à utiliser."
tags:
  - cli
  - linux
  - automation
  - productivity
series:
  - Veille techno
series_order: 39
showTableOfContents: true
---

## Introduction

En tant que développeur ou ingénieur DevOps, écrire des scripts shell efficaces fait partie du quotidien. Mais entre complexité croissante des infrastructures (Kubernetes, CI/CD, monitoring) et nécessité d’automatiser, chaque gain de temps devient précieux. Aujourd’hui, je vous parle de Gum, un outil qui rend vos scripts shell plus interactifs, simples et robustes.

## Résumé de l’article

L’article présente **Gum**, une boîte à outils en ligne de commande permettant de créer des interfaces utilisateur dans vos scripts shell – rapidement et sans effort. Après avoir installé Gum, vous pouvez intégrer des éléments interactifs comme `gum choose` pour interroger l’utilisateur (ex : choisir un type de commit). Gum propose des options poussées comme `--no-limit` pour sélectionner plusieurs éléments. En partant d’un simple script `#!/bin/sh`, on peut construire un outil complet pour nos dotfiles ou workflows CI/CD.

## Pourquoi c’est utile pour les pros tech

### Gain de temps dans l’automatisation

Les pipelines d’intégration continue ou de déploiement via Kubernetes utilisent souvent des scripts shell. Grâce à Gum, ces scripts deviennent interactifs, ce qui facilite le débogage et la configuration.

### Des dotfiles intelligents

Configurer ses dotfiles pour gérer les environnements de dev, monitoring ou outils CLI devient simple : on peut demander dynamiquement à l’utilisateur ce qu’il veut activer ou installer.

### Idéal en équipe

Dans un contexte DevOps, diffuser ces scripts à vos collègues améliore l’onboarding. Plus besoin de documentation interminable : un script Gum bien conçu guide l’utilisateur pas à pas.

## Mon retour d’expérience

J’ai intégré Gum dans mes dotfiles personnels. Par exemple, lors de l’installation de dépendances pour mon environnement de monitoring, j’utilise `gum choose` pour activer ou non certains outils. Résultat : un setup personnalisé, fluide, sans avoir à modifier manuellement le script. Autre cas : dans un projet CI/CD, j’ai utilisé Gum pour créer un menu dynamique qui permet à chacun de spécifier ses paramètres de build. Les retours de l’équipe ont été très positifs : ‘simple mais super utile’.

## Conclusion

Gum n’est peut-être qu’un petit outil, mais il transforme l’expérience développeur dès qu’on travaille avec des scripts shell. À l’heure où tout s’automatise – du déploiement Kubernetes à la gestion de la configuration – c’est une excellente addition à votre boîte à outils. Curieux d’en savoir plus ? Lisez [l’article complet ici](https://api.daily.dev/r/t-03IP19_).
