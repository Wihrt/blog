---
title: "1000 sites WordPress : réduire la facture cloud à 30 000 $/mois"
slug: "1000-sites-wordpress-reduire-la-facture-cloud-a-30-000-mois"
date: 2026-10-16T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Cas concret d'une migration Next.js pour rationaliser une infra WordPress de 25 serveurs et réduire les coûts cloud."
tags:
  - cloud
  - devops
  - platform-engineering
  - automation
series:
  - Veille techno
series_order: 99
showTableOfContents: true
---

## Contexte

Gérer plus de 1 000 sites WordPress sur 25 serveurs, c'est une réalité pour certaines agences ou éditeurs. Quand la facture cloud atteint 30 000 $ par mois uniquement en stockage, la question ne se pose plus : il faut revoir l'architecture. Ce cas documenté par The Software House illustre bien les enjeux d'une migration technique sous contrainte.

## Ce que dit l'article

Une entreprise basée au Royaume-Uni atteignait 30 000 $ mensuels en coûts de stockage cloud, avec une infrastructure de 25 serveurs hébergeant plus de 1 000 sites WordPress. Une augmentation de trafic a mis en évidence les limites de parties du système non maîtrisées en interne. The Software House est intervenu pour livrer une nouvelle application — basée sur Next.js — dans un délai contraint. L'objectif : rationaliser l'infrastructure, réduire les coûts, et poser une base plus solide pour la suite.

## Analyse

Ce type de cas est instructif, pas pour le chiffre headline, mais pour ce qu'il révèle en creux.

Une infrastructure qui coûte cher, c'est presque toujours une infrastructure qui a grandi sans stratégie d'automatisation claire. On empile des serveurs, on gère les exceptions à la main, on reporte les décisions d'architecture. Jusqu'à ce que la facture — ou une montée en charge — force la main.

L'intérêt de chercher des outils d'automatisation adaptés, c'est qu'ils révèlent les inefficacités structurelles. Sur une infra WordPress à grande échelle, ça peut toucher :

- La gestion des assets statiques et leur distribution (CDN, object storage)
- Le provisioning des environnements (combien de ces 25 serveurs sont vraiment différenciés ?)
- L'orchestration des déploiements sur N sites

La migration vers Next.js n'est pas anodine non plus : découpler le front du CMS permet de traiter le rendu comme un problème de build et de cache, pas de compute permanent. C'est une décision d'architecture qui a des implications directes sur les coûts d'infrastructure.

Pour une équipe Platform ou DevOps, le signal à retenir est simple : avant de négocier des tarifs avec votre cloud provider, vérifiez que votre outillage vous permet de savoir ce que vous consommez, pourquoi, et comment l'automatiser. C'est là que se jouent les vraies marges.

## Source

https://tsh.io/blog/how-to-reduce-cloud-costs/
