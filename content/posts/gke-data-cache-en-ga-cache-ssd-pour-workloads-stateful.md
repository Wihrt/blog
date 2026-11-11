---
title: "GKE Data Cache en GA : cache SSD pour workloads stateful"
slug: "gke-data-cache-en-ga-cache-ssd-pour-workloads-stateful"
date: 2026-11-11T19:08:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "GKE Data Cache passe en disponibilité générale : un cache SSD local pour accélérer les accès au stockage persistant sur GKE."
tags:
  - kubernetes
  - storage
  - platform-engineering
  - cloud
  - terraform
  - database
series:
  - Veille techno
series_order: 181
showTableOfContents: true
---

## Introduction

Google vient d'annoncer la disponibilité générale de **GKE Data Cache**, une fonctionnalité qui ajoute une couche de cache SSD local devant le stockage persistant sur Google Kubernetes Engine. Pour les équipes qui opèrent des workloads stateful sur GKE, c'est un levier de performance qui mérite d'être évalué.

## Ce que propose GKE Data Cache

Le principe est direct : les **SSD locaux** attachés aux nœuds GKE servent de cache en lecture pour les Persistent Volumes. Les bénéfices annoncés par Google :

- **Réduction de la latence de lecture** sur les accès au stockage persistant
- **Augmentation du nombre de transactions par seconde** (TPS)
- **Amélioration de l'efficacité globale** pour les applications de type bases de données, data warehouses ou plateformes analytiques

La configuration se fait au niveau du **cluster** et des **workloads**, sans modification du code applicatif. On reste dans du déclaratif côté infrastructure.

## Avis — un levier d'automatisation pour les équipes plateforme

Ce qui rend cette fonctionnalité pertinente au-delà du simple gain de performance, c'est son **modèle d'activation**. Le cache se configure côté infra — potentiellement dans un `StorageClass`, une config de node pool ou des paramètres de workload. Pour une équipe plateforme, ça signifie qu'on peut :

- L'intégrer dans un **module Terraform** ou un chart Helm comme paramètre exposé
- Offrir aux équipes produit un levier de performance **sans qu'elles aient à toucher leur application**
- Garder la **maîtrise côté plateforme** sur l'activation et le dimensionnement du cache

C'est exactement la logique qu'on cherche à renforcer en platform engineering : **réduire la surface de décision côté développeurs** sur les sujets infra, tout en leur donnant accès à des optimisations concrètes via des abstractions bien pensées.

Reste à valider en conditions réelles : quel impact sur le coût des nœuds avec SSD local, quel comportement en cas de rescheduling de pods, et surtout si le gain de latence justifie le surcoût par rapport à un simple passage en SSD persistant plus rapide (type `pd-ssd` ou `hyperdisk`).

Pour les équipes qui ont déjà des bases de données ou du Redis sur GKE avec des problèmes de latence I/O, c'est clairement un paramètre à tester.

**Source :** https://cloud.google.com/blog/products/containers-kubernetes/gke-data-cache-now-ga-accelerates-stateful-apps/
