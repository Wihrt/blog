---
title: "Construire un serveur gRPC en Go, testable via Postman"
slug: "construire-un-serveur-grpc-en-go-testable-via-postman"
date: 2026-10-29T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Guide pratique pour créer un serveur gRPC en Go, avec un focus sur le support natif de gRPC dans Postman depuis la 9.3.3."
tags:
  - go
  - api
  - devops
  - platform-engineering
series:
  - Veille techno
series_order: 108
showTableOfContents: true
---

## Introduction

gRPC s'est imposé comme un standard sérieux pour la communication inter-services haute performance. Basé sur HTTP/2 et Protobuf, il offre un contrat d'interface strict là où REST laisse souvent place à l'interprétation. Cet article en Go pose les fondations d'un serveur gRPC fonctionnel et illustre le tout avec une API réelle.

## Résumé de l'article

L'article guide pas à pas la construction d'un serveur `gRPC` en Go. Les points couverts :

- Rappel du positionnement de gRPC : framework RPC open source, développé par Google, orienté performance.
- Mise en place d'un serveur Go avec les primitives `gRPC` de base.
- Utilisation de l'API livescore comme cas concret pour valider le service.
- Mention importante : **depuis la version 9.3.3, Postman supporte nativement les API gRPC**, ce qui simplifie le test et l'exploration des endpoints.

Le niveau est accessible, orienté mise en pratique rapide.

## Avis

La valeur de ce type de contenu ne réside pas dans la nouveauté technique — gRPC existe depuis 2015. Elle est dans ce qu'il révèle sur la maturité de l'écosystème outillage.

Postman qui intègre `gRPC`, c'est un signal concret : la barrière à l'entrée baisse. Pour des équipes DevOps ou Platform Engineering qui gèrent des flux inter-services, un protocole à contrat fort combiné à des outils de test accessibles, c'est une réduction de friction réelle. Moins d'ambiguïté sur les interfaces, moins de temps perdu à déboguer des incompatibilités de format.

L'automatisation des tests d'API gRPC devient plus simple à intégrer dans une pipeline CI sans outillage custom. C'est exactement le genre de levier à surveiller : pas la techno elle-même, mais le moment où l'écosystème autour devient suffisamment mature pour justifier l'adoption à l'échelle d'une équipe.

Le vrai verrou sur ce type de migration n'est presque jamais technique. C'est l'outillage qui suit — ou pas.

## Source

https://towardsdev.com/build-simple-grpc-server-with-golang-7bc8bd11f5de
