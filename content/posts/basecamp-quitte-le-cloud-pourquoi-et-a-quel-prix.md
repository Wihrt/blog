---
title: "Basecamp quitte le cloud : pourquoi et à quel prix"
slug: "basecamp-quitte-le-cloud-pourquoi-et-a-quel-prix"
date: 2026-11-11T18:17:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "DHH explique le retour de Basecamp et HEY vers des serveurs dédiés, et ce que cela implique en automatisation."
tags:
  - cloud
  - platform-engineering
  - devops
  - terraform
  - ansible
series:
  - Veille techno
series_order: 130
showTableOfContents: true
---

## Contexte

Bascamp et HEY, deux produits phares de 37signals, ont annoncé leur sortie progressive du cloud. DHH, cofondateur, publie une analyse directe des raisons de ce choix. Le sujet est pertinent bien au-delà du cas Basecamp : il pose une question que beaucoup d'équipes esquivent.

## Ce que dit l'article

Le cloud est efficace à deux extrêmes : les charges très faibles, où la flexibilité à la demande prime, et les charges très élevées avec forte élasticité. Basecamp se trouve depuis des années dans une zone intermédiaire : une charge stable, prévisible, sans besoin d'élasticité forte. Dans cette configuration, le coût du cloud devient difficile à justifier face à une infrastructure physique bien dimensionnée.

L'équipe a fait le calcul. Résultat : reprendre la main sur des serveurs dédiés est plus rentable à leur échelle et leur profil de charge. HEY, qui n'a fonctionné que dans le cloud depuis son lancement, fait également partie de la migration.

DHH insiste sur un point souvent ignoré : le cloud n'est pas universellement optimal. C'est un outil, avec des cas d'usage précis.

## Analyse

Ce qui est structurant dans cette décision, ce n'est pas le retour au bare metal — c'est ce qu'il implique en termes d'outillage et d'automatisation.

Quitter les abstractions managées d'un cloud provider, c'est récupérer la responsabilité de tout ce que ces abstractions cachaient : provisionning, patching, haute disponibilité, observabilité. Les équipes qui font ce choix sans avoir un niveau d'automatisation solide se retrouvent vite en régression opérationnelle.

L'intuition ici est juste : l'objectif n'est pas de choisir entre cloud et on-premise, c'est de s'assurer que l'infrastructure est suffisamment automatisée pour être indépendante du substrat. Des outils comme **Ansible**, **Terraform** (ou OpenTofu), **Packer**, des pipelines d'Infrastructure as Code bien écrits — tout ça doit tenir la route que les ressources soient chez AWS ou dans une colo.

Pour une équipe Platform Engineering, ce type de mouvement est aussi l'occasion de remettre à plat les dépendances implicites aux services managés. Est-ce que votre monitoring repose sur CloudWatch ? Votre gestion des secrets sur AWS Secrets Manager ? Votre CI sur CodeBuild ? Autant de points de friction à cartographier avant de commencer.

Le cloud reste pertinent pour de nombreux cas. Mais cette décision rappelle qu'il faut régulièrement réévaluer le rapport coût/valeur, surtout quand le profil de charge est stable.

## Source

https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0
