---
title: "Cilium sur EKS sans kube-proxy : guide pratique"
slug: "cilium-sur-eks-sans-kube-proxy-guide-pratique"
date: 2026-11-11T18:25:00+00:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "Installer Cilium en mode eBPF sur EKS sans kube-proxy, avec bénéfices pour l'automatisation et le GitOps réseau."
tags:
  - cilium
  - kubernetes
  - networking
  - gitops
  - platform-engineering
series:
  - Veille techno
series_order: 138
showTableOfContents: true
---

## Contexte

Kube-proxy est présent dans presque tous les clusters Kubernetes par défaut. Pourtant, il repose sur `iptables` — un mécanisme difficile à déboguer à grande échelle et peu adapté aux environnements qui évoluent vite. Cilium, via eBPF, propose une alternative plus directe et plus opérable.

## Ce que couvre l'article

L'article guide pas à pas l'installation de Cilium sur EKS en mode `no kube-proxy`. Les points clés :

- Désactivation complète de `kube-proxy` lors du bootstrap du cluster
- Prise en charge du plan réseau par Cilium via eBPF, sans couche iptables
- Configuration du mode `IPAM` adapté à EKS
- Vérification de l'état du cluster post-installation avec les outils Cilium (`cilium status`, `cilium connectivity test`)
- Gains attendus : latence réduite, meilleure scalabilité, observabilité native plus fine

L'article est concret, orienté pratique, avec les commandes nécessaires pour reproduire la setup.

## Analyse

L'intérêt principal ici dépasse la performance réseau. Ce qui compte, c'est la **logique d'automatisation** que cette architecture permet.

`kube-proxy` avec ses règles `iptables` est une boîte noire difficile à inspecter, à tester et à rendre reproductible. Cilium avec eBPF expose une surface de configuration claire, des métriques Prometheus natives, et un comportement réseau qu'on peut auditer.

Pour une équipe Platform Engineering, cela change le rapport à l'infrastructure réseau : on passe d'un composant subi à un composant piloté. La configuration Cilium peut être versionnée, déployée via GitOps, et testée avant de toucher la prod. C'est exactement ce qu'on cherche quand on construit une plateforme interne fiable.

La vraie complexité reste l'adoption : eBPF impose des contraintes sur la version du kernel, et Cilium a une courbe d'apprentissage. Mais sur EKS avec des AMIs récentes, ces contraintes sont largement levées. Le ratio complexité/bénéfice penche clairement du bon côté pour les équipes qui opèrent des clusters à l'échelle.

## Source

https://medium.com/@amitmavgupta/cilium-installing-cilium-in-eks-with-no-kube-proxy-86f54a56c360
