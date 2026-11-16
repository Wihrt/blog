---
title: "Pele : rendu Mermaid en SVG, léger et rapide"
slug: "pele-rendu-mermaid-en-svg-leger-et-rapide"
date: 2026-11-16T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Pele, une lib open source zero-dependency qui rend Mermaid en SVG plus vite et plus léger que Mermaid.js."
tags:
  - open-source
  - automation
  - platform-engineering
series:
  - Veille techno
series_order: 193
showTableOfContents: true
---

## Le problème avec Mermaid.js

Mermaid.js s'est imposé comme le standard pour générer des diagrammes directement depuis du texte en Markdown. Pratique, mais son poids et ses temps de rendu peuvent devenir un frein, notamment dans des outils tournant en local comme Obsidian, ou dans des pipelines où chaque milliseconde et chaque Mo comptent.

## Ce que propose Pele

Pele est une librairie open source zero-dependency qui rend la syntaxe Mermaid en SVG, entièrement stylée via variables CSS. Quelques points clés :

- Bundle annoncé 6x plus léger que Mermaid.js

- Temps de rendu jusqu'à 500x plus rapides selon les benchmarks du projet

- Support complet de tous les types de diagrammes de Mermaid 12.1.0

- Changement de couleurs sans re-render, grâce aux variables CSS

- Adaptation réelle de la mise en page sur petits écrans, plutôt qu'un simple scaling

La librairie a été construite au départ pour Obsidian, ce qui explique son focus sur la légèreté et la rapidité d'exécution en environnement local.

## Mon avis

Ce type d'outil prend tout son sens dans une logique d'automatisation documentaire. Génération de schémas d'architecture dans un pipeline CI, docs-as-code, rendu à la volée dans des dashboards internes : dans tous ces cas, la légèreté et l'absence de dépendances lourdes simplifient grandement l'intégration. Pas besoin de traîner un écosystème Node complet pour afficher un diagramme de séquence ou un flowchart.

Pour des équipes plateforme qui cherchent à industrialiser la génération de documentation technique, un rendu rapide et stylable via CSS pur permet aussi de s'aligner facilement sur un design system existant, sans custom JS supplémentaire.

Reste la question de la maturité : l'écosystème autour de Mermaid.js (plugins, intégrations CI, éditeurs) est large et éprouvé. Pele devra faire ses preuves sur la durée et la compatibilité avant de devenir un choix par défaut en production.

Source : https://pele.run/
