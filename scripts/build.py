"""
Script de build automatisé pour le Système Expert Droit du Numérique
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def print_step(message):
    """Affiche une étape avec formatage"""
    print(f"\n{'='*60}")
    print(f"  {message}")
    print(f"{'='*60}\n")

def check_file_exists(filepath, description):
    """Vérifie qu'un fichier existe"""
    if not Path(filepath).exists():
        print(f"❌ ERREUR : {description} introuvable : {filepath}")
        return False
    print(f"✅ {description} trouvé : {filepath}")
    return True

def check_dependencies():
    """Vérifie les dépendances nécessaires"""
    print_step("Vérification des dépendances")
    
    # Vérifier Python
    print(f"Python version : {sys.version}")
    
    # Vérifier PyInstaller
    try:
        import PyInstaller
        print(f"✅ PyInstaller installé : version {PyInstaller.__version__}")
    except ImportError:
        print("❌ PyInstaller n'est pas installé")
        print("Installez-le avec : pip install pyinstaller")
        return False
    
    return True

def check_project_structure():
    """Vérifie la structure du projet"""
    print_step("Vérification de la structure du projet")
    
    files_required = {
        'main.py': 'Script principal',
        'index.html': 'Interface web',
        'legal_expert.spec': 'Configuration PyInstaller',
        'data/legal_expert_system_kb.json': 'Base de connaissances'
    }
    
    all_present = True
    for filepath, description in files_required.items():
        if not check_file_exists(filepath, description):
            all_present = False
    
    # Vérifier l'icône (optionnel)
    if not Path('icon.ico').exists():
        print("⚠️  Icône non trouvée : icon.ico")
        print("   L'application sera compilée sans icône personnalisée")
        print("   Exécutez 'python create_icon.py' pour en créer une")
    else:
        print("✅ Icône trouvée : icon.ico")
    
    return all_present

def clean_build_directories():
    """Nettoie les répertoires de build précédents"""
    print_step("Nettoyage des builds précédents")
    
    dirs_to_clean = ['build', 'dist', '__pycache__']
    
    for dir_name in dirs_to_clean:
        if Path(dir_name).exists():
            print(f"🗑️  Suppression de {dir_name}/")
            shutil.rmtree(dir_name)
    
    # Supprimer les fichiers .spec générés automatiquement
    for spec_file in Path('.').glob('*.spec'):
        if spec_file.name != 'legal_expert.spec':
            print(f"🗑️  Suppression de {spec_file}")
            spec_file.unlink()
    
    print("✅ Nettoyage terminé")

def build_application():
    """Compile l'application avec PyInstaller"""
    print_step("Compilation avec PyInstaller")
    
    # Utiliser le fichier .spec
    cmd = ['pyinstaller', 'legal_expert.spec']
    
    print(f"Commande : {' '.join(cmd)}")
    print("\nCompilation en cours...\n")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print("✅ Compilation réussie !")
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Erreur lors de la compilation :")
        print(e.stderr)
        return False

def verify_build():
    """Vérifie que le build a réussi"""
    print_step("Vérification du build")
    
    # Détecter le système d'exploitation
    if sys.platform == 'win32':
        exe_name = 'SystemeExpertDroitNumerique.exe'
    else:
        exe_name = 'SystemeExpertDroitNumerique'
    
    exe_path = Path('dist') / exe_name
    
    if exe_path.exists():
        file_size = exe_path.stat().st_size / (1024 * 1024)  # En MB
        print(f"✅ Exécutable créé : {exe_path}")
        print(f"   Taille : {file_size:.2f} MB")
        return True
    else:
        print(f"❌ Exécutable introuvable : {exe_path}")
        return False

def create_release_package():
    """Crée un package de distribution"""
    print_step("Création du package de distribution")
    
    # Créer un dossier release
    release_dir = Path('release')
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir()
    
    # Copier l'exécutable
    if sys.platform == 'win32':
        exe_name = 'SystemeExpertDroitNumerique.exe'
    else:
        exe_name = 'SystemeExpertDroitNumerique'
    
    exe_src = Path('dist') / exe_name
    exe_dst = release_dir / exe_name
    
    if exe_src.exists():
        shutil.copy2(exe_src, exe_dst)
        print(f"✅ Exécutable copié dans release/")
    
    # Copier la documentation
    docs = ['README.md', 'INSTALLATION.md']
    for doc in docs:
        if Path(doc).exists():
            shutil.copy2(doc, release_dir / doc)
            print(f"✅ {doc} copié")
    
    # Créer un fichier VERSION
    version_file = release_dir / 'VERSION.txt'
    with open(version_file, 'w', encoding='utf-8') as f:
        f.write("Système Expert - Droit du Numérique\n")
        f.write("Version 1.0.0\n")
        f.write("Date : 2024-12-16\n")
    print(f"✅ VERSION.txt créé")
    
    print(f"\n📦 Package créé dans : {release_dir.absolute()}")

def main():
    """Fonction principale"""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   Système Expert - Droit du Numérique                        ║
║   Script de Build Automatisé                                 ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Étape 1 : Vérifier les dépendances
    if not check_dependencies():
        print("\n❌ Build annulé : dépendances manquantes")
        return False
    
    # Étape 2 : Vérifier la structure du projet
    if not check_project_structure():
        print("\n❌ Build annulé : fichiers manquants")
        return False
    
    # Étape 3 : Nettoyer les builds précédents
    clean_build_directories()
    
    # Étape 4 : Compiler l'application
    if not build_application():
        print("\n❌ Build annulé : erreur de compilation")
        return False
    
    # Étape 5 : Vérifier le build
    if not verify_build():
        print("\n❌ Build annulé : exécutable non créé")
        return False
    
    # Étape 6 : Créer le package de distribution
    create_release_package()
    
    # Succès !
    print_step("BUILD TERMINÉ AVEC SUCCÈS ! 🎉")
    print("L'exécutable est prêt à être distribué.")
    print("Vous pouvez le tester en l'exécutant depuis dist/ ou release/")
    print("\nProchaines étapes :")
    print("  1. Tester l'exécutable")
    print("  2. Vérifier que toutes les fonctionnalités marchent")
    print("  3. Distribuer le package depuis release/")
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)