# 📥 Guide d'installation - Système Expert Droit du Numérique

Ce guide vous accompagne pas à pas pour installer et lancer le système expert sur votre machine (Windows, Linux, Mac).

---

## 📋 Table des matières

1. [Prérequis système](#prérequis-système)
2. [Installation standard](#installation-standard)
3. [Installation pour développeurs](#installation-pour-développeurs)
4. [Création de l'exécutable](#création-de-lexécutable)
5. [Dépannage](#dépannage)
6. [Désinstallation](#désinstallation)

---

## 🖥️ Prérequis système

### Configuration minimale

| Composant | Minimum | Recommandé |
|-----------|---------|------------|
| **OS** | Windows 7 / Ubuntu 18.04 / macOS 10.13 | Windows 10+ / Ubuntu 20.04+ / macOS 11+ |
| **Processeur** | Dual-core 1.5 GHz | Quad-core 2.0 GHz+ |
| **RAM** | 2 GB | 4 GB+ |
| **Disque** | 100 MB libres | 500 MB+ |
| **Python** | 3.8 | 3.10+ |
| **Navigateur** | Chrome 80+ / Firefox 75+ / Edge 80+ | Dernière version |

### Logiciels requis

#### 1. Python

**Vérifier si Python est installé :**

```bash
python --version
# ou
python3 --version
```

Si Python n'est pas installé :

- **Windows** : [Télécharger Python](https://www.python.org/downloads/) (cochez "Add Python to PATH")
- **Linux** : `sudo apt install python3 python3-pip`
- **Mac** : `brew install python3` (nécessite [Homebrew](https://brew.sh/))

#### 2. pip (Gestionnaire de paquets Python)

Normalement installé avec Python. Vérifiez :

```bash
pip --version
# ou
pip3 --version
```

Si absent :

```bash
python -m ensurepip --upgrade
```

#### 3. Git (optionnel mais recommandé)

Pour cloner le dépôt facilement : [Télécharger Git](https://git-scm.com/downloads)

---

## ⚙️ Installation standard

### Méthode 1 : Avec Git (recommandée)

#### Étape 1 : Cloner le dépôt

```bash
git clone https://github.com/Brice97426/systeme-expert-droit-numerique.git
cd systeme-expert-droit-numerique
```

#### Étape 2 : Créer un environnement virtuel

**Windows :**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / Mac :**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> 💡 L'environnement virtuel isole les dépendances du projet de votre système.

Vous devriez voir `(.venv)` devant votre invite de commande.

#### Étape 3 : Installer les dépendances

```bash
pip install -r requirements.txt
```

Cette commande installe :

- Flask (serveur web)
- Werkzeug (utilitaires WSGI)
- Jinja2 (moteur de templates)

#### Étape 4 : Vérifier l'installation

```bash
python main.py
```

Si tout fonctionne, vous verrez :

```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

Le navigateur devrait s'ouvrir automatiquement. Sinon, allez à `http://127.0.0.1:5000`

### Méthode 2 : Sans Git (téléchargement manuel)

1. **Télécharger** le projet : [ZIP depuis GitHub](https://github.com/Brice97426/systeme-expert-droit-numerique/archive/refs/heads/main.zip)
2. **Décompresser** l'archive
3. **Suivre les étapes 2 à 4** de la méthode 1

---

## 🛠️ Installation pour développeurs

Si vous souhaitez contribuer au projet ou modifier le code :

### 1. Fork et clone

```bash
# Fork depuis GitHub, puis :
git clone https://github.com/VOTRE_USERNAME/systeme-expert-droit-numerique.git
cd systeme-expert-droit-numerique
```

### 2. Installation en mode développement

```bash
# Créer et activer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Installer les dépendances de développement
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Si présent
```

### 3. Configuration IDE

**Visual Studio Code :**

1. Installer l'extension Python
2. Sélectionner l'interpréteur : `Ctrl+Shift+P` → "Python: Select Interpreter" → `.venv`

**PyCharm :**

1. File → Settings → Project → Python Interpreter
2. Ajouter un nouvel interpréteur → Existing environment → `.venv/bin/python`

### 4. Lancer en mode debug

```bash
export FLASK_ENV=development  # Linux/Mac
# ou
set FLASK_ENV=development     # Windows

python main.py
```

Le mode développement active :

- Rechargement automatique du serveur
- Messages d'erreur détaillés
- Debugger intégré

---

## 📦 Création de l'exécutable

Pour distribuer l'application sans nécessiter Python.

### Installation de PyInstaller

```bash
pip install pyinstaller
```

### Compilation

**Windows :**

```bash
pyinstaller --onefile --windowed --icon=icon.ico --name=ExpertDroitNumerique main.py
```

**Linux / Mac :**

```bash
pyinstaller --onefile --windowed --icon=icon.ico --name=ExpertDroitNumerique main.py
```

### Options PyInstaller

| Option | Description |
|--------|-------------|
| `--onefile` | Un seul fichier exécutable |
| `--windowed` | Pas de console (mode GUI) |
| `--icon=icon.ico` | Icône personnalisée |
| `--name=NOM` | Nom de l'exécutable |
| `--add-data` | Inclure fichiers supplémentaires |

### Inclure la base de connaissances

Créez un fichier `expert_system.spec` :

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data/legal_expert_system_kb.json', 'data'),
        ('index.html', '.'),
        ('icon.ico', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ExpertDroitNumerique',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'
)
```

Puis compiler :

```bash
pyinstaller expert_system.spec
```

L'exécutable se trouvera dans `dist/ExpertDroitNumerique.exe` (Windows) ou `dist/ExpertDroitNumerique` (Linux/Mac).

---

## 🔧 Dépannage

### Problème : Python n'est pas reconnu

**Erreur :**

```
'python' n'est pas reconnu en tant que commande interne
```

**Solution :**

1. Réinstaller Python en cochant "Add Python to PATH"
2. Ou ajouter manuellement Python au PATH :
   - Windows : Panneau de configuration → Système → Variables d'environnement
   - Ajouter `C:\Python310` (adapter selon votre version)

### Problème : Erreur lors de l'installation des dépendances

**Erreur :**

```
ERROR: Could not install packages due to an EnvironmentError
```

**Solutions :**

1. **Mettre à jour pip :**

   ```bash
   python -m pip install --upgrade pip
   ```

2. **Installer avec droits administrateur :**

   ```bash
   # Windows (CMD en admin)
   pip install -r requirements.txt
   
   # Linux/Mac
   sudo pip3 install -r requirements.txt
   ```

3. **Utiliser --user :**

   ```bash
   pip install --user -r requirements.txt
   ```

### Problème : Port 5000 déjà utilisé

**Erreur :**

```
Address already in use
```

**Solutions :**

1. **Changer le port dans `main.py` :**

   ```python
   app.run(port=5001)  # Au lieu de 5000
   ```

2. **Tuer le processus utilisant le port 5000 :**

   **Windows :**

   ```bash
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F
   ```

   **Linux/Mac :**

   ```bash
   lsof -i :5000
   kill -9 <PID>
   ```

### Problème : Le navigateur ne s'ouvre pas automatiquement

**Solution :**

Ouvrez manuellement votre navigateur et allez à :

```
http://127.0.0.1:5000
```

ou

```
http://localhost:5000
```

### Problème : Erreur JSON (base de connaissances)

**Erreur :**

```
JSONDecodeError: Expecting value
```

**Solution :**

1. Vérifier que `data/legal_expert_system_kb.json` existe
2. Valider le JSON : [JSONLint](https://jsonlint.com/)
3. Vérifier l'encodage du fichier (UTF-8)

### Problème : Module introuvable

**Erreur :**

```
ModuleNotFoundError: No module named 'flask'
```

**Solution :**

1. Vérifier que l'environnement virtuel est activé :
   - Vous devez voir `(.venv)` dans le terminal

2. Réinstaller les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

### Problème : Permissions refusées (Linux/Mac)

**Erreur :**

```
Permission denied
```

**Solution :**

```bash
chmod +x main.py
# ou
python3 main.py
```

---

## 🗑️ Désinstallation

### Désinstallation complète

```bash
# Désactiver l'environnement virtuel
deactivate

# Supprimer le dossier du projet
rm -rf systeme-expert-droit-numerique  # Linux/Mac
# ou
rmdir /s systeme-expert-droit-numerique  # Windows
```

### Désinstallation partielle (garder le code)

```bash
# Supprimer uniquement l'environnement virtuel
rm -rf .venv  # Linux/Mac
# ou
rmdir /s .venv  # Windows
```

---

## ✅ Vérification de l'installation

Pour vérifier que tout fonctionne correctement :

### Test 1 : Imports Python

```bash
python -c "import flask; import json; print('OK')"
```

Résultat attendu : `OK`

### Test 2 : Accès à la base de connaissances

```bash
python -c "import json; data=json.load(open('data/legal_expert_system_kb.json', encoding='utf-8')); print(f'Loaded {len(data[\"regles\"])} règles')"
```

Résultat attendu : `Loaded 12 règles`

### Test 3 : Lancement du serveur

```bash
python main.py
```

Résultat attendu : Page web accessible

---

## 📞 Support

Si vous rencontrez un problème non listé ici :

1. **Vérifier les issues GitHub** : [Issues existantes](https://github.com/Brice97426/systeme-expert-droit-numerique/issues)
2. **Créer une nouvelle issue** : [Nouvelle issue](https://github.com/Brice97426/systeme-expert-droit-numerique/issues/new)
3. **Inclure dans votre rapport** :
   - Système d'exploitation (Windows 10, Ubuntu 22.04, etc.)
   - Version de Python : `python --version`
   - Message d'erreur complet
   - Commande exécutée

---

## 🎉 Installation réussie

Si tout fonctionne, vous êtes prêt à utiliser le système expert !

Prochaine étape : Consultez le [Guide d'utilisation](USAGE.md)

---

<div align="center">

**💡 Besoin d'aide ? N'hésitez pas à ouvrir une issue sur GitHub !**

[← Retour au README](README.md)

</div>
