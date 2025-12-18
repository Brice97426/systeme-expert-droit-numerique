# ============================================
# run.sh (Linux/macOS)
# ============================================
#!/bin/bash

echo "========================================"
echo "Système Expert - Droit du Numérique"
echo "========================================"
echo ""
echo "Démarrage de l'application..."
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null
then
    echo "❌ ERREUR : Python 3 n'est pas installé"
    echo "Installez Python 3 avec votre gestionnaire de paquets"
    exit 1
fi

# Démarrer l'application
python3 main.py

# Vérifier le code de sortie
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ ERREUR : Impossible de démarrer l'application"
    echo "Vérifiez les logs ci-dessus pour plus d'informations"
    exit 1
fi