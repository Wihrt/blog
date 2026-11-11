---
title: "Nix et Docker : vers des builds reproductibles"
slug: "nix-et-docker-vers-des-builds-reproductibles"
date: 2026-11-11T18:56:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Kelsey Hightower explore comment Nix peut compléter Docker pour des builds déterministes et sécurisés."
tags:
  - docker
  - devops
  - security
  - platform-engineering
  - ci-cd
series:
  - Veille techno
series_order: 169
showTableOfContents: true
---

## Introduction

Kelsey Hightower, figure incontournable de l'écosystème Kubernetes et cloud-native, a récemment pris la parole à la Southern California Linux Expo pour explorer une question qui agite les cercles DevOps : Nix peut-il offrir ce que Docker ne garantit pas en matière de reproductibilité et de sécurité des builds ?

## Ce que dit l'article

Hightower partage son parcours de découverte de Nix et identifie plusieurs limites de l'approche Docker classique :

- Les builds Docker ne sont **pas hermétiques par défaut**. Un `apt-get update` dans un Dockerfile produit des résultats différents selon le moment où il est exécuté.
- La **supply chain security** reste un point faible : les images de base évoluent, les dépendances dérivent silencieusement.
- Nix propose un modèle où chaque dépendance est **hashée et verrouillée**, rendant les builds véritablement reproductibles.

Plutôt que d'opposer les deux outils, Hightower propose une **synergie** : utiliser Nix pour la construction déterministe des artefacts, et Docker pour l'empaquetage et la distribution via son écosystème établi (registries, orchestrateurs, runtime OCI).

## Avis

Le sujet n'est pas nouveau, mais le fait que Hightower le porte lui donne une visibilité que la communauté Nix n'avait pas à cette échelle. Et il pose la bonne question : on cherche en permanence des outils pour **fiabiliser l'automatisation**, pas pour ajouter de la complexité.

Concrètement, pour une équipe plateforme, l'enjeu est clair. Si vous maintenez des dizaines de Dockerfiles avec des étapes de build non déterministes, vous avez déjà rencontré le problème que Nix résout — un build qui passe en CI le lundi et casse le jeudi sans changement de code. La difficulté réside dans la **courbe d'apprentissage de Nix** (le langage, les `flakes`, l'écosystème `nixpkgs`) et dans l'intégration avec les pipelines CI/CD existants.

L'approche hybride est la plus réaliste : générer des images OCI avec `nix build` tout en conservant le runtime Docker et l'orchestration Kubernetes. Cela permet de gagner en déterminisme sans abandonner l'outillage que les équipes maîtrisent déjà. C'est un investissement progressif, pas une migration big-bang.

À surveiller si vous travaillez sur la **sécurité de la supply chain** ou si la reproductibilité de vos builds est un irritant récurrent.

**Source :** https://thenewstack.io/kelsey-hightower-on-nix-vs-docker-is-there-a-different-way/
