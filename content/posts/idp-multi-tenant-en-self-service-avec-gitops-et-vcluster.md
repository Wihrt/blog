---
title: "IDP multi-tenant en self-service avec GitOps et vCluster"
slug: "idp-multi-tenant-en-self-service-avec-gitops-et-vcluster"
date: 2026-10-09T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Architecturer une IDP multi-tenant avec Kubernetes, ArgoCD et vCluster, en approche GitOps concrète."
tags:
  - kubernetes
  - gitops
  - argocd
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 94
showTableOfContents: true
---

## Construire une IDP multi-tenant en self-service avec GitOps et vCluster

Les Internal Developer Platforms (IDP) sont devenues un sujet central en platform engineering. Mais entre la théorie et une implémentation qui tient en production avec plusieurs équipes, il y a souvent un écart. Cet article tente de combler ce fossé avec une approche concrète.

## Ce que couvre l'article

L'auteur détaille comment architécturer une IDP multi-tenant en s'appuyant sur **Kubernetes**, **ArgoCD** et **vCluster**. Les points clés abordés :

- La distinction entre l'équipe plateforme (qui expose les abstractions) et l'équipe infrastructure managée (qui opère les clusters)
- Les différentes couches d'une IDP : de l'infra sous-jacente jusqu'à l'interface self-service exposée aux développeurs
- L'utilisation de `vCluster` pour créer des clusters virtuels isolés par tenant, sans multiplier les clusters physiques
- Un guide pratique de mise en place avec GitOps comme source de vérité

L'article inclut également la promotion d'un webinar avec démo technique, ce qui lui donne un angle pédagogique assumé.

## Avis

L'angle self-service est ce qui rend cette architecture intéressante. Une IDP qui oblige les développeurs à ouvrir un ticket pour chaque besoin d'environnement ne remplit pas vraiment son rôle. L'objectif est de réduire le temps entre une intention et son exécution — et c'est là que l'automatisation prend son sens.

`vCluster` comme couche d'isolation multi-tenant est un choix pertinent : on évite la lourdeur opérationnelle de clusters physiques dédiés par équipe, tout en maintenant une isolation correcte. Pour des équipes platform engineering qui cherchent à industrialiser sans exploser les coûts infra, c'est une piste à explorer sérieusement.

La vraie question reste la gestion des cas limites : quotas, network policies croisées, gestion des secrets par tenant, observabilité. C'est souvent là que les architectures IDP montrent leurs limites. L'article pose de bonnes bases mais l'implémentation en conditions réelles demandera des arbitrages supplémentaires.

Pour des équipes qui cherchent des outils pour automatiser et réduire la friction opérationnelle, cette stack mérite d'être évaluée.

## Source

https://itnext.io/how-to-build-a-multi-tenancy-internal-developer-platform-with-gitops-and-vcluster-d8f43bfb9c3d
