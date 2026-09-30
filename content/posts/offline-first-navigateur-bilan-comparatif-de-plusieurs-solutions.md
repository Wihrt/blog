---
title: "Offline-first navigateur : bilan comparatif de plusieurs solutions"
slug: "offline-first-navigateur-bilan-comparatif-de-plusieurs-solutions"
date: 2026-09-30T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Retour d'expérience sur WatermelonDB, Triplit, PowerSync et Replicache pour la persistance offline dans un client mail."
tags:
  - database
  - storage
  - devops
  - platform-engineering
series:
  - Veille techno
series_order: 86
showTableOfContents: true
---

## Introduction

L'architecture offline-first revient régulièrement dans les discussions, mais les retours terrain sur ses limites concrètes dans un navigateur web restent rares. L'équipe de Marco, qui développe un client email cross-platform, vient de publier un compte-rendu détaillé de leur évaluation de plusieurs solutions du marché.

## Ce qu'il faut retenir

L'équipe a passé en revue plusieurs outils : **WatermelonDB**, **Triplit**, **InstantDB** et **PowerSync**. L'objectif était de gérer la synchronisation et la persistance locale pour un client mail — donc des volumes de données significatifs (100 Mo et plus).

Le constat principal : toutes ces solutions reposent in fine sur **IndexedDB**, qui reste un stockage clé-valeur avec des contraintes de performance bien réelles. Au-delà d'un certain volume, les performances se dégradent de manière notable. Aucune solution évaluée n'a tenu le choc seule sur l'ensemble des besoins (sync, persistance, recherche/indexation).

L'équipe a finalement opté pour une combinaison : **Replicache** pour la synchronisation des données et **Orama** pour l'indexation et la recherche. Deux outils spécialisés plutôt qu'un monolithe.

## Analyse

Ce retour est particulièrement utile pour les équipes plateforme et DevOps, même si le sujet semble "front-end" à première vue.

D'abord, parce que la **persistance locale dans le navigateur, c'est de l'infra**. Quand on outille des équipes produit ou qu'on définit des standards d'architecture, il faut connaître les limites réelles de `IndexedDB` pour ne pas valider des choix techniques qui s'effondrent en conditions réelles.

Ensuite, l'approche retenue — **composer des briques spécialisées** plutôt que de chercher l'outil unique — est un pattern classique côté infrastructure (on ne met pas tout dans le même Helm chart). Le voir confirmé sur la couche client avec des données chiffrées renforce l'idée que cette discipline de composition est universelle.

Enfin, pour ceux qui cherchent à **automatiser et standardiser** les choix technologiques dans une organisation, ce type de benchmark terrain est une ressource concrète à intégrer dans un ADR ou un radar techno interne. Plutôt que de refaire l'évaluation, autant capitaliser sur le travail déjà fait.

À garder sous le coude si le sujet offline-first remonte dans vos discussions d'architecture.

🔗 [Article source](https://marcoapp.io/blog/offline-first-landscape)
