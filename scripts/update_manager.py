"""
Système de Mise à Jour Sécurisé (Hors-ligne)
Permet de mettre à jour la base de connaissances avec une clé de validation
"""

import json
import hashlib
import hmac
import os
from pathlib import Path
from datetime import datetime

# Clé secrète pour signer les mises à jour (À GARDER CONFIDENTIELLE)
SECRET_KEY = "VOTRE_CLE_SECRETE_UNIQUE_ICI"  # Changez cette clé !

class UpdateManager:
    """Gestionnaire de mises à jour sécurisées"""
    
    def __init__(self, kb_path):
        self.kb_path = Path(kb_path)
        self.backup_dir = self.kb_path.parent / 'backups'
        self.backup_dir.mkdir(exist_ok=True)
    
    def create_update_package(self, new_kb_data, version_info):
        """
        Crée un package de mise à jour signé
        
        Args:
            new_kb_data: Dictionnaire contenant la nouvelle base de connaissances
            version_info: Informations sur la version (dict)
        
        Returns:
            dict: Package de mise à jour avec signature
        """
        # Préparer le package
        package = {
            'timestamp': datetime.now().isoformat(),
            'version': version_info.get('version', '1.0.0'),
            'description': version_info.get('description', 'Mise à jour de la base de connaissances'),
            'author': version_info.get('author', 'Administrateur'),
            'data': new_kb_data
        }
        
        # Sérialiser les données
        data_string = json.dumps(package['data'], sort_keys=True)
        
        # Créer la signature HMAC
        signature = self._generate_signature(data_string)
        package['signature'] = signature
        
        return package
    
    def _generate_signature(self, data_string):
        """Génère une signature HMAC-SHA256"""
        return hmac.new(
            SECRET_KEY.encode('utf-8'),
            data_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
    
    def verify_signature(self, package):
        """
        Vérifie la signature d'un package de mise à jour
        
        Returns:
            bool: True si la signature est valide
        """
        if 'signature' not in package or 'data' not in package:
            return False
        
        # Recréer la signature
        data_string = json.dumps(package['data'], sort_keys=True)
        expected_signature = self._generate_signature(data_string)
        
        # Comparaison sécurisée
        return hmac.compare_digest(expected_signature, package['signature'])
    
    def create_backup(self):
        """Crée une sauvegarde de la base actuelle"""
        if not self.kb_path.exists():
            return None
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f'kb_backup_{timestamp}.json'
        
        with open(self.kb_path, 'r', encoding='utf-8') as f:
            current_kb = json.load(f)
        
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(current_kb, f, ensure_ascii=False, indent=2)
        
        return backup_path
    
    def apply_update(self, update_package_path):
        """
        Applique une mise à jour depuis un fichier package
        
        Args:
            update_package_path: Chemin vers le fichier .update
        
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Charger le package
            with open(update_package_path, 'r', encoding='utf-8') as f:
                package = json.load(f)
            
            # Vérifier la signature
            if not self.verify_signature(package):
                return False, "❌ Signature invalide. Le fichier de mise à jour n'est pas authentique."
            
            # Créer une sauvegarde
            backup_path = self.create_backup()
            if backup_path:
                print(f"✅ Sauvegarde créée : {backup_path}")
            
            # Appliquer la mise à jour
            with open(self.kb_path, 'w', encoding='utf-8') as f:
                json.dump(package['data'], f, ensure_ascii=False, indent=2)
            
            # Message de succès
            message = f"""
✅ Mise à jour appliquée avec succès !

📋 Informations :
  - Version : {package['version']}
  - Date : {package['timestamp']}
  - Description : {package['description']}
  - Auteur : {package['author']}

💾 Sauvegarde : {backup_path}
            """
            
            return True, message
            
        except json.JSONDecodeError:
            return False, "❌ Fichier de mise à jour corrompu (JSON invalide)"
        except Exception as e:
            return False, f"❌ Erreur lors de la mise à jour : {str(e)}"
    
    def list_backups(self):
        """Liste toutes les sauvegardes disponibles"""
        backups = sorted(self.backup_dir.glob('kb_backup_*.json'), reverse=True)
        return backups
    
    def restore_backup(self, backup_path):
        """
        Restaure une sauvegarde
        
        Args:
            backup_path: Chemin vers le fichier de sauvegarde
        
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            # Créer une sauvegarde avant restauration
            self.create_backup()
            
            # Restaurer
            with open(self.kb_path, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, ensure_ascii=False, indent=2)
            
            return True, f"✅ Sauvegarde restaurée : {backup_path}"
            
        except Exception as e:
            return False, f"❌ Erreur lors de la restauration : {str(e)}"


def create_update_file():
    """
    Script interactif pour créer un fichier de mise à jour
    """
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   Création d'un Package de Mise à Jour                       ║
║   Système Expert - Droit du Numérique                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Charger la base actuelle ou nouvelle
    kb_path = input("Chemin vers la nouvelle base de connaissances (.json) : ").strip()
    
    if not Path(kb_path).exists():
        print("❌ Fichier introuvable")
        return
    
    try:
        with open(kb_path, 'r', encoding='utf-8') as f:
            new_kb = json.load(f)
    except Exception as e:
        print(f"❌ Erreur de lecture : {e}")
        return
    
    # Informations sur la version
    print("\n📋 Informations sur la mise à jour :")
    version = input("Version (ex: 1.1.0) : ").strip() or "1.0.0"
    description = input("Description : ").strip() or "Mise à jour de la base de connaissances"
    author = input("Auteur : ").strip() or "Administrateur"
    
    version_info = {
        'version': version,
        'description': description,
        'author': author
    }
    
    # Créer le package
    manager = UpdateManager('data/legal_expert_system_kb.json')
    package = manager.create_update_package(new_kb, version_info)
    
    # Sauvegarder le package
    output_file = f"update_v{version.replace('.', '_')}.update"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(package, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Package de mise à jour créé : {output_file}")
    print(f"📦 Taille : {Path(output_file).stat().st_size / 1024:.2f} KB")
    print(f"🔐 Signature : {package['signature'][:16]}...")
    print("\n💡 Distribuez ce fichier .update aux utilisateurs")


def apply_update_interactive():
    """
    Script interactif pour appliquer une mise à jour
    """
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   Application d'une Mise à Jour                              ║
║   Système Expert - Droit du Numérique                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    update_file = input("Chemin vers le fichier de mise à jour (.update) : ").strip()
    
    if not Path(update_file).exists():
        print("❌ Fichier introuvable")
        return
    
    kb_path = 'data/legal_expert_system_kb.json'
    manager = UpdateManager(kb_path)
    
    print("\n🔍 Vérification de la mise à jour...")
    success, message = manager.apply_update(update_file)
    
    print(message)
    
    if success:
        print("\n💡 Conseil : Redémarrez l'application pour utiliser la nouvelle version")


def manage_backups():
    """
    Script interactif pour gérer les sauvegardes
    """
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   Gestion des Sauvegardes                                    ║
║   Système Expert - Droit du Numérique                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    kb_path = 'data/legal_expert_system_kb.json'
    manager = UpdateManager(kb_path)
    
    backups = manager.list_backups()
    
    if not backups:
        print("📁 Aucune sauvegarde disponible")
        return
    
    print(f"\n📦 {len(backups)} sauvegarde(s) disponible(s) :\n")
    
    for i, backup in enumerate(backups, 1):
        size = backup.stat().st_size / 1024
        mtime = datetime.fromtimestamp(backup.stat().st_mtime)
        print(f"  {i}. {backup.name}")
        print(f"     Taille: {size:.2f} KB | Date: {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\n")
    choice = input("Numéro de la sauvegarde à restaurer (ou Enter pour annuler) : ").strip()
    
    if not choice:
        print("Annulé")
        return
    
    try:
        index = int(choice) - 1
        if 0 <= index < len(backups):
            backup_path = backups[index]
            confirm = input(f"\n⚠️  Confirmer la restauration de {backup_path.name} ? (oui/non) : ").strip().lower()
            
            if confirm == 'oui':
                success, message = manager.restore_backup(backup_path)
                print(message)
                if success:
                    print("\n💡 Redémarrez l'application pour utiliser la version restaurée")
            else:
                print("Annulé")
        else:
            print("❌ Numéro invalide")
    except ValueError:
        print("❌ Entrée invalide")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("""
Usage:
    python update_manager.py create    - Créer un package de mise à jour
    python update_manager.py apply     - Appliquer une mise à jour
    python update_manager.py backup    - Gérer les sauvegardes
        """)
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'create':
        create_update_file()
    elif command == 'apply':
        apply_update_interactive()
    elif command == 'backup':
        manage_backups()
    else:
        print(f"❌ Commande inconnue : {command}")