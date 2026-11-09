---
title: "mirrord : rediriger le trafic Kubernetes vers son dev local"
slug: "mirrord-rediriger-le-trafic-kubernetes-vers-son-dev-local"
date: 2026-11-09T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "mirrord capture le trafic d'un pod Kubernetes et le redirige en local pour déboguer sans modifier le workload cible."
tags:
  - kubernetes
  - devops
  - cli
  - security
  - platform-engineering
series:
  - Veille techno
series_order: 113
showTableOfContents: true
---

## Introduction

Réproduire un bug en local qui ne se manifeste qu'avec le trafic réel d'un cluster Kubernetes, c'est un problème classique et chronophage. mirrord propose une approche directe : capturer le trafic d'un pod existant et le rediriger vers l'environnement de développement local, sans modifier le workload en place.

## Ce que fait mirrord

mirrord fonctionne en déployant un pod privilégié sur le même nœud que le pod cible. Ce pod entre dans le namespace réseau et de processus du pod sélectionné pour en capturer le trafic entrant. Ce trafic est ensuite redirigé vers l'environnement local du développeur.

Points clés :

- Disponible en **extension VS Code** et en **CLI**
- Ne nécessite pas de modifier le pod cible
- Fonctionne au niveau du namespace Linux (`netns`, `pidns`)
- Pensé pour réduire la boucle de feedback entre dev local et cluster réel

## Analyse

L'outillage autour du développement Kubernetes reste un point de friction réel pour beaucoup d'équipes. Les approches habituelles — logs, port-forward, environnements de staging partiels — ont leurs limites dès qu'on cherche à reproduire un comportement lié au trafic réel.

mirrord s'inscrit dans une logique d'automatisation de la boucle dev : moins d'étapes manuelles pour obtenir un contexte d'exécution fidèle. C'est cohérent avec l'objectif de réduire la friction opérationnelle sans alourdir les processus.

Cela dit, le modèle implique un **pod privilégié en production** avec accès aux namespaces système d'autres pods. C'est un vecteur de risque qui mérite une évaluation sérieuse : politique de sécurité des pods, RBAC, périmètre d'usage autorisé. Avant tout déploiement, la question du cloisonnement et des droits accordés doit être tranchée clairement avec les équipes sécurité.

L'outil a du sens dans des contextes où l'environnement de staging est difficile à maintenir fidèle à la production. Il ne remplace pas une bonne stratégie d'observabilité, mais peut compléter utilement la boîte à outils.

## Source

https://github.com/metalbear-co/mirrord
