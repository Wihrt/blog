---
title: "Packer 1.16 : provenance SLSA native"
slug: "packer-1-16-provenance-slsa-native"
date: 2026-11-26T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Packer 1.16 génère et signe des attestations SLSA pour vos images machine, sans outillage externe."
tags:
  - security
  - devops
  - ci-cd
  - automation
  - cloud
series:
  - Veille techno
series_order: 198
showTableOfContents: true
---

## Packer v1.16.0 : la provenance SLSA sans tooling externe

HashiCorp continue d'étoffer Packer avec une fonctionnalité qui touche directement à la chaîne d'approvisionnement logicielle : la génération native d'attestations de provenance SLSA pour les images machine.

## Ce que change cette version

La version 1.16.0 introduit un nouveau post-processor "provenance" capable de produire des statements in-toto conformes au prédicat SLSA Provenance v1. Ces attestations capturent :

- le commit Git et le repository source

- la ref utilisée pour le build

- le pipeline CI d'origine

- les timestamps de build

Quatre modes de signature sont disponibles, du plus simple au plus robuste : JSON non signé, clés PEM locales, intégration cloud KMS/Vault, et enfin Sigstore Fulcio avec transparence via Rekor. Selon la configuration choisie, la sortie de Packer peut atteindre les niveaux SLSA L1 jusqu'à un pattern compatible L3, sachant que la conformité L3 complète dépend aussi du hardening de la plateforme sous-jacente.

Cette release ajoute également quelques améliorations HCL2 plus discrètes, comme le meta-argument `continue_on_error` et de nouvelles fonctions de parsing de timestamps.

## Mon avis

Ce qui rend cette fonctionnalité intéressante, c'est qu'elle est entièrement opt-in : les templates existants n'ont rien à changer, et l'équipe peut l'activer progressivement, image par image, sans big-bang. Dans une logique d'automatisation, c'est exactement le type d'ajout qu'on cherche : une brique qui remplace un outillage supply-chain qu'on devait auparavant assembler soi-même (signature, vérification, transparence log), tout en s'intégrant directement dans un pipeline de build d'images déjà existant.

Pour une équipe Platform Engineering, ça veut dire moins de scripts custom autour de la génération d'attestations, et une traçabilité renforcée sur l'origine des images en circulation. Ça ne remplace pas les mécanismes natifs cloud comme AMI Watermarks ou l'attestation NitroTPM chez AWS, mais ça complète bien ce type d'approche, notamment pour les environnements multi-cloud où on veut une méthode uniforme de provenance indépendante du fournisseur.

À tester sérieusement si votre pipeline de build d'images gagnerait en traçabilité sans ajouter une couche d'outillage supplémentaire.

Source : https://www.infoq.com/news/2026/09/hashicorp-packer-verification
