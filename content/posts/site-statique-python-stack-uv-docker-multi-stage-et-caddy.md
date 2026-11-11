---
title: "Site statique Python : stack uv, Docker multi-stage et Caddy"
slug: "site-statique-python-stack-uv-docker-multi-stage-et-caddy"
date: 2026-11-11T19:11:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Un pipeline reproductible qui build un site statique avec uv puis le sert via Caddy dans une image Docker minimale sans Python."
tags:
  - python
  - docker
  - caddy
  - self-hosted
  - devops
series:
  - Veille techno
series_order: 184
showTableOfContents: true
---

## Introduction

Générer un site statique avec Python et le déployer proprement en conteneur, sans traîner de runtime inutile en production : c'est un besoin récurrent pour de la documentation, des blogs techniques ou des pages internes. Un article récent propose une stack complète autour de `uv`, Docker et Caddy qui mérite qu'on s'y attarde.

## Ce que propose l'article

L'auteur détaille un pipeline de bout en bout :

- **`uv`** est utilisé pour la gestion des dépendances Python et l'exécution du build du site statique. Il remplace pip/pip-tools avec une approche plus rapide et reproductible.
- **Docker multi-stage** : le premier stage installe Python via `uv`, build le site, puis le second stage copie uniquement les fichiers générés dans une image **Caddy** légère.
- **Caddy** sert les fichiers avec une configuration déclarative couvrant plusieurs cas concrets : gestion multi-domaine, proxy pour l'analytics, pages d'erreur personnalisées et redirections.

Le résultat : une image de production qui ne contient ni Python, ni les dépendances de build. Juste Caddy et du HTML.

## Avis

Ce type de setup illustre bien une tendance de fond : **réduire au maximum ce qui tourne en production** en isolant les étapes de build. Le multi-stage Docker n'est pas nouveau, mais combiné avec `uv` — qui s'impose progressivement comme le gestionnaire de dépendances Python le plus efficace — on obtient un pipeline rapide et propre.

Caddy est un choix pertinent ici. Sa configuration est lisible, l'HTTPS automatique via Let's Encrypt fonctionne sans intervention, et la gestion des redirections ou du multi-domaine se fait en quelques lignes. Pour des équipes platform qui maintiennent des dizaines de petits sites internes (docs, status pages, landing pages), c'est le genre de pattern qui se templatise facilement et qu'on peut intégrer dans un workflow CI/CD standard.

L'idée de fond reste la même : chaque outil qu'on ajoute à la chaîne doit **simplifier l'automatisation**, pas la complexifier. Ici, chaque brique fait une chose et la fait bien. C'est sobre, c'est maintenable, et ça se déploie partout où Docker tourne.

## Source

https://nkantar.com/blog/2025/08/static-python-uv-caddy-docker/
