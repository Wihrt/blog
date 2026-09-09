---
title: "Do-nothing scripting : automatiser progressivement ses procédures ops"
slug: "do-nothing-scripting-automatiser-progressivement-ses-procedures-ops"
date: 2026-09-08T22:16:45+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Un pattern simple pour formaliser en code les procédures manuelles avant de les automatiser étape par étape."
tags:
  - automation
  - devops
  - platform-engineering
  - productivity
series:
  - Veille techno
series_order: 82
showTableOfContents: true
---

## Contexte

Toute équipe ops accumule des procédures manuelles qui n'ont jamais été automatisées, faute de temps, de priorité ou simplement parce que le sujet est toujours repoussé. Le do-nothing scripting est une approche qui s'attaque à ce problème sans exiger un investissement massif dès le départ.

## Ce que propose l'article

Dan Slimmon décrit un pattern simple : un script qui n'exécute aucune action à la place de l'opérateur, mais qui encode chaque étape d'une procédure manuelle dans une fonction dédiée. Le script guide l'utilisateur pas à pas, affiche les instructions de l'étape en cours, puis attend une confirmation avant de passer à la suivante.

Les bénéfices immédiats sont concrets :

- La procédure est formalisée dans du code, pas dans un doc qu'on retrouve difficilement.
- L'exécution est traçable et reproductible.
- Chaque fonction peut être remplacée par une implémentation automatisée quand le moment est venu, sans toucher au reste.

## Avis

Ce pattern répond à un problème réel : le blocage du "tout ou rien" dans l'automatisation. On reporte souvent une automatisation parce qu'elle semble trop complexe à faire entièrement. Le do-nothing script déplace le problème : on structure d'abord, on automatise ensuite, étape par étape.

Pour une équipe platform ou SRE, c'est une façon honnête d'industrialiser sans se mentir sur l'état réel des choses. Un runbook dans Confluence, personne ne le suit vraiment à la lettre. Un script qui impose un flux d'exécution, c'est différent : il contraint sans bloquer, il documente en faisant.

L'implication concrète : ce type de script peut aussi servir de base d'audit. On voit exactement où les humains interviennent encore, ce qui permet de prioriser les efforts d'automatisation là où ils ont le plus de valeur. C'est une approche qui s'intègre naturellement dans une démarche d'amélioration continue, sans nécessiter de refonte complète des processus existants.

## Source

https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/
