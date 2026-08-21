---
title: "Suivre automatiquement ses coûts GCP avec Apache Airflow"
slug: "suivi-couts-gcp-airflow"
date: 2025-11-13T08:00:00+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Export quotidien de la facturation GCP vers BigQuery, agrégation orchestrée par Airflow et rapport de coûts envoyé sur Slack."
tags:
  - cloud
  - automation
  - monitoring
  - python
series:
  - Veille techno
series_order: 36
showTableOfContents: true
---

## Introduction

Quand on pilote des projets cloud à grande échelle, une bonne visibilité sur les coûts est indispensable. En tant que développeur ayant travaillé sur des infrastructures Kubernetes et CI/CD, j’ai souvent vu des équipes surprises par des factures GCP plus élevées que prévu. Récemment, j’ai testé une solution d’automatisation partagée dans un article que j’ai lu, qui m’a réellement convaincu.

## Résumé de l’article

L’article présente une solution pour construire un système de notification automatisée des coûts GCP à l’aide d’Apache Airflow. L’approche repose sur l’export quotidien des données de facturation GCP dans BigQuery. Ensuite, Airflow orchestre un workflow qui interroge ces données, agrège les coûts (y compris les taxes) et envoie un rapport formaté sur Slack. Le but ? Offrir à l’équipe une vision journalière détaillée des dépenses, service par service, pour prévenir les dérapages budgétaires.

## Pourquoi c’est utile pour les pros tech

### Anticiper les dépassements budgétaires

Dans un environnement cloud, les coûts peuvent vite grimper, surtout avec des clusters Kubernetes mal configurés ou une CI/CD qui tourne en boucle. Avoir un suivi automatisé permet de repérer immédiatement les anomalies.

### Renforcer la culture DevOps

Le monitoring des coûts complète naturellement les pratiques DevOps : monitorer l’usage de l’infra ne suffit pas, il faut aussi monitorer les dépenses. Ce système s’intègre bien dans une logique d’amélioration continue.

### Communication simplifiée via Slack

Recevoir le rapport directement sur Slack facilite le partage d’infos avec l’équipe. Plus besoin de plonger dans la console GCP tous les matins : tout arrive dans le bon canal, avec les bons filtres.

## Mon retour d’expérience

Après lecture, j’ai moi-même testé un prototype basé sur cet article. En quelques heures, j’ai pu connecter mon export BigQuery à Airflow via un DAG programmé quotidiennement. Le plus long a été le formatage du message Slack, mais une fois intégré, c’est un vrai game changer : chaque matin, je vois en un clin d’œil les services GCP les plus coûteux. Autre avantage : ça m’aide à identifier les jobs CI/CD oubliés ou à revoir la configuration de certains pods Kubernetes trop gourmands.

## Conclusion

Cette approche d’automatisation des notifications de coûts GCP est simple à implémenter et apporte un vrai plus aux pratiques DevOps. Elle favorise la réactivité, la collaboration et la maîtrise des budgets cloud. Pour découvrir le guide complet et implémenter la solution, voici [l’article original](https://api.daily.dev/r/XyvjHgUL5).
