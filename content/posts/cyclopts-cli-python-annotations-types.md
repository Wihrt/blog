---
title: "Cyclopts : des CLI Python générées depuis vos annotations"
slug: "cyclopts-cli-python-annotations-types"
date: 2025-10-20T09:00:21+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Un framework Python moderne qui dérive la CLI des annotations de types, compatible Pydantic, dataclasses et Attrs."
tags:
  - python
  - cli
  - open-source
  - productivity
series:
  - Veille techno
series_order: 19
showTableOfContents: true
---

## Introduction

Quand il s'agit de créer des outils en ligne de commande (CLI) pour automatiser nos workflows DevOps, interagir avec des clusters Kubernetes ou simplement faciliter nos tâches quotidiennes, avoir le bon framework fait toute la différence. Récemment, j'ai découvert **Cycloptsis**, une nouvelle bibliothèque Python conçue pour rendre la création de CLI plus simple, plus lisible et surtout plus puissante.

## Résumé de l’article

L'article [Cycloptsis: a modern Python CLI framework](https://api.daily.dev/r/EHtqYtae6) présente Cycloptsis, un framework Python moderne qui exploite les annotations de types pour générer automatiquement des CLI intuitives. Compatible avec **Pydantic**, **dataclasses** et **Attrs**, il permet aussi de créer des pages d'aide complètes à partir de simples docstrings. Il propose une syntaxe concise plus agréable que des alternatives comme Typer. Il fonctionne avec Python 3.9+ et supporte à la fois les approches fonctionnelles et orientées application.

## Pourquoi c’est utile pour les pros tech

### Productivité accrue

Avec Cycloptsis, plus besoin de répéter du code : les types parlent d'eux-mêmes. En tant que développeur ou ingénieur DevOps, cela signifie que je peux me concentrer sur la logique métier plutôt que sur la gestion des arguments CLI.

### Intégration naturelle avec l’écosystème Python

L'intégration native avec Pydantic ou dataclasses rend Cycloptsis idéal dans des environnements CI/CD complexes ou des scripts d'observabilité. On peut facilement valider des entrées utilisateurs ou des configurations, ce qui est parfait pour de la configuration système ou du monitoring.

### Documentation automatique

La génération automatique des pages d'aide rend nos outils immédiatement utilisables par d'autres membres de l'équipe, sans documentation supplémentaire. C'est un vrai plus dans un contexte de travail collaboratif ou de déploiement.

## Mon retour d’expérience

Je l'ai testé sur un petit projet de gestion de pods Kubernetes en interne. En quelques lignes de code, j'avais un outil complet, avec validation de type, aide automatique et une structure claire. L'expérience m'a rappelé la productivité de FastAPI, mais appliquée au monde de la CLI. Bien que le projet soit encore jeune, la base est solide. Et franchement, je ne vois plus l'intérêt de revenir à argparse.

## Conclusion

Cycloptsis change la donne pour tous ceux qui créent des outils en ligne de commande avec Python. Que vous soyez développeur, ingénieur DevOps ou passionné par l'automatisation et le monitoring, ce framework mérite clairement votre attention. Vous pouvez découvrir [l’article original](https://api.daily.dev/r/EHtqYtae6).
