---
title: "Renovate : automatiser la gestion de vos dépendances"
slug: "renovate-automatiser-dependances"
date: 2025-10-15T00:00:12+02:00
draft: false
author: "Arnaud Hatzenbuhler"
description: "De la configuration minimale aux customManagers et à l'auto-hébergement : tout ce qu'il faut pour laisser Renovate tenir vos dépendances à jour."
tags:
  - automation
  - ci-cd
  - docker
  - git
  - devops
series:
  - Blog technique
series_order: 3
showTableOfContents: true
---

Imaginez : il est 9h lundi matin, vous ouvrez GitLab/GitHub et découvrez 12 nouvelles Merge Requests. Elles ont été créées automatiquement durant le weekend et mettent à jour vos dépendances : Node.js 18.17.1 → 18.18.0, React 18.2.0 → 18.2.1, kubectl v1.28.3 → v1.28.4...

**5 minutes plus tard**, toutes sont mergées après validation automatique des tests CI. Votre équipe peut se concentrer sur les nouvelles fonctionnalités au lieu de passer du temps sur la maintenance.

C'est exactement ce que fait **Renovate** pour vous.

## Pourquoi Renovate va vous faire gagner du temps

### Le problème qu'on connaît tous

Sans automatisation, gérer les dépendances c'est :

- 📊 **2-3h par semaine** perdues à vérifier les mises à jour manuellement

- 🔒 **Des vulnérabilités** qui traînent parce qu'on reporte les mises à jour

- 😰 **La panique** quand une CVE critique sort sur une lib qu'on utilise

- 🔥 **Des migrations douloureuses** après des mois de retard

### La solution Renovate

Renovate surveille **automatiquement** vos dépendances et vous propose les mises à jour via Merge Request. Plus besoin de s'en soucier !

## Qu'est-ce que Renovate peut gérer ?

**Réponse courte** : pratiquement tout ! 🚀

**JavaScript/TypeScript** (npm, yarn, pnpm) • **Python** (pip, poetry) • **Java** (maven, gradle) • **Go** (go.mod) • **Rust** (cargo) • **PHP** (composer) • **Ruby** (bundler) • **.NET** (nuget) • **Docker** (images) • **Terraform** • **Kubernetes** • **GitHub Actions** • **GitLab CI** • et [bien d'autres](https://docs.renovatebot.com/modules/manager/)...

### Un exemple concret

Dans ce projet React/TypeScript :

```json
// package.json
"dependencies": {
  "react": "18.2.0",
  "@types/react": "18.2.15"
}
```

Renovate va automatiquement détecter et proposer :

- ✅ React 18.2.0 → 18.2.1 (patch de sécurité)

- ✅ @types/react 18.2.15 → 18.2.21 (types à jour)

- ✅ Les dépendances dans package-lock.json

## Démarrage express : 2 minutes pour l'activer

### Étape 1 : Créer le fichier de config

Ajoutez un fichier `renovate.json` à la racine de votre projet :

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"]
}
```

**C'est tout !** Cette configuration active Renovate avec des paramètres intelligents par défaut.

> **Astuce** : Le preset `config:recommended` groupe intelligemment les mises à jour pour éviter le spam de MR !

### Ce qui va se passer

1. 🎯 Renovate scanne votre projet et détecte les dépendances

2. 📋 Il crée un "Dependency Dashboard" (issue) avec le résumé

3. 🔄 Il propose les premières mises à jour via Merge Request

### À quoi ça ressemble en vrai ?

#### Le Dependency Dashboard

Renovate crée automatiquement une issue qui centralise tout :

![Issue « Dependency Dashboard » de Renovate listant les mises à jour ouvertes, les mises à jour bloquées et les dépendances détectées](/images/renovate-automatiser-dependances/01.png)

**Super pratique** : vue d'ensemble instantanée + contrôle granulaire de chaque mise à jour !

#### Une Merge Request typique

![Merge request Renovate « Update Helm release argo-cd to v8.5.8 », avec le tableau des versions et les release notes du chart](/images/renovate-automatiser-dependances/02.png)

**Le plus** : Renovate inclut automatiquement les release notes, changelogs et liens vers la documentation !

## Personnalisation intelligente

Les [presets](https://docs.renovatebot.com/presets-default/) ne sont que des alias de configuration. Votre projet a des besoins spécifiques ? Vous pouvez tout personnaliser !

### Exemple : Grouper pour éviter le spam

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "schedule": ["before 6am on Monday"],
  "packageRules": [
    {
      "matchUpdateTypes": ["patch"],
      "groupName": "🔧 Patches de la semaine",
      "automerge": true
    }
  ]
}
```

**Résultat** : Au lieu de 15 MR individuelles, vous obtenez 1 MR groupée avec tous les patches, qui se merge automatiquement si les tests passent.

