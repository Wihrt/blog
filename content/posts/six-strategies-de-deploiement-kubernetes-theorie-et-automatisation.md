---
title: "Six stratégies de déploiement Kubernetes, théorie et automatisation"
slug: "six-strategies-de-deploiement-kubernetes-theorie-et-automatisation"
date: 2026-11-11T18:35:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Panorama des stratégies de déploiement K8s et réflexion sur l'automatisation de leur exécution en production."
tags:
  - kubernetes
  - devops
  - platform-engineering
  - gitops
series:
  - Veille techno
series_order: 148
showTableOfContents: true
---

## Contexte

Déployer sur Kubernetes ne se résume pas à `kubectl apply`. Le choix de la stratégie de déploiement a un impact direct sur la disponibilité des services, la sécurité des mises en production et la capacité à rollback rapidement. C'est un sujet structurant pour toute équipe qui opère des workloads en production.

## Ce que couvre l'article

L'article de Devtron passe en revue six stratégies :

- **Recreate** : arrêt total puis redémarrage. Simple, mais implique une indisponibilité.
- **Rolling Update** : remplacement progressif des pods. Le défaut Kubernetes, bon équilibre coût/risque.
- **Blue/Green** : deux environnements en parallèle, bascule instantanée du trafic. Coûteux en ressources.
- **Canary** : exposition progressive à un sous-ensemble d'utilisateurs. Utile pour valider avant un rollout complet.
- **A/B Testing** : routage ciblé selon des critères utilisateurs. Nécessite une infrastructure de routage adaptée.
- **Shadow** : le trafic réel est dupliqué vers une version parallèle sans impact utilisateur. Puissant pour tester en conditions réelles.

L'article souligne que le choix dépend de la tolérance à l'indisponibilité, des exigences de sécurité en production et des capacités de l'infrastructure. Devtron est présenté comme un outil pour simplifier l'implémentation de ces stratégies.

## Avis

L'article lui-même est une bonne synthèse, sans surprise pour qui travaille sur Kubernetes depuis quelques années. Ce qui est plus intéressant, c'est le signal qu'il porte : **l'automatisation de l'exécution des stratégies de déploiement reste un vrai sujet opérationnel**.

On a souvent des équipes qui connaissent les stratégies en théorie mais qui les implémentent manuellement ou via des scripts fragiles. C'est là que des outils comme Devtron, Argo Rollouts ou Flagger ont un rôle concret à jouer — pas pour décider de la stratégie, mais pour en fiabiliser l'exécution et réduire la charge opérationnelle.

La nuance importante : **automatiser sans comprendre, c'est juste déplacer le risque**. Un Canary mal configuré ou un Shadow deployment qui sature un backend, ça arrive. L'outil doit venir après la maîtrise du concept, pas à la place.

Pour une équipe Platform Engineering, l'enjeu est de proposer ces stratégies comme des primitives self-service, documentées et bornées. Moins de ticket ops, plus de guardrails.

## Source

https://devtron.ai/blog/top-6-kubernetes-deployment-strategies/
