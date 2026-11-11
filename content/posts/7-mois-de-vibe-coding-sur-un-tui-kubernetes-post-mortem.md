---
title: "7 mois de vibe-coding sur un TUI Kubernetes : post-mortem"
slug: "7-mois-de-vibe-coding-sur-un-tui-kubernetes-post-mortem"
date: 2026-11-11T19:17:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Post-mortem d'un projet Go/Kubernetes développé avec Claude : 5 patterns d'échec de l'IA sans architecture posée en amont."
tags:
  - ai
  - kubernetes
  - go
  - rust
  - devops
series:
  - Veille techno
series_order: 190
showTableOfContents: true
---

## Introduction

Le vibe-coding — laisser une IA générer l'essentiel du code à partir de prompts — séduit par sa vélocité apparente. Mais que se passe-t-il quand on pousse l'approche pendant 7 mois sur un projet non trivial, un TUI Kubernetes GPU-aware ? Un développeur vient de publier un post-mortem détaillé après avoir archivé son projet **k10s**.

## Ce que dit l'article

L'auteur a développé k10s en Go avec Claude comme co-pilote principal. Le projet fonctionnait, les features s'empilaient. Puis la codebase s'est effondrée sous son propre poids. Il identifie **5 patterns d'échec récurrents** dans le développement assisté par IA sans garde-fous :

- **L'IA construit des features, pas de l'architecture** : le code produit résout le problème immédiat sans vision structurelle.
- **Le god object comme artefact par défaut** : l'IA centralise naturellement la logique dans des structures monolithiques.
- **L'illusion de vélocité** : la vitesse de production masque un scope creep permanent.
- **Les données positionnelles comme bombe à retardement** : des choix de modélisation fragiles qui cassent dès qu'on fait évoluer le code.
- **La mauvaise gestion des transitions d'état** : source de data races concrètes dans le projet.

Chaque pattern est illustré avec du code réel extrait du projet, accompagné de directives `CLAUDE.md` et `AGENTS.md` pour contraindre l'IA en amont. L'auteur repart de zéro en **Rust**, en posant l'architecture manuellement avant toute génération de code.

## Avis

Ce retour d'expérience met le doigt sur un problème structurel pour les équipes plateforme et DevOps. On cherche en permanence à automatiser, à outiller, à aller plus vite. L'IA générative s'insère naturellement dans cette logique. Mais elle produit du code **localement correct et globalement incohérent** si personne ne pose les contraintes architecturales.

Concrètement, sur du tooling interne — CLI, opérateurs, dashboards — le risque est exactement celui décrit ici : un prototype qui marche vite, qu'on pousse un peu trop loin, et qui devient un monolithe accidentel impossible à faire évoluer. Les directives `CLAUDE.md` proposées dans l'article sont une piste intéressante : traiter les contraintes d'architecture comme de la configuration, versionnée et partagée, plutôt que comme un savoir implicite.

L'approche "architecture d'abord, IA ensuite" n'est pas un retour en arrière. C'est probablement la seule façon de tirer parti de ces outils sans générer de la dette technique à haute vélocité.

🔗 [Article source](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand)
