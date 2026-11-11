---
title: "mcpso : annuaire self-hosted de serveurs MCP avec Supabase"
slug: "mcpso-annuaire-self-hosted-de-serveurs-mcp-avec-supabase"
date: 2026-11-11T19:09:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "mcpso est un projet open source pour cataloguer et découvrir des serveurs MCP, basé sur TypeScript et Supabase."
tags:
  - self-hosted
  - open-source
  - typescript
  - database
  - ai
  - devops
series:
  - Veille techno
series_order: 182
showTableOfContents: true
---

## Introduction

Le protocole MCP (Model Context Protocol) gagne en traction dans les workflows d'automatisation et d'intégration IA. Avec cette adoption croissante, un besoin concret émerge : comment cataloguer et découvrir les serveurs MCP disponibles ? Le projet open source **mcpso** apporte une réponse simple et self-hosted.

## Ce que propose mcpso

Le repo [chatmcp/mcpso](https://github.com/chatmcp/mcpso) fournit une application permettant de déployer un **annuaire de serveurs MCP**. Côté stack :

- **TypeScript** pour le code applicatif
- **Supabase** comme backend de base de données (création et gestion des données)
- Setup standard : cloner le repo, installer les dépendances, configurer les variables d'environnement, lancer le serveur de développement

Le projet est pensé pour être opérationnel rapidement. Supabase permet d'éviter de provisionner une infrastructure base de données dédiée, ce qui rend le déploiement accessible même pour des petites équipes.

## Analyse et implications pour les équipes DevOps/Platform

L'intérêt principal de ce type d'outil réside dans la **centralisation de l'information**. Quand on commence à intégrer MCP dans des pipelines d'automatisation — que ce soit pour du tooling IA, de l'orchestration ou de l'intégration de contexte — le nombre de serveurs MCP disponibles peut croître rapidement. Sans catalogue, on retombe dans le travers classique : listes manuelles dans un wiki, recherche dans des repos GitHub, connaissance tribale.

Avoir un annuaire **requêtable et self-hosted** change la donne côté opérationnel. On peut envisager de l'intégrer dans des workflows de discovery automatisés, de le coupler avec du monitoring, ou simplement de donner aux équipes un point d'entrée unique pour savoir ce qui est disponible.

Le choix de Supabase est pragmatique : c'est suffisant pour ce cas d'usage, rapide à mettre en place, et ça évite d'ajouter une dépendance infra lourde. Pour les équipes qui veulent évaluer MCP à plus grande échelle, c'est le type de brique d'outillage qui **réduit la friction** et facilite l'adoption progressive.

Projet à surveiller, surtout si l'écosystème MCP continue de s'étoffer.

## Source

https://github.com/chatmcp/mcpso
