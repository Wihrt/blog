---
title: "Automatiser la publication d'articles sur les réseaux sociaux"
slug: "automatiser-publication-reseaux-sociaux"
date: 2025-09-17T09:00:59+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Comment j'ai monté une chaîne n8n et Postiz pour planifier mes publications sur plusieurs réseaux sans repasser à la main dessus."
tags:
  - n8n
  - automation
  - self-hosted
  - productivity
series:
  - Blog technique
series_order: 1
showTableOfContents: true
---

## Introduction

Gérer les publications sur différents réseaux sociaux peut rapidement devenir fastidieux. Chaque plateforme a ses propres spécificités, avec des limitations sur la planification des posts, souvent limitée à une semaine à l'avance. Si des solutions spécialisées existent, elles sont généralement payantes.

## Comment résoudre le problème ?

J'ai récemment découvert Postiz, un outil open source en pleine ascension qui permet de :

- Centraliser la gestion de vos publications sur plus de 25 réseaux via une interface unique ;

- Publier simultanément sur plusieurs plateformes sans ressaisir le contenu ;

- Générer du contenu à l'aide de l’IA.

Personnellement, je n’utilise que la première fonctionnalité, ce qui me permet de regrouper mes publications LinkedIn, Hashnode, et Discord dans une même interface.

## Comment installer Postiz ?

Deux options s’offrent à vous : utiliser la version SaaS ou héberger Postiz vous-même. Disposant d’un homelab, j'ai opté pour l’auto-hébergement sur Kubernetes, mais une installation via Docker Compose est également possible. L’installation est assez simple. Le chart Helm mériterait des améliorations, mais il reste fonctionnel.

## Configuration des canaux

Postiz introduit la notion de "canaux", correspondant aux différents réseaux où vous souhaitez publier. La configuration dépend du réseau et la documentation officielle vous guidera selon chaque plateforme.

![Screenshot des canaux disponibles](/images/automatiser-publication-reseaux-sociaux/01.png)

Pour les technophiles, cette étape est relativement aisée. Toutefois, pour les moins expérimentés, la prise en main peut être moins intuitive. À noter : sur certains canaux comme LinkedIn, vous ne pouvez configurer qu’un seul compte. Publier sur plusieurs pages LinkedIn nécessite donc autant d'instances que de pages, une véritable limite à considérer selon vos besoins.

## Utilisation de Postiz

Vous pouvez gérer vos publications soit depuis l’interface graphique, soit via l’API. Pour ma part, j’utilise les deux : l’API pour automatiser certains articles et l’interface pour les publications manuelles.

![Exemple de création d'une publication](/images/automatiser-publication-reseaux-sociaux/02.png)

![Création d'un futur post en utilisant l'IA directement intégrée](/images/automatiser-publication-reseaux-sociaux/03.png)

L’API possède deux limites : une documentation succincte et un quota par défaut de 30 appels par heure (modifiable en auto-hébergement). De plus, elle offre moins de fonctionnalités que l’interface, mais son évolution est prometteuse. L’interface reste quant à elle très agréable et efficace.

## Conclusion

Postiz s’impose comme un outil essentiel pour la gestion multi-canal des réseaux sociaux, permettant aux particuliers comme aux entreprises d’optimiser et de simplifier leur présence en ligne.

Broken By Mega - Si ça marche, c'est louche !
