---
title: "Tofu Controller : Terraform/OpenTofu en GitOps avec Flux"
slug: "tofu-controller-terraform-opentofu-en-gitops-avec-flux"
date: 2026-11-11T19:03:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Un contrôleur Kubernetes qui intègre Terraform et OpenTofu à Flux, avec adoption progressive du GitOps."
tags:
  - gitops
  - terraform
  - kubernetes
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 176
showTableOfContents: true
---

## Introduction

Gérer du Terraform ou de l'OpenTofu via des pipelines CI, ça fonctionne, mais ça atteint ses limites quand on veut un vrai modèle de réconciliation continue. Le **Tofu Controller** propose une approche différente : intégrer la gestion IaC directement dans Flux, côté Kubernetes.

## Ce que propose le Tofu Controller

Le Tofu Controller est un contrôleur Kubernetes qui s'intègre nativement à **Flux CD** pour gérer des ressources **Terraform** et **OpenTofu** en mode GitOps. Il ne se limite pas à un seul modèle d'utilisation. Quatre approches sont proposées :

- **GitOps Automation** : réconciliation complète et automatique depuis le dépôt Git.
- **Hybrid GitOps** : un mix entre approbation manuelle et automatisation.
- **State Enforcement** : le contrôleur s'assure que le state réel correspond à ce qui est déclaré.
- **Drift Detection** : détection passive des écarts sans action corrective automatique.

Cette granularité permet une adoption progressive, ce qui est rarement le cas avec les outils concurrents.

## Mon avis

L'intérêt principal du Tofu Controller, c'est cette **logique incrémentale**. Sur le terrain, les équipes qui gèrent de l'IaC ont souvent du Terraform legacy, des states partagés, des workflows de `plan`/`apply` manuels bien ancrés. Imposer un passage brutal au GitOps complet, c'est le meilleur moyen de ne jamais y arriver.

Pouvoir démarrer par de la **drift detection** — sans toucher aux workflows existants — puis monter en maturité vers du state enforcement ou de l'automation complète, c'est une approche réaliste.

Le point à ne pas éluder : ce modèle **couple le lifecycle de l'IaC à celui du cluster Kubernetes**. Si votre cluster tombe, votre capacité à gérer l'infra tombe avec. C'est un choix d'architecture qui se défend dans un contexte multi-cluster ou quand Kubernetes est déjà le plan de contrôle central, mais qui mérite d'être explicitement assumé par l'équipe plateforme.

Pour les équipes déjà sur Flux et qui cherchent à consolider leur outillage GitOps, c'est un candidat sérieux à évaluer.

🔗 **Source** : [https://github.com/flux-iac/tofu-controller](https://github.com/flux-iac/tofu-controller)
