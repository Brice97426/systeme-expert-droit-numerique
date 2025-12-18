import sys
import os
import json
import webbrowser
import threading
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from tkinter import Tk, messagebox

class LegalExpertSystem:
    """Moteur d'inférence du système expert"""
    
    def __init__(self, kb_path):
        self.kb = self.load_knowledge_base(kb_path)
        self.user_answers = {}
        
    def load_knowledge_base(self, path):
        """Charge la base de connaissances JSON"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erreur lors du chargement de la base de connaissances: {e}")
            sys.exit(1)
    
    def evaluate_condition(self, condition):
        """Évalue une condition de règle"""
        if not isinstance(condition, dict):
            return False
            
        critere_id = condition.get('id')
        valeur_attendue = condition.get('valeur')
        
        if critere_id not in self.user_answers:
            return None  # Non répondu
            
        valeur_reponse = self.user_answers[critere_id]
        return valeur_reponse == valeur_attendue
    
    def evaluate_rule(self, rule):
        """Évalue une règle complète"""
        if not rule.get('active', True):
            return False
            
        conditions = rule.get('conditions', {})
        operateur = conditions.get('operateur', 'ET')
        criteres = conditions.get('criteres', [])
        
        if not criteres:
            return False
        
        results = []
        for cond in criteres:
            result = self.evaluate_condition(cond)
            if result is None:
                return None  # Incomplet
            results.append(result)
        
        if operateur == 'ET':
            return all(results)
        elif operateur == 'OU':
            return any(results)
        
        return False
    
    def find_matching_rules(self):
        """Trouve toutes les règles qui correspondent aux réponses"""
        matching_decisions = []
        
        for rule in self.kb.get('regles', []):
            evaluation = self.evaluate_rule(rule)
            
            if evaluation is True:
                decision_id = rule.get('decision')
                decision = self.get_decision_by_id(decision_id)
                
                if decision:
                    matching_decisions.append({
                        'rule': rule,
                        'decision': decision,
                        'confiance': rule.get('confiance', 0.5)
                    })
        
        # Tri par priorité et confiance
        matching_decisions.sort(
            key=lambda x: (x['rule'].get('priorite', 999), -x['confiance'])
        )
        
        return matching_decisions
    
    def get_decision_by_id(self, decision_id):
        """Récupère une décision par son ID"""
        for decision in self.kb.get('decisions', []):
            if decision.get('id') == decision_id:
                return decision
        return None
    
    def get_applicable_criteria(self):
        """Retourne les critères applicables selon les réponses"""
        applicable = []
        
        for critere in self.kb.get('criteres', []):
            # Vérifier si le critère a une condition
            condition = critere.get('condition')
            
            if condition:
                # Évaluer la condition (format: "C1 == true")
                try:
                    condition_met = eval(condition, {"__builtins__": {}}, self.user_answers)
                    if condition_met:
                        applicable.append(critere)
                except:
                    pass
            else:
                # Pas de condition, toujours applicable
                applicable.append(critere)
        
        return applicable


class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Handler HTTP personnalisé pour servir l'application"""
    
    def __init__(self, *args, directory=None, **kwargs):
        self.expert_system = kwargs.pop('expert_system', None)
        super().__init__(*args, directory=directory, **kwargs)
    
    def do_POST(self):
        """Gère les requêtes POST pour l'analyse"""
        if self.path == '/analyze':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                self.expert_system.user_answers = data.get('answers', {})
                
                # Effectuer l'analyse
                results = self.expert_system.find_matching_rules()
                
                # Préparer la réponse
                response = {
                    'success': True,
                    'decisions': [
                        {
                            'rule_id': r['rule']['id'],
                            'rule_name': r['rule']['nom'],
                            'decision': r['decision'],
                            'confiance': r['confiance']
                        }
                        for r in results
                    ],
                    'metadata': self.expert_system.kb.get('metadata', {}),
                    'avertissement': self.expert_system.kb.get('avertissement', {})
                }
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                
            except Exception as e:
                self.send_error(500, f"Erreur serveur: {str(e)}")
        
        elif self.path == '/kb':
            # Envoyer la base de connaissances
            try:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(self.expert_system.kb, ensure_ascii=False).encode('utf-8'))
            except Exception as e:
                self.send_error(500, f"Erreur serveur: {str(e)}")
        else:
            self.send_error(404)
    
    def do_GET(self):
        """Gère les requêtes GET"""
        if self.path == '/kb':
            # Envoyer la base de connaissances
            try:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(self.expert_system.kb, ensure_ascii=False).encode('utf-8'))
                return
            except Exception as e:
                self.send_error(500, f"Erreur serveur: {str(e)}")
                return
        
        # Comportement par défaut pour les autres fichiers
        super().do_GET()
    
    def log_message(self, format, *args):
        """Supprime les logs de console"""
        pass


