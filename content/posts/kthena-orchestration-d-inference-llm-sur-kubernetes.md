---
title: "Kthena : orchestration d'inférence LLM sur Kubernetes"
slug: "kthena-orchestration-d-inference-llm-sur-kubernetes"
date: 2026-11-11T19:14:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Sous-projet de Volcano (CNCF), Kthena automatise scheduling GPU, routage et scaling pour l'inférence LLM en production."
tags:
  - kubernetes
  - ai
  - platform-engineering
  - open-source
series:
  - Veille techno
series_order: 187
showTableOfContents: true
---

## Introduction

Faire tourner de l'inférence LLM en production sur Kubernetes reste un exercice complexe. Entre le placement GPU, le scaling, le routage entre instances et la gestion multi-modèles, les équipes plateforme passent beaucoup de temps à assembler des solutions maison. Kthena, nouveau sous-projet open source de Volcano (CNCF), propose d'intégrer cette intelligence directement dans l'orchestrateur.

## Ce que propose Kthena

Kthena cible les problèmes concrets de l'inférence LLM en production :

- **Utilisation GPU/NPU trop basse** : scheduling topology-aware et gang scheduling pour optimiser le placement des workloads sur les accélérateurs disponibles.
- **Compromis latence/débit** : routage intelligent et disaggregation Prefill-Decode pour séparer les phases de calcul et mieux paralléliser.
- **Gestion multi-modèles** : un controller manager et un routeur haute performance qui supportent plusieurs engines d'inférence — `vLLM`, `SGLang`, `Triton`.
- **KV Cache-aware scheduling** : le scheduler prend en compte l'état du cache KV pour router les requêtes vers les instances les plus pertinentes.
- **Autoscaling** intégré.

Les benchmarks annoncés sont significatifs : **x2.73 en throughput** et **-73.5% sur le Time To First Token** par rapport à du routage aléatoire. Le projet est soutenu par Huawei Cloud, China Telecom, DaoCloud et d'autres partenaires industriels.

## Avis

L'intérêt principal de Kthena, c'est l'automatisation. Aujourd'hui, proposer du LLM-as-a-Service sur une plateforme Kubernetes interne, ça implique de câbler soi-même le scaling, le routage, le placement GPU. Chaque engine d'inférence a ses spécificités, et le tout finit souvent en scripts fragiles.

Kthena remonte cette logique au niveau de l'orchestrateur, ce qui est la bonne approche pour des équipes plateforme. Le fait que le projet s'intègre dans Volcano, déjà incubé à la CNCF et reconnu pour le batch scheduling, lui donne une base solide.

Les questions ouvertes restent classiques pour un projet à ce stade : quelle maturité réelle hors des environnements Huawei ? Quelle communauté au-delà des partenaires fondateurs ? Et surtout, comment ça se comporte face à des patterns de trafic réels, pas juste des benchmarks synthétiques. À suivre de près pour quiconque gère de l'inférence LLM sur Kubernetes.

[Source : CNCF Blog](https://www.cncf.io/blog/2026/01/28/introducing-kthena-llm-inference-for-the-cloud-native-era/)
