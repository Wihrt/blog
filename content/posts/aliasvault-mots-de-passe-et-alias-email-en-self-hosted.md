---
title: "AliasVault : mots de passe et alias email en self-hosted"
slug: "aliasvault-mots-de-passe-et-alias-email-en-self-hosted"
date: 2026-11-11T18:52:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Outil open-source MIT combinant gestion de mots de passe, alias email et serveur mail intégré, pensé pour un usage self-hosted."
tags:
  - self-hosted
  - security
  - email
  - open-source
  - automation
series:
  - Veille techno
series_order: 165
showTableOfContents: true
---

## Introduction

La gestion des identités numériques reste un sujet sous-estimé, y compris dans les équipes techniques. Entre les comptes de service, les environnements de test et les inscriptions à des services SaaS, on accumule des credentials souvent mal gérés. AliasVault propose une approche intéressante en combinant plusieurs briques dans un seul outil open-source.

## Ce que propose AliasVault

AliasVault est un outil open-source sous licence MIT qui regroupe trois fonctions :

- **Gestion de mots de passe** avec chiffrement de bout en bout
- **Génération d'alias email** : chaque service obtient une adresse unique, ce qui isole les identités
- **Serveur mail intégré** : pas besoin de s'appuyer sur Gmail, Fastmail ou un autre tiers pour recevoir les emails

L'outil est conçu pour être **self-hosted**, ce qui garantit un contrôle total sur les données. Aucune dépendance à une infrastructure externe pour le stockage ou le transit des emails.

## Mon avis

Ce qui retient mon attention, c'est le potentiel d'**automatisation** que ce type d'outil peut offrir dans un contexte DevOps ou Platform Engineering.

Aujourd'hui, créer des comptes techniques ou des identités jetables pour des pipelines CI/CD, des environnements éphémères ou des tests d'intégration implique souvent du bricolage : boîtes mail partagées, alias manuels, catch-all sur un domaine dédié. C'est fragile et ça scale mal.

Un outil self-hosted capable de **générer à la volée un couple alias email + mot de passe**, avec un serveur mail intégré pour recevoir les confirmations, ça pourrait simplifier des workflows entiers. La question clé est de savoir si AliasVault expose une **API suffisamment complète** pour s'intégrer dans des pipelines automatisés — provisioning de comptes, rotation de credentials, nettoyage d'identités éphémères.

La licence MIT lève les freins juridiques pour une adoption en entreprise. Le chiffrement E2E est un bon point pour les équipes sécu. Reste à évaluer la maturité du projet et la robustesse du serveur mail embarqué pour un usage en production.

À surveiller de près si vous cherchez à industrialiser la gestion d'identités techniques.

🔗 https://www.aliasvault.net/
