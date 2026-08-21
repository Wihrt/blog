---
title: "Keyper : un coffre-fort de credentials à connaissance nulle"
slug: "keyper-coffre-fort-credentiels"
date: 2025-11-03T08:00:00+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Clés API, mots de passe et secrets chiffrés côté client en AES-256-GCM, dans une PWA React branchée sur votre propre instance Supabase."
tags:
  - security
  - self-hosted
  - open-source
  - typescript
series:
  - Veille techno
series_order: 30
showTableOfContents: true
---

## Introduction

Keyper est une solution innovante pour gérer vos crédentiels de manière sécurisée. En tant que développeur, je sais combien il est crucial de protéger nos informations sensibles.

## Résumé

Keyper est un coffre-fort de crédentiels, open source et auto-hébergé, qui stocke vos clés API, mots de passe et secrets via un chiffrement à connaissance nulle. Il est construit comme une PWA React TypeScript et se connecte à votre propre instance Supabase. Tout est chiffré côté client avec AES-256-GCM, garantissant que vos données restent sécurisées.

## Utilité pros tech

Les fonctionnalités de Keyper, comme le support multi-utilisateur et la sécurité au niveau des lignes de la base de données, sont essentielles pour les équipes techniques. De plus, l'interface propre, avec des fonctions de recherche et de catégorisation, facilite la gestion des informations sensibles.

## Mon expérience

En l'installant via npm, j'ai été impressionné par la simplicité du processus et la prise de contrôle totale sur mes crédentiels, sans aucune télémetrie ou partage de données avec des tiers.

## Conclusion

Le chiffrement côté client est la propriété qui compte vraiment ici : elle détermine ce qu'un attaquant obtient s'il met la main sur la base. Avec une architecture à connaissance nulle, il récupère des octets inexploitables. Le revers est tout aussi net : personne ne peut vous rendre l'accès si vous perdez votre clé. C'est un choix assumé, qui impose de réfléchir à la sauvegarde de la clé avant d'y déposer quoi que ce soit d'important.

Pour quiconque soucieux de sécuriser ses informations sans compromis, Keyper est une solution que je recommande chaudement. L'article complet est à lire ici : [Lien vers l'article complet](https://api.daily.dev/r/th5zdd8YW).
