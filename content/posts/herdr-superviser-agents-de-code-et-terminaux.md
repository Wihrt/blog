---
title: "Herdr : superviser agents de code et terminaux"
slug: "herdr-superviser-agents-de-code-et-terminaux"
date: 2026-11-12T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Herdr est une app desktop qui centralise terminaux et agents de code avec une CLI pilotable."
tags:
  - ai
  - rust
  - cli
  - automation
  - devops
  - platform-engineering
series:
  - Veille techno
series_order: 191
showTableOfContents: true
---

## Un outil pour centraliser terminaux et agents de code

Gérer plusieurs sessions de terminal et plusieurs agents de code en parallèle devient vite ingérable à la main. Herdr propose une approche desktop pour organiser tout ça et, surtout, pour le superviser depuis une interface unique.

## Ce que propose Herdr

L'application organise le travail en **spaces**, divisés en **tabs** et **panes**. Particularité notable : fermer la fenêtre ne coupe pas vos sessions. Un process core séparé garde les terminaux actifs en arrière-plan, ce qui évite de perdre le contexte en cas de fermeture accidentelle ou de redémarrage de l'interface.

Une sidebar dédiée affiche l'état des agents de code sur l'ensemble des spaces :

- en cours
- bloqué
- terminé
- idle

Herdr permet aussi de se connecter à des machines distantes en SSH, et son apparence est personnalisable via des "mods" écrits en JavaScript. Côté build, le projet nécessite Rust 1.95.0 et Zig 0.16.0, avec des scripts d'installation pour Linux, macOS (shell) et Windows (PowerShell). Une CLI (`--skill`, `ls`, `status`, `commands`) permet de piloter la fenêtre directement depuis les agents.

## Pourquoi ça compte pour l'automatisation

Le point qui retient l'attention, c'est la CLI. Les agents de code autonomes commencent à se généraliser, mais leur gestion reste souvent manuelle : on ouvre un terminal, on surveille, on relance si besoin. Avoir une interface scriptable pour interroger l'état d'une flotte d'agents (`status`, `ls`) ou déclencher des actions (`commands`) ouvre la porte à une vraie intégration dans des pipelines CI/CD ou des scripts d'orchestration maison.

Pour une équipe DevOps ou Platform Engineering, ça change la donne sur un point précis : au lieu de surveiller des agents à l'œil, on peut les traiter comme n'importe quel composant d'infra, avec des hooks et des checks automatisés. Reste à évaluer la robustesse du core process en production et la maturité de l'écosystème de mods, mais la direction prise est cohérente avec les besoins actuels d'automatisation outillée.

Source : https://github.com/herdrdev/herdr-app
