---
title: "Pulumi vs Terraform : réduire la friction en IaC"
slug: "pulumi-vs-terraform-reduire-la-friction-en-iac"
date: 2026-11-05T07:00:38+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Comparaison Pulumi/Terraform : pourquoi les langages généralistes réduisent la friction en infrastructure as code."
tags:
  - terraform
  - platform-engineering
  - devops
  - automation
series:
  - Veille techno
series_order: 111
showTableOfContents: true
---

## Contexte

Le choix d'un outil d'Infrastructure as Code n'est pas anodin. Il conditionne la maintenabilité, la courbe d'apprentissage et la vélocité des équipes sur le long terme. Le débat Pulumi vs Terraform revient régulièrement, et cet article l'aborde sous un angle intéressant : non pas "que fait chaque outil", mais "qu'est-ce qu'un bon outil IaC doit permettre de faire".

## Ce que dit l'article

L'article part d'un principe simple : en IaC, on devrait se concentrer sur **ce qu'on veut accomplir**, pas sur les contraintes imposées par l'outil lui-même. Terraform, avec HCL, impose un DSL propriétaire qui fonctionne bien pour des cas standards, mais qui montre ses limites dès qu'on cherche à :

- Abstraire des patterns complexes
- Factoriser de la logique réutilisable
- Tester l'infrastructure comme du code applicatif

Pulumi répond à ces limites en permettant d'utiliser des langages généralistes — TypeScript, Python, Go, C# — pour décrire l'infrastructure. Le gain : les équipes travaillent dans des langages qu'elles connaissent, avec les mêmes outils, les mêmes pratiques de test et les mêmes patterns de conception.

## Avis

L'intuition derrière cet article est bonne : **l'outil IaC idéal est celui qui génère le moins de friction possible entre l'intention et l'exécution**. Terraform reste une valeur sûre avec un écosystème de providers imbattable et une adoption massive. Difficile de l'ignorer.

Mais HCL devient un vrai obstacle dès qu'on veut industrialiser sérieusement. Les modules Terraform permettent de factoriser, mais avec des limites structurelles que n'importe quel développeur ressent rapidement. Pulumi lève cette contrainte en s'appuyant sur des langages qui disposent nativement de structures de contrôle, de typage fort, de tests unitaires.

Pour des équipes Platform Engineering qui cherchent à **réduire le coût cognitif de la gestion d'infrastructure**, c'est un argument concret. L'automatisation ne devrait pas se faire malgré l'outil, mais grâce à lui.

Le choix reste contextuel — taille d'équipe, compétences disponibles, écosystème existant — mais la direction pointée par Pulumi est alignée avec ce que le terrain demande.

## Source

https://techwatching.dev/posts/pulumi-vs-terraform
