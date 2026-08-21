---
title: "fnox : centraliser le chiffrement et l'accès à vos secrets"
slug: "fnox-gestion-secrets"
date: 2025-11-10T08:00:03+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Chiffrement via age ou les KMS cloud, intégration avec AWS Secrets Manager, Azure Key Vault, 1Password et Bitwarden."
tags:
  - security
  - cli
  - cloud
  - devops
series:
  - Veille techno
series_order: 34
showTableOfContents: true
---

## Introduction

Dans le monde actuel, la gestion des secrets est cruciale pour assurer la sécurité des applications. J'ai découvert "fnoxis", un outil de gestion de secrets qui prend en charge le stockage chiffré dans Git ainsi que chez des fournisseurs de cloud. Pour ceux qui, comme moi, recherchent une solution robuste, fnoxis semble être une option prometteuse.

## Résumé

Fnoxis permet un chiffrement via des solutions comme age, AWS KMS, Azure KMS et GCP KMS. Il s'intègre également avec des gestionnaires de secrets cloud tels qu'AWS Secrets Manager, Azure Key Vault, et des gestionnaires de mots de passe comme 1Password et Bitwarden. Avec une intégration shell pour le chargement automatique des secrets, fnoxis propose aussi un support multi-environnement basé sur des profils.

## Utilité Pros Tech

Avoir un outil comme fnoxis simplifie énormément la gestion des secrets pour les développeurs. En tant que professionnel de la tech, l'idée de pouvoir chiffrer des secrets et les commettre dans le contrôle de version ou les référencer depuis des fournisseurs distants est extrêmement pratique. De plus, l'utilisation d'un format simple comme TOML pour la configuration facilite l'adoption par les équipes.

## Mon Expérience

En utilisant fnoxis dans différents environnements (développement, mise en scène et production), j'ai pu explorer la flexibilité offerte par cet outil. L'interface est intuitive et la possibilité de mixer diverses approches de gestion selon les besoins des environnements est un véritable atout pour mon flux de travail.

## Conclusion

Pour toute personne impliquée dans le développement et la sécurité, fnoxis offre une solution viable pour la gestion des secrets. Je recommande cet outil à quiconque cherche à optimiser la sécurité tout en simplifiant le processus dans un cadre multi-environnement. Plus de détails sont disponibles dans [l'article complet](https://api.daily.dev/r/Mg0pgkamt).
