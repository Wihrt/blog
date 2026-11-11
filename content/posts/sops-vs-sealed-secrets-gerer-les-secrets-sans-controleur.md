---
title: "SOPS vs Sealed Secrets : gérer les secrets sans contrôleur"
slug: "sops-vs-sealed-secrets-gerer-les-secrets-sans-controleur"
date: 2026-11-11T18:03:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "SOPS chiffre les secrets Kubernetes sans contrôleur dans le cluster, une alternative à Sealed Secrets pour le GitOps."
tags:
  - kubernetes
  - gitops
  - security
  - helm
  - devops
series:
  - Veille techno
series_order: 116
showTableOfContents: true
---

## Contexte

La gestion des secrets dans un contexte Kubernetes/GitOps reste un problème récurrent. Sealed Secrets est souvent la première réponse, mais elle n'est pas sans contraintes. SOPS se présente comme une alternative sérieuse à connaître.

## Ce que fait SOPS

SOPS (Secrets OPerationS) est un binaire qui chiffre les **valeurs** d'un fichier de configuration, tout en laissant les **clés** en clair. Résultat : le fichier reste lisible structurellement (YAML, JSON, ENV...), mais les données sensibles sont chiffrées.

Les points clés :

- Compatible avec plusieurs backends de chiffrement : `AWS KMS`, `GCP KMS`, `Azure Key Vault`, ou `Age` pour une approche locale/légère.
- Le fichier chiffré peut être versionné directement dans Git, ce qui s'intègre naturellement dans un workflow GitOps.
- Pas de contrôleur à déployer dans le cluster — le seul prérequis est d'installer le binaire SOPS et Age en local (ou sur WSL).
- Fonctionne avec Helm via le plugin `helm-secrets`.

## Analyse

Si on cherche à réduire la surface de dépendances dans un cluster Kubernetes, SOPS est cohérent avec cet objectif. Sealed Secrets nécessite un contrôleur actif dans le cluster, ce qui représente un composant supplémentaire à maintenir, superviser, et mettre à jour. En production, chaque composant de plus, c'est une source potentielle de friction opérationnelle.

SOPS déplace la complexité côté outillage de développement et de CI/CD, ce qui est souvent plus facile à standardiser et à auditer dans une équipe. La clé privée Age ou les accès KMS peuvent être gérés via les mécanismes d'IAM existants, sans introduire de nouveau périmètre de sécurité dans le cluster lui-même.

Cela dit, SOPS ne résout pas la question de la distribution des clés — il la repose différemment. Il faut une stratégie claire : qui a accès à quoi, comment les clés sont rotées, comment le pipeline CI/CD s'authentifie. Ce n'est pas une complexité évitable, juste mieux positionnée.

Pour des équipes orientées automatisation et GitOps, c'est une approche qui mérite d'être évaluée sérieusement face à des solutions comme External Secrets Operator.

## Source

https://itnext.io/goodbye-sealed-secrets-hello-sops-3ee6a92662bb?source=rss----5b301f10ddcd---4
