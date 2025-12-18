# 🔨 Guide de Compilation et Packaging

Ce guide explique comment compiler le Système Expert en application standalone et créer un installateur Windows.

---

## 📋 Table des matières

1. [Prérequis](#prérequis)
2. [Compilation avec PyInstaller](#compilation-avec-pyinstaller)
3. [Création de l'installateur Windows](#création-de-linstallateur-windows)
4. [Script de build automatique](#script-de-build-automatique)
5. [Dépannage](#dépannage)

---

## 🛠️ Prérequis

### Logiciels requis

| Logiciel | Version minimale | Utilisation |
|----------|------------------|-------------|
| Python | 3.8+ | Exécution et compilation |
| PyInstaller | 5.0+ | Création de l'exécutable |
| Inno Setup | 6.0+ (Windows uniquement) | Création de l'installateur |

### Installation des dépendances

```bash
# Installer PyInstaller
pip install pyinstaller

# Vérifier l'installation
pyinstaller --version
```

---

## 📦 Compilation avec PyInstaller

### Méthode 1 : Avec le fichier .spec (Recommandée)

Le fichier `SystemeExpertDroitNumerique.spec` contient toute la configuration nécessaire.

```bash
# Compiler avec le fichier .spec
pyinstaller SystemeExpertDroitNumerique.spec --clean --noconfirm
```

**Avantages :**

- Configuration centralisée
- Reproductibilité garantie
- Personnalisation avancée
- Support multi-plateforme

### Méthode 2 : Compilation directe

Sans fichier `.spec`, vous pouvez compiler directement :

```bash
# Windows
pyinstaller --onefile --windowed --icon=icon.ico --name=SystemeExpertDroitNumerique --add-data="data/legal_expert_system_kb.json;data" --add-data="index.html;." main.py

# Linux / macOS
pyinstaller --onefile --windowed --icon=icon.png --name=SystemeExpertDroitNumerique --add-data="data/legal_expert_system_kb.json:data" --add-data="index.html:." main.py
```

### Options PyInstaller importantes

| Option | Description |
|--------|-------------|
| `--onefile` | Crée un seul fichier exécutable |
| `--windowed` | Pas de console (mode GUI) |
| `--icon` | Icône de l'application |
| `--name` | Nom de l'exécutable |
| `--add-data` | Inclure des fichiers de données |
| `--clean` | Nettoyer les builds précédents |
| `--noconfirm` | Pas de confirmation (écrase) |
| `--upx-dir` | Chemin vers UPX pour compression |

### Résultats de la compilation

Après compilation, vous trouverez :

```
dist/
  └── SystemeExpertDroitNumerique.exe    # Windows
  └── SystemeExpertDroitNumerique        # Linux/Mac

build/                                    # Fichiers temporaires
  └── SystemeExpertDroitNumerique/

SystemeExpertDroitNumerique.spec          # Configuration (généré)
```

---

## 🎯 Script de Build Automatique

Le script `scripts/build.py` automatise tout le processus.

### Utilisation

```bash
# Lancer le build automatique
python scripts/build.py
```

### Étapes du script

1. ✅ **Vérification des dépendances** (Python, PyInstaller)
2. ✅ **Vérification de la structure du projet**
3. 🗑️ **Nettoyage des builds précédents**
4. 📦 **Compilation avec PyInstaller**
5. ✅ **Vérification du build**
6. 📁 **Création du package de distribution**

### Sortie du script

```
release/
  ├── SystemeExpertDroitNumerique.exe
  ├── README.md
  ├── LICENSE
  ├── CHANGELOG.md
  ├── docs/
  │   ├── INSTALLATION.md
  │   └── ...
  ├── icon.ico
  ├── icon.png
  └── VERSION.txt
```

### Personnalisation du script

Éditez `scripts/build.py` pour :

- Modifier les fichiers inclus dans le package
- Changer le nom de l'exécutable
- Ajouter des étapes de post-processing

---

## 🖥️ Création de l'Installateur Windows

### Installation d'Inno Setup

1. Téléchargez : [https://jrsoftware.org/isdl.php](https://jrsoftware.org/isdl.php)
2. Installez Inno Setup 6
3. Vérifiez l'installation : ouvrez Inno Setup Compiler

### Utilisation du script installer.iss

Le fichier `scripts/installer.iss` contient la configuration de l'installateur.

#### Configuration

Ouvrez `scripts/installer.iss` et vérifiez :

```pascal
#define MyAppName "Système Expert - Droit du Numérique"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Système Expert Académique"
#define MyAppURL "https://github.com/Brice97426/systeme-expert-droit-numerique"
#define MyAppExeName "SystemeExpertDroitNumerique.exe"
```

#### Compilation de l'installateur

**Méthode GUI :**

1. Ouvrez Inno Setup Compiler
2. File → Open → Sélectionnez `scripts/installer.iss`
3. Build → Compile

**Méthode ligne de commande :**

```bash
# Windows (avec Inno Setup installé)
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" scripts\installer.iss
```

#### Résultat

L'installateur sera créé dans :

```
scripts/installer_output/
  └── SystemeExpertDroitNumerique_Setup_v1.0.0.exe
```

### Fonctionnalités de l'installateur

✅ **Installation facile** (Next → Next → Install)
✅ **Choix du répertoire d'installation**
✅ **Création de raccourcis** (Bureau, Menu Démarrer)
✅ **Programme de désinstallation intégré**
✅ **Vérification de version** (upgrade automatique)
✅ **Gestion du registre Windows**
✅ **Messages personnalisés en français**

---

## 🎨 Création de l'Icône

### Utilisation du script create_icon.py

```bash
# Installer Pillow (si nécessaire)
pip install Pillow

# Générer les icônes
python scripts/create_icon.py
```

### Résultats

```
icon.ico     # Pour Windows
icon.png     # Pour Linux/Mac
icon.icns    # Pour macOS
```

### Personnalisation

Éditez `scripts/create_icon.py` pour :

- Changer les couleurs
- Modifier le symbole (⚖️)
- Ajuster la taille

---

## 🔍 Dépannage

### Problème : PyInstaller introuvable

**Erreur :**

```
ModuleNotFoundError: No module named 'PyInstaller'
```

**Solution :**

```bash
pip install pyinstaller
```

### Problème : Fichiers manquants dans l'exécutable

**Symptôme :** L'application se lance mais ne trouve pas les fichiers.

**Solution :**

1. Vérifiez le fichier `.spec` :

```python
datas = [
    ('data/legal_expert_system_kb.json', 'data'),
    ('index.html', '.'),
]
```

2. Recompilez avec `--clean` :

```bash
pyinstaller SystemeExpertDroitNumerique.spec --clean
```

### Problème : Exécutable trop volumineux

**Symptôme :** L'exécutable fait plus de 50 MB.

**Solutions :**

1. **Activer UPX** (compression) :

```bash
# Télécharger UPX : https://upx.github.io/
# Ajouter au PATH ou spécifier le chemin
pyinstaller --upx-dir="C:\upx" SystemeExpertDroitNumerique.spec
```

2. **Exclure les modules inutiles** dans le `.spec` :

```python
excludes=[
    'matplotlib',
    'numpy',
    'pandas',
    'scipy',
    'PIL',
]
```

### Problème : L'antivirus bloque l'exécutable

**Symptôme :** Windows Defender ou autre antivirus supprime l'exécutable.

**Raisons :** Faux positif courant avec PyInstaller.

**Solutions :**

1. **Ajouter une exception** dans l'antivirus
2. **Signer l'exécutable** (certificat code signing)
3. **Soumettre à VirusTotal** pour analyse

### Problème : Erreur lors de l'import de tkinter

**Erreur :**

```
ModuleNotFoundError: No module named '_tkinter'
```

**Solution (Linux) :**

```bash
sudo apt-get install python3-tk
```

**Solution (macOS) :**

```bash
brew install python-tk
```

### Problème : L'installateur Inno Setup échoue

**Erreur :** Fichier source introuvable.

**Solution :** Vérifiez les chemins dans `installer.iss` :

```pascal
Source: "dist\SystemeExpertDroitNumerique.exe"; DestDir: "{app}";
```

Assurez-vous que l'exécutable existe dans `dist/`.

---

## 📊 Comparaison des méthodes

| Méthode | Avantages | Inconvénients |
|---------|-----------|---------------|
| **PyInstaller seul** | Simple, rapide | Pas d'installateur |
| **Script build.py** | Automatisé, reproductible | Nécessite Python |
| **Inno Setup** | Installateur pro, désinstallation | Windows uniquement |
| **Tout combiné** | Expérience complète | Plus complexe |

---

## 🚀 Workflow recommandé

### Pour les développeurs

```bash
# 1. Développement et tests
python main.py

# 2. Compilation rapide
pyinstaller SystemeExpertDroitNumerique.spec --clean

# 3. Test de l'exécutable
./dist/SystemeExpertDroitNumerique.exe
```

### Pour la distribution

```bash
# 1. Build complet automatique
python scripts/build.py

# 2. Création de l'installateur (Windows)
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" scripts\installer.iss

# 3. Distribution
# - Exécutable : release/SystemeExpertDroitNumerique.exe
# - Installateur : scripts/installer_output/SystemeExpertDroitNumerique_Setup_v1.0.0.exe
```

---

## 📝 Checklist avant distribution

- [ ] ✅ Version mise à jour dans tous les fichiers
- [ ] ✅ CHANGELOG.md à jour
- [ ] ✅ Tests de l'application réussis
- [ ] ✅ Compilation sans erreurs ni warnings
- [ ] ✅ Exécutable testé sur machine vierge
- [ ] ✅ Installateur testé (installation + désinstallation)
- [ ] ✅ Documentation à jour
- [ ] ✅ Icônes présentes et correctes
- [ ] ✅ Licence vérifiée
- [ ] ✅ Release notes rédigées

---

## 📚 Ressources

- [Documentation PyInstaller](https://pyinstaller.org/)
- [Documentation Inno Setup](https://jrsoftware.org/isinfo.php)
- [UPX - Compresseur d'exécutables](https://upx.github.io/)
- [VirusTotal - Analyse de sécurité](https://www.virustotal.com/)

---

## 💡 Conseils avancés

### Optimisation de la taille

```bash
# Utiliser --exclude-module pour exclure des modules lourds
pyinstaller --exclude-module matplotlib SystemeExpertDroitNumerique.spec

# Activer la compression maximale
pyinstaller --upx-dir=/path/to/upx SystemeExpertDroitNumerique.spec
```

### Build multi-plateforme

Pour compiler pour plusieurs plateformes, utilisez des machines virtuelles ou CI/CD :

```yaml
# Exemple GitHub Actions
- name: Build Windows
  run: pyinstaller SystemeExpertDroitNumerique.spec
  
- name: Build Linux
  run: pyinstaller SystemeExpertDroitNumerique.spec
  
- name: Build macOS
  run: pyinstaller SystemeExpertDroitNumerique.spec
```

### Signature de code (Windows)

```bash
# Signer l'exécutable avec un certificat
signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com dist/SystemeExpertDroitNumerique.exe
```

---

<div align="center">

**🎉 Votre application est maintenant prête à être distribuée !**

[← Retour au README](../README.md)

</div>
