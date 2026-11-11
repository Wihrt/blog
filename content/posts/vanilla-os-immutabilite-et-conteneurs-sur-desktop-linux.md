---
title: "Vanilla OS : immutabilité et conteneurs sur desktop Linux"
slug: "vanilla-os-immutabilite-et-conteneurs-sur-desktop-linux"
date: 2026-11-11T18:21:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Distribution Ubuntu au système de fichiers immutable, avec apx pour isoler les paquets dans des conteneurs gérés."
tags:
  - linux
  - docker
  - open-source
  - platform-engineering
series:
  - Veille techno
series_order: 134
showTableOfContents: true
---

## Introduction

L'immutabilité est un principe bien ancré dans les pratiques DevOps côté infrastructure. Vanilla OS l'applique maintenant au desktop Linux. Une approche qui mérite une lecture attentive pour quiconque cherche à réduire la complexité de gestion des environnements.

## Ce que propose Vanilla OS

Vanilla OS est une distribution basée sur Ubuntu qui prend le parti d'un **système de fichiers immutable**. Concrètement, le système de base ne peut pas être modifié au fil du temps, ce qui limite la dérive de configuration.

Pour gérer les logiciels, la distribution introduit **`apx`**, son propre gestionnaire de paquets. Ce n'est pas un package manager classique : c'est un **wrapper autour de plusieurs gestionnaires existants** (`apt`, `dnf`, `pacman`...) qui installe et exécute les paquets à l'intérieur de **conteneurs gérés**. L'isolation est donc native, pas optionnelle.

Points clés :

- Système de fichiers immutable par défaut
- `apx` comme couche d'abstraction multi-package-manager
- Paquets isolés dans des conteneurs managés
- Base Ubuntu, donc écosystème connu

## Analyse

L'intention derrière cette architecture est claire : rendre le système difficile à casser et réduire l'état mutable à gérer. C'est exactement la même logique que celle appliquée aux images serveur immuables en infrastructure — on construit, on déploie, on ne patche pas en live.

Pour des équipes DevOps ou Platform Engineering, l'intérêt est double. D'abord, **faciliter l'automatisation** : un OS dont l'état de base est garanti simplifie les scripts de provisioning et réduit les cas limites liés à la dérive. Ensuite, **standardiser les environnements de développement** : si les paquets sont isolés dans des conteneurs, les conflits de dépendances entre projets deviennent structurellement moins probables.

Cela dit, Vanilla OS en est à sa première release. La maturité en contexte professionnel reste à évaluer. Les points de friction à surveiller : la compatibilité des outils métier, la gestion des mises à jour du système de base, et la courbe d'adoption pour des équipes habituées à des distros classiques.

À observer, pas encore à adopter en prod. Mais la direction est cohérente.

## Source

https://www.omglinux.com/vanilla-os-first-release-download/
