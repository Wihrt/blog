---
title: "Software catalog avec Backstage : automatisation et ownership"
slug: "software-catalog-avec-backstage-automatisation-et-ownership"
date: 2026-11-11T18:50:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Guide pratique pour construire un software catalog avec Backstage : YAML versionné, automatisation et ownership des services."
tags:
  - platform-engineering
  - automation
  - devops
series:
  - Veille techno
series_order: 163
showTableOfContents: true
---

## Introduction

Dans les organisations qui opèrent plusieurs dizaines de services, la question "qui possède ce composant et où est sa doc ?" revient trop souvent. Le software catalog est une réponse structurée à ce problème — et Backstage est aujourd'hui l'un des outils les plus matures pour le mettre en place.

## Ce que couvre l'article

L'article propose un guide pratique pour construire un software catalog avec Backstage :

- **Pourquoi un catalog** : réduire la redondance, centraliser les informations sur les services, clarifier l'ownership.
- **Structure YAML** : chaque composant est décrit via un fichier `catalog-info.yaml` versionné avec le code.
- **Automatisation des entrées** : Backstage peut découvrir et ingérer les composants automatiquement à partir de ces fichiers, sans saisie manuelle.
- **Documentation et ownership** : chaque entrée du catalog peut embarquer des liens vers la doc, le repo, les contacts responsables.

Le guide est progressif, adapté à quelqu'un qui démarre avec Backstage.

## Analyse et point de vue

L'automatisation est la clé de voûte de tout catalog utile. Un catalog alimenté manuellement est condamné à devenir obsolète — c'est une question de mois, pas d'années. Ce que Backstage permet avec les fichiers YAML versionnés, c'est d'aligner le cycle de vie du catalog sur celui du code : quand le service évolue, la description évolue avec lui.

Cela a des implications concrètes pour les équipes Platform Engineering :

- **Onboarding accéléré** : un nouveau développeur trouve propriétaire, doc et dépendances en un seul endroit.
- **Réduction des doublons** : avant de créer un service, on vérifie s'il existe déjà quelque chose de similaire.
- **Gouvernance facilitée** : l'ownership explicite dans le catalog devient une base pour les audits, la gestion des incidents, les plans de migration.

La vraie difficulté n'est pas technique — c'est l'adoption. Un catalog ne vit que si les équipes jouent le jeu de renseigner et maintenir leurs fichiers. L'automatisation réduit la friction, mais ne l'élimine pas. C'est un investissement organisationnel autant que technique.

## Source

https://faun.pub/platform-engineering-in-action-building-a-software-catalog-2fa7833b2fb2