#### Exemple concret : avant/après

**AVANT Renovate** (gestion manuelle) :

```plaintext
📅 Lundi : "Il faut que je vérifie les mises à jour..."
🔍 Mardi : Ouverture de package.json, vérification manuelle de 20 dépendances
📝 Mercredi : Mise à jour de 3 packages, tests en échec
🐛 Jeudi : Debug des breaking changes de lodash 4.17.20 → 5.0.0
😰 Vendredi : Rollback, remise à plus tard...
```

**APRÈS Renovate** (automatisé) :

```plaintext
🎯 Lundi matin : 3 MR prêtes dans votre boîte GitLab
   ├─ "🔧 Patches de la semaine" (lodash 4.17.20→4.17.21, axios 1.5.0→1.5.1...)
   ├─ "⬆️ Update React to v18.2.1" (avec changelog détaillé)
   └─ "🚨 Security: Update express to v4.18.2" (CVE-2023-XXXX)

✅ 5 minutes : Review rapide + merge des patches auto-testés
☕ 9h05 : Café en toute sérénité, les dépendances sont à jour !
```

### Cas d'usage populaires

- **Scheduling** : `"schedule": ["after 10pm every weekday"]` → pas de MR pendant le travail

- **Automerge** : Patches et dev dependencies se mergent tout seuls

- **Labels** : `"labels": ["dependencies"]` → tri automatique

- **Assignation** : `"assignees": ["@team-lead"]` → notification directe

