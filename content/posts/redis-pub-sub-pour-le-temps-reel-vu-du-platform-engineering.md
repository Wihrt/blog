---
title: "Redis Pub/Sub pour le temps réel, vu du Platform Engineering"
slug: "redis-pub-sub-pour-le-temps-reel-vu-du-platform-engineering"
date: 2026-11-04T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "WebSocket et Redis Pub/Sub pour le temps réel : architecture, limites et enjeux de standardisation à l'échelle d'une organisation."
tags:
  - platform-engineering
  - database
  - api
  - devops
series:
  - Veille techno
series_order: 110
showTableOfContents: true
---

## Contexte

Les événements temps réel sont devenus un attendu standard dans les applications web modernes. Afficher un message instantané, notifier un utilisateur sans rechargement de page — ce sont des besoins courants qui impliquent des choix d'architecture précis côté backend.

## Ce que couvre l'article

L'article de Hackernoon détaille la mécanique classique derrière ce type de système :

- Le navigateur établit une connexion persistante avec le serveur via **WebSocket**.
- Le serveur s'appuie sur **Redis Pub/Sub** pour propager les messages entre ses différentes instances.
- Chaque instance souscrit aux canaux pertinents et relaie les événements aux clients connectés.

C'est un pattern bien établi, documenté, et qui fonctionne pour une large gamme de cas d'usage : messagerie, notifications, live updates. L'article en pose les bases de manière claire et accessible.

## Point de vue

La vraie question que soulève ce type d'article n'est pas *"faut-il utiliser Redis Pub/Sub ?"* mais *"comment on rend ce pattern accessible et maintenable à l'échelle d'une organisation ?"*

Dans une logique **Platform Engineering**, ce genre de brique est exactement ce qu'on cherche à standardiser. L'objectif : que les équipes produit ne réimplémentent pas la même plomberie à chaque nouveau service. Ça passe par des abstractions, des templates de déploiement, voire des services managés exposés via une Internal Developer Platform.

Cela dit, Redis Pub/Sub a ses limites connues : pas de persistance des messages, pas de garantie de delivery en cas de reconnexion, scalabilité horizontale à surveiller sous forte charge. Pour des cas plus exigeants, `Kafka` ou `NATS` entrent en jeu. Savoir *quand* ce pattern suffit — et *quand* il ne suffit plus — c'est une décision d'architecture qui mérite d'être documentée et partagée dans l'équipe.

L'automatisation commence par le choix des bons outils, puis par leur exposition cohérente aux équipes qui en ont besoin.

## Source

https://hackernoon.com/how-to-use-redis-pubsub-in-messengers?source=rss
