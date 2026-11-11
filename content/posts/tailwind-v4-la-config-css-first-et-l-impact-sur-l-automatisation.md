---
title: "Tailwind v4 : la config CSS-first et l'impact sur l'automatisation"
slug: "tailwind-v4-la-config-css-first-et-l-impact-sur-l-automatisation"
date: 2026-11-11T18:34:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Tailwind CSS v4 supprime le fichier de config obligatoire, un atout pour standardiser les templates de scaffolding internes."
tags:
  - automation
  - platform-engineering
  - devops
series:
  - Veille techno
series_order: 147
showTableOfContents: true
---

## Contexte

Tailwind CSS v4.0 vient de sortir avec une réécriture significative du moteur. Au-delà des nouveautés purement front, certains choix d'architecture méritent l'attention des équipes qui industrialisent la mise en place de projets web.

## Ce que dit l'article

La v4 tire parti des fonctionnalités CSS modernes : **cascade layers**, `color-mix()`, **container queries**, **transforms 3D**, et des valeurs utilitaires dynamiques. L'aspect le plus structurant est la **configuration CSS-first** : la personnalisation se fait désormais directement dans un fichier CSS, sans passer par un `tailwind.config.js` obligatoire. L'installation est allégée, avec moins de dépendances à gérer. Les performances sont également améliorées, le nouveau moteur étant réécrit en Rust.

## Analyse

Du point de vue d'une plateforme interne ou d'une chaîne d'automatisation, la suppression du fichier de configuration obligatoire est le détail le plus intéressant. Un fichier de config en moins, c'est :

- **Moins de surface à maintenir** dans les templates de scaffolding.
- **Une standardisation plus simple** à embarquer dans des générateurs de projets (Cookiecutter, Backstage, scripts maison).
- **Moins de drift de configuration** entre projets générés à des moments différents.

La config CSS-first simplifie aussi la lisibilité pour les équipes qui ne sont pas full CSS : tout est au même endroit, dans le même fichier que les variables de design. C'est un gain de cohérence, pas juste une préférence stylistique.

À noter : la migration depuis v3 implique des ajustements. L'écosystème de plugins doit s'adapter. Dans une logique de plateforme, il vaut mieux attendre que les dépendances critiques soient compatibles avant de standardiser sur la v4 — mais anticiper l'intégration dans les templates internes, c'est le bon moment pour le faire.

## Source

https://tailwindcss.com/blog/tailwindcss-v4
