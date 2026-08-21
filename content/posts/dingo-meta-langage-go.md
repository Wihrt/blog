---
title: "Dingo : un méta-langage qui compile vers Go"
slug: "dingo-meta-langage-go"
date: 2025-12-04T08:00:03+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Types Result et Option, types somme avec pattern matching et propagation d'erreurs, compilés en Go idiomatique et compatible."
tags:
  - go
  - open-source
series:
  - Veille techno
series_order: 50
showTableOfContents: true
---

## Introduction

Je suis ravi de partager avec vous une découverte passionnante dans le développement Go : Dingo. C'est un méta-langage qui transpile vers Go, offrant des avancées significatives pour les développeurs.

## Résumé

Dingo ajoute des types Result, Option et des types somme avec un matching de motifs, la propagation d'erreurs grâce à l'opérateur ' ? ', ainsi que des utilitaires fonctionnels, tout en garantissant une compatibilité totale avec l'écosystème Go. C'est un peu comme TypeScript pour JavaScript, Dingo compile sa syntaxe en un code Go propre et idiomatique, sans surcharge d'exécution. Actuellement en développement actif, les fonctionnalités de base comme les types somme, le matching de motifs, la propagation d'erreurs et les fonctions lambda sont déjà opérationnelles. Le transpileur utilise une architecture en deux étapes : un préprocesseur pour les transformations textuelles suivi d'un traitement AST avec le parseur natif de Go. L'intégration LSP avec le proxy gopls et les cartes de sources garantissent un support IDE complet.

## Utilité pros tech

Pour les professionnels de la tech, Dingo est une aubaine. Il permet d'optimiser le développement en Go grâce à des outils modernes sans renoncer à la performance ou à la compatibilité. C'est un pont entre la puissance fonctionnelle et la robustesse de Go.

## Mon expérience

En tant que développeur, expérimenter Dingo a été incroyablement enrichissant. La capacité de gérer les erreurs de manière concise tout en utilisant des motifs complexes a transformé ma façon de coder en Go.

## Conclusion

Je vous encourage à jeter un œil à Dingo et à voir par vous-même l'impact qu'il peut avoir sur vos projets Go. Pour plus de détails, consultez l'article complet ici : [lien de l'article](https://api.daily.dev/r/mI5DgcWBH).
