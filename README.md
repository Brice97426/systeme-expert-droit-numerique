# 🏛️ Système Expert - Droit du Numérique

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/Brice97426/systeme-expert-droit-numerique)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)](https://www.python.org/)
[![Offline](https://img.shields.io/badge/mode-offline-orange.svg)](README.md)

> 🎓 **Système expert académique d'aide à la décision en droit du numérique français**

Un outil d'orientation juridique destiné aux étudiants pour comprendre les enjeux du droit du numérique (RGPD, propriété intellectuelle, e-commerce, cybersécurité).

⚠️ **Avertissement** : Ce système ne remplace pas un avocat spécialisé. Les informations fournies sont indicatives et à des fins pédagogiques.

---

## 📋 Table des matières

- [Présentation](#-présentation)
- [Fonctionnalités](#-fonctionnalités)
- [Captures d'écran](#-captures-décran)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Architecture](#-architecture)
- [Technologies](#-technologies)
- [Base de connaissances](#-base-de-connaissances)
- [Contribution](#-contribution)
- [Licence](#-licence)
- [Auteur](#-auteur)

---

## 🎯 Présentation

Le **Système Expert - Droit du Numérique** est une application autonome fonctionnant **100% hors-ligne** qui aide à identifier les enjeux juridiques liés aux activités numériques en France.

### 🎓 Objectifs pédagogiques

- Sensibiliser aux obligations légales du numérique
- Comprendre le RGPD et la protection des données
- Appréhender les notions de propriété intellectuelle en ligne
- Identifier les risques juridiques du e-commerce
- Connaître les responsabilités en matière de cybersécurité

### 🔍 Domaines couverts

| Domaine | Thématiques |
|---------|-------------|
| **RGPD** | Traitement de données personnelles, consentement, données sensibles |
| **Propriété intellectuelle** | Droit d'auteur, contrefaçon, licences |
| **E-commerce** | CGV, obligations légales, droit de rétractation |
| **Cybersécurité** | Violations de données, notification CNIL |
| **Responsabilité** | Éditeur vs hébergeur, contenu illicite |

---

## ✨ Fonctionnalités

### 🧠 Moteur d'inférence

- ✅ Chaînage avant (forward chaining)
- ✅ 12 règles juridiques expertes
- ✅ Gestion des cas incomplets
- ✅ Explications détaillées des décisions
- ✅ Niveau de confiance pour chaque conclusion

### 🎨 Interface utilisateur

- ✅ Interface web responsive (PC et mobile)
- ✅ Formulaire interactif avec questions conditionnelles
- ✅ Résultats détaillés avec codes couleur selon la gravité
- ✅ Affichage des textes de loi applicables
- ✅ Recommandations d'actions concrètes

### 📦 Application autonome

- ✅ Fonctionnement 100% hors-ligne
- ✅ Application desktop packagée (PyInstaller)
- ✅ Aucune dépendance externe (CDN, API)
- ✅ Exécutable portable pour Windows/Linux/Mac
- ✅ Icône personnalisée

---

## 📸 Captures d'écran

*(À ajouter après installation)*

```
docs/
  ├── screenshots/
  │   ├── interface-accueil.png
  │   ├── formulaire-questions.png
  │   └── resultats-analyse.png
```

---

## 🚀 Installation

### Prérequis

- **Python 3.8+** ([Télécharger Python](https://www.python.org/downloads/))
- **pip** (gestionnaire de paquets Python)
- **Navigateur web moderne** (Chrome, Firefox, Edge)

### Installation rapide

#### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/Brice97426/systeme-expert-droit-numerique.git
cd systeme-expert-droit-numerique
```

#### 2️⃣ Créer un environnement virtuel

**Windows :**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac :**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

#### 4️⃣ Lancer l'application

```bash
python main.py
```

L'interface web s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse `http://127.0.0.1:5000`

---

## 📖 Utilisation

### Mode Web local

1. Lancez l'application : `python main.py`
2. Le navigateur s'ouvre automatiquement sur l'interface
3. Répondez aux questions du formulaire
4. Consultez l'analyse juridique détaillée
5. Exportez le rapport (PDF/HTML)

### Mode Application Desktop (à venir)

1. Double-cliquez sur l'exécutable `systeme_expert.exe`
2. L'interface s'ouvre dans une fenêtre dédiée
3. Utilisez l'application sans navigateur

### Exemple d'utilisation

**Cas pratique :** Site e-commerce avec collecte d'emails

1. **Question 1** : Le cas implique-t-il des données personnelles ? → **Oui** (emails)
2. **Question 2** : Avez-vous obtenu le consentement ? → **Non**
3. **Résultat** : ⚠️ Violation du RGPD détectée
   - Sanctions possibles : jusqu'à 20M€
   - Actions recommandées : Obtenir un consentement RGPD valide
   - Textes applicables : RGPD Article 6

---

## 🏗️ Architecture

### Structure du projet

```
systeme-expert-droit-numerique/
│
├── 📁 data/                          # Base de connaissances
│   └── legal_expert_system_kb.json  # Règles et décisions
│
├── 📁 scripts/                       # Scripts métier
│   ├── inference_engine.py          # Moteur d'inférence
│   └── utils.py                     # Fonctions utilitaires
│
├── 📁 docs/                          # Documentation
│   ├── INSTALLATION.md              # Guide d'installation détaillé
│   ├── USAGE.md                     # Guide d'utilisation
│   └── ARCHITECTURE.md              # Documentation technique
│
├── 📄 index.html                     # Interface utilisateur
├── 📄 main.py                        # Serveur Flask
├── 📄 requirements.txt               # Dépendances Python
├── 📄 README.md                      # Ce fichier
├── 📄 LICENSE                        # Licence MIT
├── 🖼️ icon.ico                       # Icône application
└── 📄 .gitignore                     # Fichiers exclus
```

### Flux de données

```
Utilisateur → Interface Web → Serveur Flask → Moteur d'inférence
                                  ↓
                         Base de connaissances (JSON)
                                  ↓
                     Résultat avec explications → Utilisateur
```

---

## 🛠️ Technologies

| Composant | Technologie | Version |
|-----------|-------------|---------|
| **Backend** | Python | 3.8+ |
| **Framework Web** | Flask | 3.0+ |
| **Frontend** | HTML5 / CSS3 / JavaScript | - |
| **Base de connaissances** | JSON | - |
| **Packaging** | PyInstaller | 6.0+ |

### Bibliothèques Python

```
Flask==3.0.0
Werkzeug==3.0.1
Jinja2==3.1.2
PyInstaller==6.3.0 (pour l'exécutable)
```

---

## 📚 Base de connaissances

### Structure JSON

La base de connaissances (`legal_expert_system_kb.json`) contient :

- **12 critères juridiques** (questions)
- **12 règles d'inférence** (conditions → décisions)
- **12 décisions** (diagnostics avec explications)
- **Métadonnées** (version, domaine, auteur)
- **Ressources** (organismes, textes de loi)

### Exemple de règle

```json
{
  "id": "R1",
  "nom": "RGPD - Traitement sans consentement",
  "conditions": {
    "operateur": "ET",
    "criteres": [
      {"id": "C1", "valeur": true},
      {"id": "C2", "valeur": false}
    ]
  },
  "decision": "D1",
  "confiance": 0.9
}
```

### Mise à jour

Pour modifier la base de connaissances :

1. Éditez le fichier `data/legal_expert_system_kb.json`
2. Respectez la structure JSON
3. Incrémentez la version dans les métadonnées
4. Relancez l'application (pas besoin de recompiler)

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Ce projet est à but académique.

### Comment contribuer

1. **Fork** le projet
2. Créez une branche : `git checkout -b feature/amelioration`
3. Committez vos changements : `git commit -m 'Ajout nouvelle règle RGPD'`
4. Poussez vers la branche : `git push origin feature/amelioration`
5. Ouvrez une **Pull Request**

### Règles de contribution

- ✅ Respecter la structure de la base de connaissances
- ✅ Tester les modifications avant PR
- ✅ Documenter les nouvelles règles
- ✅ Citer les sources juridiques
- ✅ Pas de données personnelles dans le code

---

## 📄 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License - Copyright (c) 2024 Brice97426

Permission est accordée d'utiliser, copier, modifier, fusionner, publier, 
distribuer, sous-licencier et/ou vendre des copies du logiciel.
```

---

## 👨‍💻 Auteur

**Brice97426**

- GitHub : [@Brice97426](https://github.com/Brice97426)
- Projet : [Système Expert - Droit du Numérique](https://github.com/Brice97426/systeme-expert-droit-numerique)

### Remerciements

- 🏛️ **CNIL** pour les ressources sur le RGPD
- 📖 **Légifrance** pour les textes de loi
- 🎓 Communauté des étudiants en droit du numérique

---

## ⚖️ Mentions légales

Ce système expert est un **outil pédagogique** destiné à l'apprentissage du droit du numérique. Il ne constitue pas une consultation juridique et ne remplace pas l'avis d'un avocat spécialisé.

Les informations fournies sont indicatives et peuvent ne pas refléter les dernières évolutions législatives ou jurisprudentielles.

**En cas de situation juridique réelle, consultez un professionnel du droit.**

---

## 📞 Support

- 🐛 **Bugs** : [Créer une issue](https://github.com/Brice97426/systeme-expert-droit-numerique/issues)
- 💡 **Suggestions** : [Ouvrir une discussion](https://github.com/Brice97426/systeme-expert-droit-numerique/discussions)
- 📧 **Contact** : Via GitHub

---

## 🗺️ Roadmap

### Version 1.0 (Actuelle)

- ✅ Moteur d'inférence fonctionnel
- ✅ 12 règles de base
- ✅ Interface web responsive
- ✅ Mode hors-ligne

### Version 1.1 (Prévue)

- ⏳ Application desktop packagée
- ⏳ Export PDF des rapports
- ⏳ Historique des analyses
- ⏳ Mode multilingue (EN/FR)

### Version 2.0 (Future)

- 💡 50+ règles juridiques
- 💡 IA pour améliorer les recommandations
- 💡 Mise à jour automatique de la jurisprudence
- 💡 API REST pour intégration externe

---

<div align="center">

**⭐ Si ce projet vous aide, n'hésitez pas à laisser une étoile sur GitHub ! ⭐**

Made with ❤️ for digital law education

</div>
