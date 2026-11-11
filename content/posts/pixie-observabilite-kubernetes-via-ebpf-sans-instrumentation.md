---
title: "Pixie : observabilité Kubernetes via eBPF sans instrumentation"
slug: "pixie-observabilite-kubernetes-via-ebpf-sans-instrumentation"
date: 2026-11-11T18:24:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Pixie collecte métriques, traces et logs Kubernetes via eBPF, sans modifier le code applicatif."
tags:
  - kubernetes
  - observability
  - monitoring
  - platform-engineering
  - open-source
series:
  - Veille techno
series_order: 137
showTableOfContents: true
---

## Introduction

L'observabilité dans un cluster Kubernetes reste un chantier permanent pour les équipes Platform Engineering. Entre la configuration des agents, l'instrumentation du code et la maintenance des pipelines de collecte, le coût opérationnel est souvent sous-estimé. Pixie propose une approche différente : collecter les données directement au niveau système, sans modifier les applications.

## Ce que fait Pixie

Pixie est un outil open-source d'observabilité conçu pour les environnements Kubernetes. Ses points clés :

- Utilise **eBPF** pour capturer les données au niveau du kernel Linux, sans instrumentation applicative.
- Collecte automatiquement des **métriques de performance**, des **traces réseau**, des **requêtes HTTP/gRPC/SQL** et des **logs**.
- S'intègre nativement dans Kubernetes, sans nécessiter de modification du code source des services.
- Propose une interface de requêtage via **PxL**, un langage inspiré de Pandas, pour explorer les données en temps réel.
- Disponible en open-source sur GitHub, avec une version managée via Pixie Cloud.

## Avis

L'axe qui retient l'attention ici, c'est l'automatisation de l'instrumentation. Dans la construction d'une Internal Developer Platform, chaque outil qui s'intègre sans friction réduit le coût d'adoption et limite la surface de configuration à maintenir.

Avec `eBPF`, Pixie contourne le problème classique de l'instrumentation : pas besoin de toucher aux Dockerfiles, pas de SDK à injecter, pas de sidecar à gérer pour chaque service. C'est un gain réel, surtout dans des environnements hétérogènes où les équipes applicatives ne sont pas toujours alignées sur les standards d'observabilité.

La vraie question est celle de la profondeur et de la maturité face à une stack plus établie comme **OpenTelemetry + Prometheus + Tempo**. Pixie semble plus adapté à un usage de diagnostic rapide et d'exploration qu'à un pipeline d'observabilité long terme. Les deux approches ne sont pas forcément exclusives.

À évaluer sérieusement si l'objectif est de réduire le temps d'onboarding à l'observabilité pour les équipes de développement.

## Source

https://github.com/pixie-io/pixie
