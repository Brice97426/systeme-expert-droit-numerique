# 🤝 Guide de contribution

Merci de votre intérêt pour contribuer au **Système Expert - Droit du Numérique** ! Ce projet est conçu dans un cadre académique et toutes les contributions sont les bienvenues.

---

## 📋 Table des matières

- [Code de conduite](#code-de-conduite)
- [Comment contribuer](#comment-contribuer)
- [Signaler un bug](#signaler-un-bug)
- [Proposer une amélioration](#proposer-une-amélioration)
- [Ajouter des règles juridiques](#ajouter-des-règles-juridiques)
- [Guide de style](#guide-de-style)
- [Processus de Pull Request](#processus-de-pull-request)
- [Communauté](#communauté)

---

## 📜 Code de conduite

### Nos valeurs

Ce projet s'engage à fournir un environnement accueillant et inclusif pour tous. Nous attendons de tous les contributeurs :

- ✅ Respect et courtoisie dans toutes les interactions
- ✅ Critiques constructives et bienveillantes
- ✅ Collaboration et entraide
- ✅ Acceptation des différents niveaux d'expertise

### Comportements inacceptables

- ❌ Harcèlement sous toutes ses formes
- ❌ Langage offensant ou discriminatoire
- ❌ Spam ou trolling
- ❌ Publication d'informations privées sans consentement

Les violations de ce code de conduite peuvent entraîner un bannissement temporaire ou permanent du projet.

---

## 💡 Comment contribuer

Il existe plusieurs façons de contribuer au projet :

### 1. 🐛 Signaler des bugs

Trouvé un bug ? Consultez [Signaler un bug](#signaler-un-bug)

### 2. 💡 Proposer des améliorations

Une idée pour améliorer le projet ? Voir [Proposer une amélioration](#proposer-une-amélioration)

### 3. 📚 Améliorer la documentation

- Corriger des fautes de frappe
- Clarifier des explications
- Traduire la documentation
- Ajouter des exemples

### 4. ⚖️ Enrichir la base juridique

- Ajouter de nouvelles règles
- Mettre à jour la jurisprudence
- Corriger des imprécisions juridiques

### 5. 💻 Coder

- Corriger des bugs
- Implémenter de nouvelles fonctionnalités
- Optimiser les performances
- Améliorer l'interface utilisateur

---

## 🐛 Signaler un bug

Avant de créer une issue :

1. **Vérifiez** qu'il n'existe pas déjà une issue similaire
2. **Testez** avec la dernière version du projet
3. **Isolez** le problème (étapes de reproduction minimales)

### Template de bug report

```markdown
## 🐛 Description du bug

[Description claire et concise du bug]

## 📋 Étapes pour reproduire

1. Aller à '...'
2. Cliquer sur '...'
3. Défiler jusqu'à '...'
4. Voir l'erreur

## ✅ Comportement attendu

[Ce qui devrait se passer]

## ❌ Comportement actuel

[Ce qui se passe réellement]

## 🖼️ Captures d'écran

[Si applicable]

## 🖥️ Environnement

- OS : [Windows 10, Ubuntu 22.04, macOS 12]
- Python : [3.10.5]
- Navigateur : [Chrome 110]

## 📝 Informations complémentaires

[Logs, messages d'erreur, etc.]
```

[Créer une issue de bug](https://github.com/Brice97426/systeme-expert-droit-numerique/issues/new?template=bug_report.md)

---

## 💡 Proposer une amélioration

### Template de feature request

```markdown
## 💡 Résumé de la fonctionnalité

[Description courte]

## 🎯 Problème résolu

[Quel problème cette fonctionnalité résout-elle ?]

## 💭 Solution proposée

[Comment cette fonctionnalité devrait fonctionner]

## 🔄 Alternatives envisagées

[Autres solutions possibles]

## ➕ Informations complémentaires

[Contexte, exemples, mockups]
```

[Proposer une amélioration](https://github.com/Brice97426/systeme-expert-droit-numerique/issues/new?template=feature_request.md)

---

## ⚖️ Ajouter des règles juridiques

### Structure d'une règle

Pour ajouter une nouvelle règle juridique à la base de connaissances :

1. **Ouvrez** `data/legal_expert_system_kb.json`
2. **Ajoutez** un nouveau critère si nécessaire :

```json
{
  "id": "C13",
  "code": "nom_unique",
  "question": "Votre question claire et précise ?",
  "type": "boolean",
  "obligatoire": true,
  "aide": "Explication détaillée avec exemples",
  "exemples": ["Exemple 1", "Exemple 2"],
  "categorie": "Catégorie juridique"
}
```

3. **Créez** une nouvelle règle :

```json
{
  "id": "R13",
  "nom": "Nom de la règle",
  "description": "Description juridique",
  "conditions": {
    "operateur": "ET",
    "criteres": [
      {"id": "C1", "valeur": true}
    ]
  },
  "decision": "D13",
  "confiance": 0.85,
  "priorite": 2,
  "categorie": "Catégorie",
  "active": true
}
```

4. **Ajoutez** la décision correspondante :

```json
{
  "id": "D13",
  "code": "code_unique",
  "titre": "Titre de la décision",
  "jugement": "CONFORME / NON_CONFORME / PARTIELLEMENT_CONFORME",
  "gravite": "nulle / faible / moyenne / elevee / tres_elevee",
  "couleur": "#hexcode",
  "icone": "emoji",
  "resume": "Résumé court",
  "explication": "Explication juridique détaillée",
  "consequences": ["Conséquence 1", "Conséquence 2"],
  "actions_recommandees": ["Action 1", "Action 2"],
  "textes_applicables": ["Loi X", "Article Y"],
  "references_jurisprudence": ["Arrêt Z"]
}
```

5. **Incrémentez** la version dans les métadonnées
6. **Citez vos sources** juridiques (textes de loi, jurisprudence)

### Critères de validation

✅ **Obligatoire :**

- Sources juridiques fiables (Légifrance, CNIL, etc.)
- Références aux textes de loi applicables
- Exemples concrets
- Explication pédagogique claire

❌ **À éviter :**

- Informations non sourcées
- Opinions personnelles non étayées
- Termes trop techniques sans explication
- Copier-coller de textes de loi sans contextualisation

---

## 🎨 Guide de style

### Code Python

```python
# PEP 8 - Style guide Python officiel

# Imports
import json
from flask import Flask, render_template

# Classes (PascalCase)
class InferenceEngine:
    pass

# Fonctions (snake_case)
def load_knowledge_base():
    pass

# Constants (UPPER_CASE)
MAX_RULES = 100

# Variables (snake_case)
user_responses = {}

# Docstrings
def analyze_case(responses):
    """
    Analyse un cas juridique.
    
    Args:
        responses (dict): Réponses de l'utilisateur
        
    Returns:
        list: Liste des décisions applicables
    """
    pass
```

### Code JavaScript

```javascript
// camelCase pour variables et fonctions
let userAnswers = {};

function displayResults(decisions) {
  // Code...
}

// PascalCase pour classes
class DecisionRenderer {
  constructor() {
    // Code...
  }
}

// Constants en UPPER_CASE
const MAX_RETRIES = 3;

// Commentaires clairs
// Vérifie si toutes les questions obligatoires ont une réponse
function validateForm() {
  // Code...
}
```

### HTML/CSS

```html
<!-- HTML5 sémantique -->
<article class="decision-card decision-card--non-conforme">
  <header class="decision-card__header">
    <h2 class="decision-card__title">Titre</h2>
  </header>
  <div class="decision-card__content">
    <!-- Contenu -->
  </div>
</article>
```

```css
/* BEM (Block Element Modifier) */
.decision-card {
  /* Block */
}

.decision-card__header {
  /* Element */
}

.decision-card--non-conforme {
  /* Modifier */
}
```

### JSON

```json
{
  "id": "R1",
  "nom": "Nom de la règle",
  "description": "Description",
  "conditions": {
    "operateur": "ET",
    "criteres": []
  }
}
```

- Indentation : 2 espaces
- Noms de clés : snake_case
- Encodage : UTF-8

### Commits

Format : `type(scope): message`

**Types :**

- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation
- `style`: Formatage, point-virgule manquant
- `refactor`: Refactorisation du code
- `test`: Ajout de tests
- `chore`: Maintenance

**Exemples :**

```
feat(rules): ajout règle RGPD cookies
fix(ui): correction affichage mobile
docs(readme): mise à jour installation
refactor(engine): optimisation moteur inférence
```

---

## 🔀 Processus de Pull Request

### 1. Fork et clone

```bash
# Fork depuis GitHub
git clone https://github.com/VOTRE_USERNAME/systeme-expert-droit-numerique.git
cd systeme-expert-droit-numerique
```

### 2. Créer une branche

```bash
# Branche descriptive
git checkout -b feat/nouvelle-regle-cookies
# ou
git checkout -b fix/correction-affichage-mobile
```

### 3. Faire vos modifications

- Respectez le [Guide de style](#guide-de-style)
- Testez localement
- Committez régulièrement

```bash
git add .
git commit -m "feat(rules): ajout règle cookies"
```

### 4. Pousser votre branche

```bash
git push origin feat/nouvelle-regle-cookies
```

### 5. Créer la Pull Request

1. Allez sur GitHub
2. Cliquez sur "New Pull Request"
3. Remplissez le template :

```markdown
## 📝 Description

[Description de vos changements]

## 🎯 Type de changement

- [ ] 🐛 Correction de bug
- [ ] ✨ Nouvelle fonctionnalité
- [ ] 📚 Documentation
- [ ] ♻️ Refactorisation
- [ ] ⚖️ Ajout de règle juridique

## 🧪 Tests effectués

- [ ] Testé localement
- [ ] Testé sur Windows/Linux/Mac
- [ ] Vérifié sur mobile
- [ ] Pas de régression

## 📋 Checklist

- [ ] Mon code suit le guide de style
- [ ] J'ai testé mes modifications
- [ ] J'ai mis à jour la documentation si nécessaire
- [ ] J'ai ajouté des commentaires si nécessaire
- [ ] Mes commits suivent la convention
- [ ] J'ai cité mes sources (si règle juridique)

## 📎 Informations complémentaires

[Screenshots, sources juridiques, etc.]
```

### 6. Revue de code

- Un mainteneur reviewera votre PR
- Répondez aux commentaires
- Effectuez les modifications demandées
- Une fois approuvée, votre PR sera mergée !

---

## 📚 Ressources

### Documentation officielle

- [RGPD - Texte complet](https://www.cnil.fr/fr/reglement-europeen-protection-donnees)
- [Légifrance](https://www.legifrance.gouv.fr/)
- [Code de la propriété intellectuelle](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069414/)

### Outils

- [JSON Validator](https://jsonlint.com/)
- [Python PEP 8](https://pep8.org/)
- [Markdown Guide](https://www.markdownguide.org/)

### Contact

- 📧 Issues GitHub : [Créer une issue](https://github.com/Brice97426/systeme-expert-droit-numerique/issues/new)
- 💬 Discussions : [Ouvrir une discussion](https://github.com/Brice97426/systeme-expert-droit-numerique/discussions)

---

## 🏆 Contributeurs

Merci à tous ceux qui contribuent à améliorer ce projet !

<!-- Contributors list will be automatically generated -->

---

## 📄 Licence

En contribuant à ce projet, vous acceptez que vos contributions soient sous [Licence MIT](LICENSE).

---

<div align="center">

**🙏 Merci pour votre contribution !**

Chaque contribution, petite ou grande, est précieuse.

[← Retour au README](README.md)

</div>
