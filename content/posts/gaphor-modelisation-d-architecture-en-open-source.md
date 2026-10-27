---
title: "Gaphor : modélisation d'architecture en open source"
slug: "gaphor-modelisation-d-architecture-en-open-source"
date: 2026-10-27T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Gaphor combine UML, SysML et C4 avec des exports PDF/SVG/XML, utiles pour documenter en mode docs-as-code."
tags:
  - open-source
  - platform-engineering
  - devops
  - automation
series:
  - Veille techno
series_order: 106
showTableOfContents: true
---

## Introduction

La modélisation d'architecture est souvent reléguée à des outils graphiques isolés, déconnectés des workflows d'ingénierie. Gaphor, outil open source multiplateforme, propose une alternative sérieuse — et soulève une question plus large : comment intégrer la modélisation dans des flux automatisés ?

## Ce que fait Gaphor

Gaphor est une application de modélisation gratuite et open source, disponible sur Linux, Windows et macOS. Elle supporte plusieurs langages de modélisation :

- **UML** : pour la modélisation logicielle classique
- **SysML** : orienté systèmes complexes
- **RAAML** : pour l'analyse de risques
- **C4** : pour la documentation d'architecture logicielle à différents niveaux d'abstraction

Les diagrammes peuvent être exportés en **PDF, PNG, SVG et XML**, ce qui ouvre des possibilités d'intégration concrètes.

## Avis

L'angle intéressant avec Gaphor, ce n'est pas uniquement d'avoir un outil de dessin gratuit. C'est la combinaison entre des formats d'export ouverts et standards, et le support du modèle C4 — particulièrement utile pour les équipes platform engineering qui cherchent à documenter des systèmes distribués de façon cohérente et maintenable.

Le format XML en sortie laisse entrevoir des usages dans des pipelines de documentation automatisée : génération de diagrammes à partir de sources de vérité, intégration dans des workflows CI/CD pour maintenir la documentation à jour, ou versionnement des modèles directement dans un dépôt Git aux côtés du code.

Le SVG, lui, est directement exploitable dans des sites de documentation statiques (type docs-as-code avec MkDocs ou Docusaurus) sans perte de qualité.

L'enjeu pour une équipe DevOps ou Platform Engineering n'est pas de trouver le meilleur outil de dessin, mais de traiter la modélisation comme un artefact à part entière — versionnable, automatisable, intégrable. Gaphor, de par son format open source et ses exports standards, s'inscrit dans cette logique.

## Source

https://itsfoss.com/gaphor-modeling-tool/
