---
title: "Cours Microsoft sur les agents IA pour l'automatisation plateforme"
slug: "cours-microsoft-sur-les-agents-ia-pour-l-automatisation-plateforme"
date: 2026-10-08T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Microsoft propose un cours gratuit sur les agents IA (Semantic Kernel, AutoGen) utile aux équipes DevOps et Platform Engineering."
tags:
  - ai
  - automation
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 93
showTableOfContents: true
---

## Introduction

Microsoft propose un cours gratuit et complet sur la construction d'agents IA, disponible sur YouTube et accompagné de ressources sur GitHub. Pour les ingénieurs DevOps et Platform Engineering, le sujet est directement lié à une préoccupation quotidienne : **automatiser plus, mieux, et avec moins de friction**.

## Ce que couvre le cours

Le cours part des fondamentaux et va jusqu'à l'implémentation concrète :

- **Modèles de langage** : comprendre comment un LLM peut servir de moteur de décision pour un agent.
- **Mémoire** : comment un agent conserve du contexte entre les interactions, essentiel pour des workflows multi-étapes.
- **Outils** : la capacité d'un agent à appeler des fonctions, des API, à exécuter des actions concrètes.
- **Frameworks** : deux approches sont présentées — `Semantic Kernel` (orienté intégration dans des applications existantes) et `AutoGen` (orienté agents multi-acteurs).
- **Pratique** : des notebooks Jupyter permettent de manipuler directement les concepts, avec du code fonctionnel.

Le format mélange vidéos et code samples, ce qui permet d'avancer à son rythme.

## Avis

En Platform Engineering, on passe un temps significatif à construire des automatisations : pipelines CI/CD, réactions à des événements d'infrastructure, orchestration de workflows. Les agents IA représentent une évolution potentielle de cette couche d'orchestration.

Ce qui rend l'approche intéressante, c'est qu'on ne parle pas de coller un prompt sur un LLM en espérant un résultat. **Semantic Kernel** et **AutoGen** apportent une structure : gestion de la mémoire, appel d'outils, chaînage de tâches. C'est exactement ce qu'il faut pour que l'IA passe du gadget à l'outil fiable dans une chaîne d'automatisation.

Le cours reste introductif, il ne faut pas en attendre une solution clé en main pour des cas de production. Mais il pose les bases nécessaires pour évaluer sérieusement ce que les agents IA peuvent apporter à une équipe plateforme. Le fait que tout soit open source et disponible sur GitHub facilite l'expérimentation sans engagement.

Pour ceux qui cherchent à étendre leur boîte à outils d'automatisation, c'est une piste à explorer méthodiquement.

## Source

https://www.youtube.com/watch?v=OhI005_aJkA
