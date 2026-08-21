---
title: "make-argocd-fly : générer ses Applications ArgoCD"
slug: "make-argocd-fly-generer-applications-argocd"
date: 2025-11-03T08:00:03+01:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Rendu de manifestes Kubernetes depuis Helm, Kustomize et Jinja2, avec création automatique des ressources Application d'ArgoCD."
tags:
  - argocd
  - kubernetes
  - gitops
  - helm
series:
  - Veille techno
series_order: 31
showTableOfContents: true
---

## Introduction

Déployer des applications dans Kubernetes peut sembler complexe, surtout lorsqu'on jongle avec plusieurs environnements. Avec make-argocd-fly, un outil Python, ce processus devient plus fluide et structuré grâce à l'automatisation de la création des Applications ArgoCD.

## Résumé

make-argocd-fly est conçu pour générer des Applications ArgoCD et rendre des manifestes Kubernetes à partir de charts Helm, de superpositions Kustomize et de templates Jinja2. Il soutient les déploiements multi-environnements, crée automatiquement les ressources ArgoCD Application, et organise tout dans une structure de répertoire compatible avec GitOps. En rendant les templates en manifestes Kubernetes simples, cet outil permet aux développeurs de visualiser clairement ce qui sera déployé avant que cela n'atteigne le cluster.

## Utilité pros tech

Pour un professionnel en technologie, make-argocd-fly est une aubaine. Il élimine la complexité inhérente à la gestion des multiples environnements en automatisant la création des manifestes Kubernetes. Chaque déploiement est ainsi mieux contrôlé et prévisible.

## Mon expérience

J'ai trouvé make-argocd-fly particulièrement utile lors de la mise en place de projets où la fiabilité des déploiements est cruciale. Sa capacité à rendre visibles et compréhensibles les évolutions des manifestes Kubernetes avant le déploiement est un atout significatif, qui m'a épargné bien des surprises en production.

## Conclusion

make-argocd-fly révolutionne la manière dont nous gérons les déploiements Kubernetes grâce à sa simplicité et son efficacité. C'est un outil indispensable pour quiconque souhaite adopter une approche GitOps sans tracas.