Toutes les options de configuration sont [documentées ici](https://docs.renovatebot.com/configuration-options/).

## Aller plus loin : gérer l'impossible

Renovate peut même gérer les dépendances "non-standard" avec les `customManagers`. Exemple parfait : les versions d'outils dans vos Dockerfiles.

### Le problème

Votre `Dockerfile` contient des versions hardcodées que Renovate ne détecte pas nativement :

```dockerfile
FROM ubuntu:24.04

# Version de kubectl non détectée par Renovate ❌
ENV KUBECTL_VERSION=v1.28.4
RUN curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
```

### La solution magique

Ajoutez un `customManager` dans votre config Renovate :

```json
{
  "extends": ["config:recommended"],
  "customManagers": [
    {
      "customType": "regex",
      "fileMatch": ["Dockerfile"],
      "matchStrings": [
        "# renovate: datasource=(?<datasource>\\S+) depName=(?<depName>\\S+)\\s+ENV \\w+_VERSION=(?<currentValue>.*)"
      ]
    }
  ]
}
```

Puis annotez votre Dockerfile :

```dockerfile
FROM ubuntu:24.04

# renovate: datasource=github-releases depName=kubernetes/kubernetes
ENV KUBECTL_VERSION=v1.28.4
RUN curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
```

**Magie** ✨ : Renovate propose maintenant automatiquement les mises à jour de kubectl dans vos Dockerfiles !

> **Attention** : Les customManagers sont puissants mais complexes. Lisez [la documentation](https://docs.renovatebot.com/modules/manager/custom/) avant de vous lancer.

## Renovate à l'échelle d'une organisation

### L'onboarding automatique

Renovate peut s'auto-inviter sur vos projets ! Il crée une MR d'onboarding avec une configuration de base :

#### La MR d'onboarding en détail

````markdown
# 🎉 Configure Renovate

Welcome to Renovate! This merge request introduces Renovate dependency update automation to this repository.

## What this PR does

Renovate will now keep your dependencies up-to-date by raising merge requests for you to approve or merge.

## Next steps

1. **Merge this MR** to enable Renovate
2. **Check the Dependency Dashboard** issue that will be created
3. **Customize** your renovate.json as needed

## Configuration preview

Renovate found the following package files:
- 📦 `package.json` (npm)
- 🐳 `Dockerfile` (docker)
- 🏗️ `.github/workflows/ci.yml` (github-actions)

**Detected dependencies**: 23 npm packages, 2 Docker images, 4 GitHub Actions

## Proposed renovate.json

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"]
}
````

This configuration will: ✅ Create dependency update MRs
✅ Group related updates together
✅ Respect semver for safer updates
✅ Add helpful labels and context

---

🤖 This MR was created automatically. Questions? Check the [docs](https://docs.renovatebot.com/).

````plaintext

**Génial** : Renovate vous montre exactement ce qu'il a détecté dans votre projet avant même de commencer !

#### Après le merge : le premier scan

```bash
# Logs de Renovate (visibles dans le Dependency Dashboard)
🔍 Scanning repository...
✅ Found package.json with 18 dependencies
✅ Found Dockerfile with 2 custom dependencies
✅ Found .github/workflows with 3 actions

📊 Summary:
├─ 5 patch updates available
├─ 2 minor updates available
├─ 1 major update available (will need approval)
└─ 1 security advisory found

🎯 Creating 3 merge requests...
✅ MR !45: Update patch dependencies
✅ MR !46: Update typescript to v5.2.0
⚠️ MR !47: Update lodash to v5.0.0 (major - needs approval)
````

Fini le setup manuel sur chaque projet → **adoption progressive** et **sans friction**.

### Partage de configuration

Créez vos propres presets et partagez-les dans toute l'organisation :

```json
// Dans votre repo "renovate-config"
{
  "description": "Config standard équipe Backend",
  "extends": ["config:recommended"],
  "schedule": ["after 22:00 on Sunday"],
  "labels": ["dependencies", "backend"],
  "assignees": ["@tech-lead-backend"]
}
```

```json
// Dans chaque projet de l'équipe
{
  "extends": ["github>company/renovate-config"]
}
```

**Bénéfice** : Modification centralisée → tous les projets bénéficient instantanément des améliorations !

### Auto-hébergement (self-hosted)

Pour les organisations avec des besoins spécifiques :

- 🏢 **Contrôle total** : vos données restent chez vous

- ⚡ **Performance** : pas de limite de rate limiting

- 🔧 **Customisation** : adaptez Renovate à votre infrastructure

#### Exemple : Renovate self-hosted sur GitLab CI

Voici une configuration complète pour faire tourner Renovate sur votre propre GitLab :

**1. Variables d'environnement GitLab** (Settings > CI/CD > Variables)

```bash
RENOVATE_TOKEN=<votre Personal Access Token GitLab>
RENOVATE_GIT_AUTHOR=renovate-bot <bot@company.com>
```

**2. Fichier** `.gitlab-ci.yml` dans un projet dédié :

```yaml
# Projet "renovate-runner"
stages:
  - renovate

renovate:
  stage: renovate
  image: renovate/renovate:latest
  script:
    - renovate
  rules:
    # Exécution automatique tous les jours à 6h
    - if: $CI_PIPELINE_SOURCE == "schedule"
    # Exécution manuelle possible
    - if: $CI_PIPELINE_SOURCE == "web"
  variables:
    # Configuration Renovate
    RENOVATE_PLATFORM: gitlab
    RENOVATE_ENDPOINT: https://gitlab.company.com/api/v4/
    RENOVATE_AUTODISCOVER: true
    RENOVATE_AUTODISCOVER_FILTER: "company-group/*"

    # Optimisations
    RENOVATE_REQUIRE_CONFIG: required
    LOG_LEVEL: info

    # Sécurité
    RENOVATE_ALLOWED_POST_UPGRADE_COMMANDS: '["npm audit fix"]'
```

**3. Pipeline programmée** (GitLab > CI/CD > Schedules) :

- **Cron** : `0 6 * * 1-5` (tous les jours ouvrés à 6h)

- **Variables** : `RENOVATE_LOG_LEVEL=debug` (optionnel pour debug)

#### Avantages du self-hosted

✅ **Contrôle complet** : vos tokens et données ne sortent pas de votre infra
✅ **Performance** : pas de limitation de l'API GitHub/GitLab
✅ **Customisation** : ajoutez vos propres datasources ou managers
✅ **Compliance** : respect des politiques de sécurité internes

#### Surveillance et maintenance

**Monitoring** via les logs GitLab CI :

```bash
# Voir les projets traités
grep "Processing repository" job-logs

# Identifier les erreurs
grep "ERROR" job-logs | head -20

# Statistiques des MR créées
grep "Created.*PR" job-logs | wc -l
```

**Mise à jour** : changez simplement la version de l'image Docker `renovate/renovate:latest`

> **Tip** : Commencez par un seul groupe de projets test avec `autodiscoverFilter` avant de l'appliquer à toute l'organisation !

## Pourquoi vous devriez l'adopter dès maintenant

### ROI immédiat

- ⏰ **Gain de temps** : 2-3h/semaine récupérées par développeur

- 🛡️ **Sécurité** : patches appliqués en quelques heures au lieu de semaines

- 😌 **Sérénité** : plus de stress sur les mises à jour en retard

### Adoption progressive

- 🚀 **Démarrage en 2 min** avec une config minimale

- 📈 **Amélioration continue** : ajustez selon vos besoins

- 👥 **Acceptation équipe** : les développeurs adorent ne plus gérer ça manuellement

---

**Le secret** : Renovate ne vous fait pas juste gagner du temps, il vous fait **dormir tranquille**. Vos dépendances sont à jour, sécurisées, et vous n'avez plus à y penser.

Prêt à essayer ? Ajoutez un `renovate.json` dans votre prochain projet et regardez la magie opérer ! ✨
