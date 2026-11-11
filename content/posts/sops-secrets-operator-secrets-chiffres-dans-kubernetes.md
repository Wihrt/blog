---
title: "SOPS Secrets Operator : secrets chiffrés dans Kubernetes"
slug: "sops-secrets-operator-secrets-chiffres-dans-kubernetes"
date: 2026-11-11T19:05:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Un opérateur Kubernetes qui déchiffre des secrets SOPS depuis Git pour un workflow GitOps sans Vault."
tags:
  - kubernetes
  - gitops
  - security
  - helm
  - self-hosted
series:
  - Veille techno
series_order: 178
showTableOfContents: true
---

## Introduction

La gestion des secrets dans un workflow GitOps reste un sujet épineux. Stocker des secrets en clair dans Git est évidemment exclu, mais les alternatives ajoutent souvent de la complexité opérationnelle. Le **SOPS Secrets Operator** propose une approche pragmatique pour réconcilier chiffrement, Kubernetes et déploiement continu.

## Ce que fait le SOPS Secrets Operator

Ce projet open source est un opérateur Kubernetes qui s'inspire à la fois de **Bitnami SealedSecrets** et de **Mozilla SOPS**. Le principe : on définit des Custom Resources de type `SopsSecrets` contenant des secrets chiffrés. L'opérateur se charge de les déchiffrer et de créer les `Secrets` Kubernetes correspondants dans le cluster.

Points clés :

- **Chiffrement multi-cloud** : supporte les clés KMS sur AWS, GCP, Azure, ainsi que PGP pour les environnements on-prem.
- **Déploiement via Helm** et intégration native avec **Flux** pour le GitOps.
- **Annotations et labels personnalisables** sur les secrets générés, ce qui permet notamment de les exposer comme **Jenkins Credentials** sans étape manuelle.
- Les secrets chiffrés vivent dans le dépôt Git aux côtés des manifestes, versionnés et auditables.

## Mon avis

L'intérêt principal de cet opérateur, c'est qu'il ne réinvente pas la roue. Il assemble des briques éprouvées — SOPS pour le chiffrement, un opérateur Kubernetes pour la réconciliation, Flux pour le déploiement — dans un workflow cohérent.

Pour des équipes qui cherchent à **automatiser la gestion des secrets en GitOps sans déployer une infrastructure lourde type HashiCorp Vault**, c'est une option sérieuse. Vault reste pertinent pour des besoins avancés (secrets dynamiques, rotation automatique, lease management), mais pour du secret statique versionné dans Git, un opérateur SOPS couvre le besoin avec beaucoup moins de friction opérationnelle.

Le détail de l'intégration Jenkins Credentials via annotations montre que le projet est pensé pour des cas d'usage réels, pas juste pour une démo. C'est le genre de signal qui compte.

Les points à évaluer avant adoption : la **maturité du projet** (fréquence des releases, réactivité sur les issues), la gestion de la **rotation des clés KMS**, et le comportement en cas de drift entre le CR chiffré et le secret déchiffré dans le cluster.

Dans une logique d'automatisation progressive, c'est typiquement l'outil qu'on intègre tôt dans la chaîne pour éviter les "je te file le secret sur Slack".

🔗 **Source** : [https://github.com/isindir/sops-secrets-operator](https://github.com/isindir/sops-secrets-operator)