def start_server(kb_path, port=8080):
    """Démarre le serveur HTTP local"""
    
    # Obtenir le répertoire de l'application
    if getattr(sys, 'frozen', False):
        # Mode exécutable PyInstaller
        app_dir = Path(sys._MEIPASS)
    else:
        # Mode développement
        app_dir = Path(__file__).parent
    
    # Créer le système expert
    expert_system = LegalExpertSystem(kb_path)
    
    # Changer le répertoire de travail
    os.chdir(app_dir)
    
    # Créer le handler avec le système expert
    def handler(*args, **kwargs):
        CustomHTTPRequestHandler(*args, directory=str(app_dir), 
                                expert_system=expert_system, **kwargs)
    
    # Démarrer le serveur
    server = HTTPServer(('localhost', port), handler)
    
    print(f"✓ Serveur démarré sur http://localhost:{port}")
    print(f"✓ Base de connaissances chargée: {kb_path}")
    print(f"✓ Nombre de règles: {len(expert_system.kb.get('regles', []))}")
    print(f"✓ Ouverture du navigateur...")
    
    # Ouvrir le navigateur
    def open_browser():
        import time
        time.sleep(1)
        webbrowser.open(f'http://localhost:{port}/index.html')
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Lancer le serveur
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Serveur arrêté")
        server.shutdown()


def main():
    """Point d'entrée principal de l'application"""
    
    # Obtenir le chemin de la base de connaissances
    if getattr(sys, 'frozen', False):
        # Mode exécutable PyInstaller
        kb_path = Path(sys._MEIPASS) / 'data' / 'legal_expert_system_kb.json'
    else:
        # Mode développement
        kb_path = Path(__file__).parent / 'data' / 'legal_expert_system_kb.json'
    
    # Vérifier l'existence de la base de connaissances
    if not kb_path.exists():
        # Interface graphique pour l'erreur
        root = Tk()
        root.withdraw()
        messagebox.showerror(
            "Erreur - Fichier manquant",
            f"La base de connaissances est introuvable:\n{kb_path}\n\n"
            "Veuillez vérifier l'installation de l'application."
        )
        sys.exit(1)
    
    # Démarrer l'application
    try:
        start_server(str(kb_path), port=8080)
    except OSError as e:
        if e.errno == 48 or e.errno == 10048:  # Port déjà utilisé
            root = Tk()
            root.withdraw()
            messagebox.showerror(
                "Erreur - Port occupé",
                "Le port 8080 est déjà utilisé.\n\n"
                "Une instance de l'application est peut-être déjà en cours d'exécution.\n"
                "Fermez l'autre instance et réessayez."
            )
            sys.exit(1)
        else:
            raise
    except Exception as e:
        root = Tk()
        root.withdraw()
        messagebox.showerror(
            "Erreur",
            f"Une erreur s'est produite:\n{str(e)}\n\n"
            "Veuillez contacter le support technique."
        )
        sys.exit(1)


if __name__ == '__main__':
    main()