---
title: "Automatiser la conformité CIS sur Amazon EKS"
slug: "conformite-cis-amazon-eks"
date: 2026-02-09T17:07:25+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Kyverno pour les politiques, OpenTofu pour la validation d'infrastructure et kube-bench pour les nœuds : 62 contrôles CIS couverts."
tags:
  - security
  - kubernetes
  - terraform
  - cloud
  - ci-cd
series:
  - Veille techno
series_order: 73
showTableOfContents: true
---

## Introduction

Dans cet article, je vais vous montrer comment automatiser la conformité CIS sur Amazon EKS en utilisant une approche multi-outils. Le but est de combiner plusieurs technologies pour atteindre une couverture de conformité optimale et sécuriser efficacement vos clusters.

## Résumé

Nous allons utiliser Kyverno pour l'application des politiques Kubernetes-native, OpenTofu pour la validation de l'infrastructure et kube-bench pour un scanning de sécurité au niveau des nœuds. Cette solution met en œuvre 62 contrôles CIS couvrant la validation à l'époque de la planification, l'application à l'exécution et l'audit au niveau du système, atteignant plus de 95 % de couverture grâce à l'intégration stratégique de ces outils.

## Utilité pros tech

En tant que professionnels de la technologie, assurer la sécurité et la conformité de nos environnements Kubernetes est crucial. Grâce à ce guide, vous pouvez intégrer ces outils directement dans votre pipeline de déploiement, garantissant que vos configurations respectent en permanence les normes sécuritaires de l'industrie.

## Mon expérience

En travaillant avec ces outils, j'ai constaté que tester avec des clusters KIND est un excellent moyen d'identifier les limitations réalistes de chaque outil dans le pipeline de validation de conformité. J'apprécie particulièrement comment Kyverno facilite l'application de politiques dynamiques et comment kube-bench offre une couverture complète au niveau des nœuds.

## Conclusion

En somme, l'intégration de Kyverno, OpenTofu, et kube-bench fournit une solution robuste pour la conformité CIS d'Amazon EKS. Bien qu'il y ait des limitations inhérentes à chaque outil, cette approche multi-outils assure une couverture exceptionnelle et réduit considérablement les risques de sécurité. Pour plus de détails, je vous encourage à consulter l'article complet sur [Daily Dev](https://api.daily.dev/r/PYLuR8jQo).
