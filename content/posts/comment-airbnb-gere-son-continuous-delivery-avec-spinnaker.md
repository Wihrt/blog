---
title: "Comment Airbnb gère son continuous delivery avec Spinnaker"
slug: "comment-airbnb-gere-son-continuous-delivery-avec-spinnaker"
date: 2026-09-24T11:28:32+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Retour sur la migration d'Airbnb vers les microservices et l'adoption de Spinnaker pour le continuous delivery."
tags:
  - ci-cd
  - devops
  - platform-engineering
  - open-source
  - argocd
series:
  - Veille techno
series_order: 82
showTableOfContents: true
---

## Contexte

Les migrations de monolithe vers microservices sont souvent documentées côté architecture applicative. Moins souvent côté delivery. L'exemple d'Airbnb est intéressant précisément parce qu'il met le focus sur cette couche — comment on livre, pas seulement comment on construit.

## Ce que dit l'article

Airbnb a migré son application principale depuis un monolithe Ruby on Rails vers une architecture microservices. Face à la complexité croissante des déploiements, ils ont adopté **Spinnaker**, la plateforme de continuous delivery open source développée initialement chez Netflix puis contribuée avec Google.

Parmi les points clés :

- Spinnaker permet de gérer des pipelines de déploiement multi-environnements avec des stratégies avancées (canary, blue/green).
- L'article mentionne également des optimisations d'efficacité mémoire, avec une approche bottom-up légèrement plus compacte.
- Le choix d'un outil établi plutôt qu'une solution maison reflète une volonté de capitaliser sur des patterns éprouvés à l'échelle.

## Analyse

L'enjeu central dans ce type de migration, c'est l'automatisation du delivery. Pas l'automatisation pour le principe, mais celle qui permet aux équipes produit de livrer sans dépendre d'une expertise pipeline pointue à chaque déploiement.

Spinnaker répond à ça — mais il a un coût opérationnel réel. C'est un outil puissant, avec une courbe d'adoption non négligeable. Le choisir, c'est parier sur la standardisation et la robustesse plutôt que sur la légèreté.

Pour une équipe Platform Engineering, le message concret est le suivant : bien outiller le delivery, c'est un levier direct sur la vélocité des équipes produit. Un pipeline fragile ou trop manuel, c'est de la dette opérationnelle qui s'accumule silencieusement. L'adoption d'outils comme Spinnaker — ou d'alternatives comme Argo CD, Flux selon le contexte — doit être un choix délibéré, pas un bricolage progressif.

La tendance de fond reste la même : chercher des outils qui absorbent la complexité du déploiement pour que les équipes puissent se concentrer sur ce qui a de la valeur.

## Source

https://quastor.substack.com/p/how-airbnb-does-continuous-delivery
