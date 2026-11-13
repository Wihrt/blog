---
title: "CloudNativePG 1.31 : rotation auto des passwords"
slug: "cloudnativepg-1-31-rotation-auto-des-passwords"
date: 2026-11-13T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "CloudNativePG 1.31 automatise la génération et la rotation des mots de passe PostgreSQL via Kubernetes."
tags:
  - kubernetes
  - postgresql
  - security
  - automation
  - platform-engineering
series:
  - Veille techno
series_order: 192
showTableOfContents: true
---

## Une feature qui règle un problème terrain classique

Gérer la rotation des mots de passe PostgreSQL dans un cluster Kubernetes est souvent bricolé : scripts cron, CronJobs maison, ou pire, oubli pur et simple jusqu'à l'incident. CloudNativePG 1.31 s'attaque à ce point avec une approche déclarative directement intégrée à l'opérateur.

## Ce que change la 1.31

La ressource `DatabaseRole` gagne un nouveau stanza `password`. En mode `generate`, l'opérateur :

- crée le mot de passe automatiquement ;
- le stocke dans un Secret qu'il possède et gère ;
- applique une politique de rotation via les champs `duration` et `renewBefore`.

Exemple concret donné dans l'article : une durée de vie de 720 heures, avec renouvellement un jour avant expiration. PostgreSQL applique lui-même cette limite via un timestamp `VALID UNTIL`, donc la contrainte est portée au niveau de la base, pas juste côté opérateur.

Un bloc `criteria` permet de définir les règles de complexité du mot de passe généré : longueur, présence de chiffres, de symboles. Une annotation dédiée permet aussi de déclencher une rotation immédiate en dehors du cycle planifié, utile en cas de compromission suspectée.

À noter : la feature est mergée sur le trunk de développement mais pas encore release. La 1.31 est attendue pour le dernier trimestre de l'année.

## Pourquoi c'est pertinent pour une équipe plateforme

Ce type de feature ne fait pas de bruit, mais c'est exactement ce qui compte dans l'outillage d'automatisation au quotidien. Déléguer la génération et la rotation des credentials à l'opérateur, avec une politique déclarative et versionnable, s'inscrit directement dans la logique GitOps : moins de scripts planqués dans un coin, moins de dépendance à une personne qui "sait comment ça marche".

Pour les équipes qui opèrent PostgreSQL sur Kubernetes à l'échelle, ça réduit un vecteur de risque réel : les credentials qui ne tournent jamais. Reste à voir comment ça s'intègre avec les solutions de secrets management externes (Vault, External Secrets) déjà en place dans beaucoup d'infra.

Source : https://postgr.es/p/9zS
