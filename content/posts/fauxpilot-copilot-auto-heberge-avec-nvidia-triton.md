---
title: "FauxPilot : Copilot auto-hébergé avec NVIDIA Triton"
slug: "fauxpilot-copilot-auto-heberge-avec-nvidia-triton"
date: 2026-11-11T18:04:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "FauxPilot combine CodeGen et NVIDIA Triton pour un assistant de code auto-hébergé, avec ses contraintes GPU et licence."
tags:
  - ai
  - self-hosted
  - open-source
  - platform-engineering
series:
  - Veille techno
series_order: 117
showTableOfContents: true
---

## Contexte

Les assistants de complétion de code cloud posent des questions légitimes : confidentialité des données, conformité, dépendance à un tiers. FauxPilot est une tentative de répondre à ça en proposant une stack auto-hébergée calquée sur GitHub Copilot.

## Ce que fait FauxPilot

FauxPilot repose sur plusieurs briques :

- Les modèles **CodeGen de Salesforce**, entraînés sur du code source.
- **NVIDIA Triton Inference Server** comme moteur de serving.
- Le backend **FasterTransformer** pour l'optimisation de l'inférence sur GPU.

Pour faire tourner le modèle `6B` (6 milliards de paramètres), le prérequis matériel annoncé est **deux NVIDIA RTX 3080**. Le container fourni est soumis à la **NVIDIA Deep Learning Container License**, qui impose des restrictions non négligeables sur l'usage et la redistribution.

## Point de vue

L'automatisation, ça commence par choisir les bons outils — et par choisir lesquels on contrôle vraiment. Un assistant de code local, c'est une piste intéressante pour des équipes qui gèrent des bases de code sensibles ou évoluent dans des environnements avec des contraintes de conformité fortes (secteur financier, santé, défense).

Mais FauxPilot dans son état actuel soulève deux points de friction concrets :

1. **Le prérequis hardware** : deux RTX 3080 pour le modèle 6B, c'est une barrière réelle. Peu d'équipes ont ce genre de capacité GPU disponible en dehors de contextes ML dédiés.
2. **La licence NVIDIA sur le container** : elle mérite une lecture attentive avant tout déploiement, même en interne. Ce n'est pas une licence open source permissive.

Pour une équipe Platform Engineering, l'intérêt de ce type de projet est moins dans l'outil lui-même que dans la direction qu'il pointe : maîtriser la couche d'inférence, éviter la fuite de données vers des APIs tierces, et construire une automatisation qui reste dans le périmètre de l'infrastructure maîtrisée.

À surveiller dans ses évolutions, notamment si des alternatives de serving moins contraintes émergent.

## Source

https://github.com/moyix/fauxpilot
