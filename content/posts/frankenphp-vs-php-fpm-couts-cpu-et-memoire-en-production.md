---
title: "FrankenPHP vs PHP-FPM : coûts CPU et mémoire en production"
slug: "frankenphp-vs-php-fpm-couts-cpu-et-memoire-en-production"
date: 2026-10-05T06:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Comparatif chiffré entre FrankenPHP et PHP-FPM pour choisir le runtime PHP selon le trafic et automatiser le provisioning."
tags:
  - platform-engineering
  - docker
  - kubernetes
  - automation
  - devops
series:
  - Veille techno
series_order: 90
showTableOfContents: true
---

## Introduction

Le choix du runtime PHP en production a un impact direct sur le dimensionnement, le coût d'infrastructure et les stratégies de scaling. Un article récent propose une comparaison détaillée entre FrankenPHP (mode worker) et PHP-FPM, en allant au-delà du simple benchmark de requêtes pour analyser la consommation CPU et mémoire en charge **et au repos**.

## Ce que dit l'article

Les résultats clés de cette analyse :

- **FrankenPHP en mode worker** délivre un throughput **3x supérieur** à PHP-FPM et une latence **60% plus basse**, grâce à son état applicatif persistant qui supprime le coût de bootstrap à chaque requête.
- **Au repos**, FrankenPHP consomme environ **85 MB** de mémoire contre **25 MB** pour PHP-FPM. Ce surcoût existe même sans trafic.
- **PHP-FPM** reste optimal pour les applications à faible trafic où la consommation minimale au repos est un critère important.
- **FrankenPHP** devient plus rentable dès que le volume de requêtes augmente, le coût par requête diminuant significativement grâce à la persistance de l'application en mémoire.

Le contexte de test inclut Docker et Symfony, ce qui rend les résultats directement exploitables pour des stacks courantes.

## Avis

D'un point de vue platform engineering, ce type de benchmark est exactement ce qu'il faut pour **alimenter des décisions d'automatisation**. Plutôt que de standardiser un runtime unique sur toute une plateforme, ces données permettent de construire des règles de provisioning adaptées au profil de chaque workload.

Concrètement, sur une plateforme Kubernetes hébergeant plusieurs services PHP, on pourrait imaginer des templates de déploiement qui sélectionnent le runtime en fonction du trafic attendu : `php-fpm` pour les microservices internes à faible sollicitation, `frankenphp` en mode worker pour les APIs exposées à fort débit. Le surcoût mémoire de FrankenPHP au repos (60 MB de delta) est négligeable sur un node bien dimensionné, mais il s'accumule si on l'applique à des dizaines de petits services qui ne font rien 90% du temps.

L'enjeu n'est pas de choisir un vainqueur, mais d'avoir les **métriques pour automatiser le bon choix** selon le contexte. C'est du capacity planning basé sur des données, pas sur des opinions.

---

🔗 [Article source](https://vulke.medium.com/frankenphp-vs-php-fpm-part-3-cpu-memory-and-the-hidden-cost-of-doing-nothing-92bfee7b00a5)
