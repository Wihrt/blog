---
title: "Vals-Operator : secrets Kubernetes multi-backend synchronisés"
slug: "vals-operator-secrets-kubernetes-multi-backend-synchronises"
date: 2026-09-11T13:10:49+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Un opérateur Kubernetes qui synchronise des secrets depuis Vault, AWS, GCP ou Azure sans dépendance à un backend unique."
tags:
  - kubernetes
  - security
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 83
showTableOfContents: true
---

## Introduction

La gestion des secrets dans Kubernetes est un sujet récurrent, et les solutions ne manquent pas. `vals-operator` s'inscrit dans cette catégorie, mais avec un angle différent : la généricité des backends supportés. Un point qui mérite qu'on s'y arrête.

## Ce que fait Vals-Operator

`vals-operator` est un opérateur Kubernetes qui synchronise des secrets depuis n'importe quel store supporté par la librairie `vals`. Concrètement, ça couvre :

- **HashiCorp Vault**
- **AWS Secrets Manager**
- **GCP Secret Manager**
- **Azure Key Vault**
- Et d'autres backends compatibles `vals`

L'opérateur fonctionne sur un cycle de réconciliation configurable : à chaque période définie, il vérifie l'état du secret côté backend et met à jour l'objet Kubernetes correspondant si nécessaire. Le code source s'appuie sur le projet `secrets-manager`, ce qui donne une base éprouvée.

Le fonctionnement est donc proche de ce que font d'autres opérateurs du marché, mais avec une couche d'abstraction qui permet de ne pas se lier à un seul fournisseur.

## Analyse

L'intérêt principal de cet outil, c'est précisément ce que la plupart des solutions similaires n'offrent pas : **l'indépendance vis-à-vis d'un backend spécifique**. Dans des environnements multi-cloud, ou dans des organisations où chaque équipe a hérité d'un outil différent, écrire une couche de synchronisation cohérente est souvent source de dette technique.

Avoir un opérateur qui abstrait cette complexité réduit la quantité de colle à maintenir. Moins de scripts ad hoc, moins de CronJobs maison, moins de surface d'erreur. C'est exactement le genre de décision qui s'inscrit dans une logique de Platform Engineering : standardiser les patterns d'intégration pour que les équipes produit n'aient pas à réinventer la roue.

Le cycle de réconciliation est aussi un point fort : les secrets restent à jour de façon passive, sans dépendance à un pipeline CI/CD ou à une intervention humaine. Dans un contexte de rotation régulière des secrets, c'est un comportement attendu.

À évaluer bien sûr selon le contexte : la maturité du projet, la fréquence de réconciliation, et les éventuelles implications en termes de permissions RBAC côté cluster.

## Source

https://golangexample.com/kubernetes-operator-to-sync-secrets-between-different-secret-backends-and-kubernetes/
