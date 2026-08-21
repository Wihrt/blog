---
title: "Postgresus : sauvegarder PostgreSQL vers de multiples cibles"
slug: "postgresus-sauvegarde-postgresql"
date: 2025-11-20T08:00:03+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Stockage local, S3, Cloudflare R2 ou Google Drive, avec compression intelligente, espaces de travail partagés et contrôle d'accès."
tags:
  - postgresql
  - backup
  - self-hosted
  - database
series:
  - Veille techno
series_order: 40
showTableOfContents: true
---

## Introduction

J'ai récemment découvert Postgresusis, un outil open-source formidable qui a transformé ma gestion de sauvegarde de bases de données PostgreSQL. Il est auto-hébergé et facilite grandement les sauvegardes automatiques avec des options de planification flexibles allant d'horaires à mensuelles.

## Résumé

Postgresusis offre une multitude de destinations de stockage, y compris le stockage local, S3, Cloudflare R2, Google Drive, et plus encore. Grâce à sa compression intelligente, l'espace utilisé est optimisé. De plus, l'outil propose des fonctionnalités collaboratives telles que les espaces de travail, le contrôle d'accès basé sur les rôles et les journaux d'audit.

## Utilité professionnelle pour les techniciens

Les notifications en temps réel via Email, Telegram, Slack ou Discord sont un vrai plus. Il supporte les versions de PostgreSQL de 12 à 18 et se déploie facilement via Docker grâce à trois options d'installation : un script automatisé, une simple commande Docker run, ou DockerCompose.

## Mon expérience

J'ai beaucoup apprécié la facilité d'installation et la capacité de Postgresusis à s'intégrer dans notre flux de travail existant. Les outils de collaboration ont renforcé notre efficacité en équipe.

## Conclusion

En somme, Postgresusis n'est pas seulement une solution de sauvegarde, mais un outil complet pour la gestion sécurisée et efficace des bases de données PostgreSQL. Pour en savoir plus, consultez l'article complet ici : [lien de l'article](https://api.daily.dev/r/C2y9CyO01).
