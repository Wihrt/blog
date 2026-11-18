---
title: "Sheety : compiler un tableur en binaire exécutable"
slug: "sheety-compiler-un-tableur-en-binaire-executable"
date: 2026-11-18T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Sheety compile des feuilles de calcul en binaires autonomes avec TUI, sans dépendance runtime."
tags:
  - open-source
  - cli
  - automation
  - platform-engineering
series:
  - Veille techno
series_order: 195
showTableOfContents: true
---

## Un hobby project qui compile des tableurs

Sheety est un projet personnel de Roberto Alsina, codé en Crystal. L'idée : prendre une définition de feuille de calcul et la compiler en un binaire exécutable autonome, avec une interface terminal (TUI) qui supporte même la souris.

## Ce que fait Sheety

Quelques points clés :

- Zéro dépendance runtime : le binaire généré tourne seul, sans interpréteur ni bibliothèque externe à installer.
- Import/export au format Excel ou en YAML lisible par un humain.
- Recompilation à la volée : dès qu'une formule est modifiée, l'outil se recompile automatiquement.
- Écrit en Crystal, un langage compilé proche de Ruby en syntaxe.

L'auteur le présente lui-même comme un projet que "personne n'a vraiment besoin", mais amusant à construire et à tester. Le code source est disponible sur GitHub.

## Un avis terrain

Sur le papier, Sheety ne résout aucun problème urgent de production. Mais ce genre d'outil mérite d'être regardé de près par qui travaille sur l'automatisation. Compiler une logique de calcul en artefact autonome, sans runtime à gérer, c'est exactement le type de pattern qu'on cherche quand on veut packager une petite brique métier dans un pipeline CI/CD ou un script d'infra.

Pour une équipe platform engineering, l'intérêt n'est pas d'utiliser Sheety tel quel, mais de retenir l'approche : transformer une définition déclarative (ici un tableur) en binaire portable, déployable sans dépendance. C'est une logique qu'on retrouve dans des outils d'infra-as-code ou de génération de configuration. Un hobby project, certes, mais qui illustre bien comment l'automatisation se nourrit d'expérimentations en apparence gadget.

## Source

https://hackaday.com/2026/09/30/sheety-turns-spreadsheets-into-binaries-for-some-reason
