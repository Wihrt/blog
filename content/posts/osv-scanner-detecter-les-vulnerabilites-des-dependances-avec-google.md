---
title: "OSV-Scanner : détecter les vulnérabilités des dépendances avec Google"
slug: "osv-scanner-detecter-les-vulnerabilites-des-dependances-avec-google"
date: 2026-11-11T18:20:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "OSV-Scanner scanne lockfiles, SBOM, images Docker et repos Git via la base OSV pour automatiser la détection de vulnérabilités."
tags:
  - security
  - docker
  - ci-cd
  - open-source
  - devops
series:
  - Veille techno
series_order: 133
showTableOfContents: true
---

## Introduction

Détecter les vulnérabilités dans ses dépendances n'est plus optionnel. Mais entre les outils qui génèrent du bruit, ceux qui demandent du glue code et ceux qui reposent sur des bases propriétaires, trouver la bonne brique à intégrer dans une pipeline reste un vrai sujet. **OSV-Scanner** de Google propose une approche intéressante.

## Ce que fait OSV-Scanner

OSV-Scanner est le frontend officiel de la base [OSV](https://osv.dev/) (Open Source Vulnerabilities), maintenue par Google. Son rôle : prendre en entrée une liste de dépendances — via des **lockfiles**, des **SBOM**, des **images Docker** ou directement des **repos Git** — et la croiser avec les vulnérabilités référencées dans la base.

La particularité du format OSV est qu'il stocke les informations de versions affectées de manière **non ambiguë et machine-readable**. Pas de plages floues, pas d'interprétation nécessaire : le mapping entre un package et ses vulnérabilités est précis. C'est un format ouvert, adopté par plusieurs écosystèmes (Go, npm, PyPI, crates.io, etc.).

## Pourquoi c'est pertinent pour une équipe Platform/DevOps

L'enjeu aujourd'hui n'est plus de convaincre qu'il faut scanner. C'est d'**industrialiser le scan** sans multiplier les outils ad hoc et le code de liaison.

OSV-Scanner a plusieurs atouts concrets sur ce terrain :

- **Format standardisé** : le format OSV est exploitable par d'autres outils en aval, ce qui facilite l'automatisation de bout en bout — alerting, ticketing, policies as code.
- **Support natif Docker et Git** : pas besoin de scripts intermédiaires pour extraire les dépendances d'une image ou d'un dépôt.
- **Open source et maintenu** : le projet est actif, soutenu par Google, avec une communauté qui contribue.

Dans un contexte où on cherche à réduire la maintenance des chaînes de sécurité, un outil qui parle un format ouvert et qui s'intègre sans adaptation est un gain de temps réel. Comparé à des outils comme `trivy` ou `grype`, OSV-Scanner ne les remplace pas forcément — mais il peut compléter une stratégie multi-scanner avec une source de données différente et un format interopérable.

À évaluer sérieusement si vous cherchez à **rationaliser votre outillage de scan de vulnérabilités** dans vos pipelines CI/CD.

🔗 [OSV-Scanner sur GitHub](https://github.com/google/osv-scanner)
