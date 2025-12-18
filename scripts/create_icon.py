"""
Script pour créer une icône simple pour l'application
Nécessite Pillow : pip install Pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("❌ Pillow n'est pas installé.")
    print("Installez-le avec : pip install Pillow")
    exit(1)

def create_icon():
    """Crée une icône 256x256 avec le symbole ⚖️"""
    
    # Créer une image avec fond dégradé
    size = 256
    image = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(image)
    
    # Fond dégradé bleu
    for y in range(size):
        # Dégradé du bleu foncé au bleu clair
        r = int(30 + (y / size) * 70)
        g = int(60 + (y / size) * 130)
        b = int(114 + (y / size) * 80)
        draw.rectangle([(0, y), (size, y+1)], fill=(r, g, b))
    
    # Dessiner un cercle blanc au centre
    margin = 30
    draw.ellipse(
        [(margin, margin), (size-margin, size-margin)],
        fill='white',
        outline=(30, 60, 114),
        width=5
    )
    
    # Essayer d'ajouter le texte "⚖️"
    try:
        # Tenter d'utiliser une police système
        font = ImageFont.truetype("segoeui.ttf", 140)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 140)
        except:
            # Utiliser la police par défaut si aucune police n'est trouvée
            font = ImageFont.load_default()
            print("⚠️ Police par défaut utilisée (qualité réduite)")
    
    # Dessiner le symbole de balance
    text = "⚖"
    
    # Centrer le texte
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - 10
    
    # Dessiner le texte
    draw.text((x, y), text, fill=(30, 60, 114), font=font)
    
    # Sauvegarder en différents formats
    # ICO pour Windows
    image.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    print("✅ Icône créée : icon.ico")
    
    # PNG pour autres usages
    image.save('icon.png', format='PNG')
    print("✅ Icône créée : icon.png")
    
    # Créer aussi une version pour macOS
    image.save('icon.icns', format='ICNS')
    print("✅ Icône créée : icon.icns (macOS)")
    
    print("\n🎨 Icônes créées avec succès !")
    print("Vous pouvez maintenant compiler avec PyInstaller.")

if __name__ == '__main__':
    create_icon()