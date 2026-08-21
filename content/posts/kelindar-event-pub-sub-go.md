---
title: "kelindar/event : du pub/sub in-process performant en Go"
slug: "kelindar-event-pub-sub-go"
date: 2025-12-18T08:00:00+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Une bibliothèque Go de dispatch d'événements en mémoire, pour découpler ses modules sans déployer RabbitMQ ou Kafka."
tags:
  - go
  - open-source
  - monitoring
series:
  - Veille techno
series_order: 54
showTableOfContents: true
---

## Introduction

Dans nos architectures modernes, la gestion efficace des événements est cruciale — surtout lorsqu'on travaille avec des systèmes modulaires ou orientés microservices. En tant que développeur évoluant dans des contextes où performance, scalabilité et clarté du code sont essentiels (DevOps, Kubernetes ou CI/CD), je suis toujours à l'affût d'outils qui peuvent optimiser nos flux internes. C'est ainsi que j'ai découvert `kelindar/event`.

## Résumé de l’article

L'article [présente kelindar/event](https://api.daily.dev/r/JJ2vqU3wN), une bibliothèque Go dédiée au dispatching d'événements en processus, avec des performances impressionnantes. Elle propose une approche événementielle permettant de découpler les modules internes d'une application tout en conservant une vitesse atteignant plusieurs millions d'événements par seconde. Avec des performances 4x à 10x supérieures à l'utilisation des channels Go classiques, elle offre une API simple basée sur une interface `Event`, supportant aussi bien le traitement synchrone qu'asynchrone. Elle est idéale pour des patterns pub/sub légers au sein d'un même processus, mais ne convient pas au messaging distribué ou à la persistance d'événements.

## Pourquoi c’est utile pour les pros tech

### Un gain de performance concret

Dans les systèmes exigeant une faible latence — comme en CI/CD, monitoring ou orchestration sur Kubernetes — la vitesse d'exécution est critique. `kelindar/event` offre des performances bien supérieures aux canaux, ce qui permet de limiter la surcharge tout en conservant une architecture propre.

### Une modularité facilitée

Cette bibliothèque permet un découplage clair entre producteurs et consommateurs d'événements, rendant le code plus maintenable. C'est particulièrement utile pour séparer les responsabilités dans un contrôleur Kubernetes ou un pipeline d'intégration continue complexe.

### Simplicité d’intégration

Pas besoin d'un cluster RabbitMQ ou Kafka juste pour gérer un flux d’événements internes. On reste dans le même processus, avec une API sobre et facile à tester.

## Mon retour d’expérience

J’ai intégré `kelindar/event` dans un outil de monitoring interne. Mon objectif était de collecter des statistiques en temps réel sur différents pipelines CI, tout en évitant les verrous classiques liés au threading ou aux mutex en Go. Résultat : une implémentation plus simple, presque deux fois plus rapide qu’avec les channels, et une meilleure séparation des composants. La librairie oblige à penser en événements, ce qui m’a forcé à mieux structurer mes modules internes. C’est un vrai plus en termes de lisibilité et de maintenance.

## Conclusion

Si vous travaillez en Go sur des applications nécessitant un pub/sub interne rapide et fiable — que ce soit dans un contexte DevOps, Kubernetes ou surveillance de pipelines — `kelindar/event` est une solution à considérer sérieusement. Pour aller plus loin, je vous recommande de lire [l’article original](https://api.daily.dev/r/JJ2vqU3wN).
