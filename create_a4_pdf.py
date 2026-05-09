# =========================================================
# FJIFE 2026 — Créateur de PDF A4 Paysage pour Impression
# Centre chaque attestation sur une page A4 blanche
# =========================================================

from PIL import Image
import glob
import os

# =========================================================
# CONFIGURATION
# =========================================================

INPUT_FOLDER = "output"
OUTPUT_FOLDER = "output_a4"
PDF_FILENAME = "FJIFE26_Attestations_A4_Ready_to_Print.pdf"

# Format A4 paysage à 300 DPI
A4_WIDTH = 3508   # 297 mm × 300 DPI / 25.4
A4_HEIGHT = 2480  # 210 mm × 300 DPI / 25.4

# =========================================================
# CRÉATION DU DOSSIER DE SORTIE
# =========================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

image_paths = sorted(glob.glob(os.path.join(INPUT_FOLDER, "*.png")))

if not image_paths:
    print(f"Aucune image trouvée dans '{INPUT_FOLDER}/'")
    exit(1)

print(f"Attestations à traiter : {len(image_paths)}")
print(f"Format cible : A4 paysage ({A4_WIDTH}x{A4_HEIGHT} px @ 300 DPI)")
print("Centrage avec marges blanches...\n")

a4_images = []

for img_path in image_paths:
    basename = os.path.basename(img_path)
    
    # Charger l'attestation
    attestation = Image.open(img_path)
    attestation = attestation.convert("RGB")
    
    # Redimensionner pour tenir dans le A4 (conservation du ratio)
    att_ratio = attestation.width / attestation.height
    a4_ratio = A4_WIDTH / A4_HEIGHT
    
    if att_ratio > a4_ratio:
        # L'attestation est plus large que le A4 (ratio) → contrainte par la largeur
        new_width = A4_WIDTH
        new_height = int(A4_WIDTH / att_ratio)
    else:
        # Contrainte par la hauteur
        new_height = A4_HEIGHT
        new_width = int(A4_HEIGHT * att_ratio)
    
    attestation_resized = attestation.resize((new_width, new_height), Image.LANCZOS)
    
    # Créer la page A4 blanche
    a4_page = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), (255, 255, 255))
    
    # Calculer la position centrée
    x_offset = (A4_WIDTH - new_width) // 2
    y_offset = (A4_HEIGHT - new_height) // 2
    
    # Coller l'attestation au centre
    a4_page.paste(attestation_resized, (x_offset, y_offset))
    
    # Sauvegarder la page A4
    a4_path = os.path.join(OUTPUT_FOLDER, basename)
    a4_page.save(a4_path, dpi=(300, 300))
    a4_images.append(a4_path)
    
    print(f"  A4 : {basename}")

print(f"\n{len(a4_images)} pages A4 générées dans '{OUTPUT_FOLDER}/'")

# =========================================================
# CONVERTIR EN PDF AVEC img2pdf
# =========================================================

import subprocess

print(f"\nCréation du PDF A4 : {PDF_FILENAME}")

cmd = [
    "python3", "-m", "img2pdf",
    "--output", PDF_FILENAME,
    "--pagesize", "297mmx210mm",  # A4 paysage
    *a4_images
]

subprocess.run(cmd, check=True)

print(f"\nPDF A4 créé avec succès : {PDF_FILENAME}")
print(f"  Pages      : {len(a4_images)}")
print(f"  Format     : A4 paysage (297×210 mm)")
print(f"  Résolution : 300 DPI")
print(f"  Marges     : blanches automatiques")
print("\nFichier prêt à être envoyé à l'imprimeur.")
