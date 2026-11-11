---
title: "AWS ACK en GA : piloter RDS, Lambda, KMS depuis Kubernetes"
slug: "aws-ack-en-ga-piloter-rds-lambda-kms-depuis-kubernetes"
date: 2026-11-11T18:11:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "AWS ACK passe en GA pour RDS, Lambda, Step Functions, AMP et KMS, permettant de gérer ces services via CRDs Kubernetes."
tags:
  - kubernetes
  - cloud
  - gitops
  - automation
  - platform-engineering
  - database
series:
  - Veille techno
series_order: 124
showTableOfContents: true
---

## Contexte

AWS a annoncé le passage en disponibilité générale de ses Controllers for Kubernetes (ACK) pour cinq services : Amazon RDS, AWS Lambda, AWS Step Functions, Amazon Managed Service for Prometheus et AWS KMS. Une étape qui mérite qu'on s'y arrête, surtout pour les équipes qui cherchent à rationaliser leur outillage cloud.

## Ce que permet ACK

ACK repose sur le pattern des Custom Resource Definitions (CRDs) Kubernetes. Concrètement :

- Tu définis une ressource AWS (ex. une instance RDS) sous forme de manifeste YAML.
- Le controller ACK associé surveille cet objet et réconcilie l'état réel AWS avec l'état déclaré.
- L'ensemble s'intègre naturellement dans un workflow GitOps — ArgoCD, Flux, peu importe.

Les cinq services en GA couvrent des besoins larges : bases de données relationnelles (`RDS`), fonctions serverless (`Lambda`), orchestration (`Step Functions`), observabilité (`AMP`) et gestion de clés (`KMS`).

## Analyse

L'automatisation des ressources cloud a longtemps reposé sur des outils extérieurs au cluster : Terraform, CDK, CloudFormation, ou des scripts maison collés ensemble. ACK propose une approche différente — pas nécessairement meilleure dans tous les cas, mais cohérente avec une philosophie précise : **tout réconcilier depuis Kubernetes**.

Pour une équipe plateforme déjà investie dans l'écosystème Kubernetes, l'intérêt est réel. Moins d'interfaces à maintenir, un seul plan de contrôle, une surface GitOps unifiée. Le GA de `RDS` et `KMS` notamment ouvre des scénarios concrets : provisionner une base de données ou gérer des clés de chiffrement directement depuis un pipeline de déploiement, sans passer par un outil tiers.

La question n'est pas de savoir si ACK remplace Terraform — ce n'est pas son objectif. C'est plutôt de savoir si la granularité de contrôle qu'il offre correspond à votre contexte. Pour des équipes qui veulent réduire la fragmentation et centraliser l'automatisation autour de Kubernetes, c'est une piste sérieuse à évaluer.

## Source

https://aws.amazon.com/about-aws/whats-new/2022/09/aws-controllers-kubernetes-ack-rds-lambda-step-functions-prometheus-kms/
