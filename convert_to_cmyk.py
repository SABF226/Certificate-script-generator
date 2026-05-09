# =========================================================
# FJIFE 2026 — Conversion CMJN pour Impression Professionnelle
# Convertit les attestations RGB en CMYK ( TIFF + PDF )
# =========================================================

import subprocess
import glob
import os

# =========================================================
# CONFIGURATION
# =========================================================

INPUT_FOLDER = "output"
OUTPUT_FOLDER = "output_cmyk"
PDF_FILENAME = "FJIFE26_Attestations_CMJN_Ready_to_Print.pdf"

# Qualité de compression TIFF (LZW = sans perte, recommandé pour impression)
TIFF_COMPRESSION = "LZW"

# =========================================================
# CRÉATION DU DOSSIER DE SORTIE
# =========================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Récupérer les images triées
image_paths = sorted(glob.glob(os.path.join(INPUT_FOLDER, "*.png")))

if not image_paths:
    print(f"Aucune image trouvée dans '{INPUT_FOLDER}/'")
    exit(1)

print(f"Images à convertir : {len(image_paths)}")
print("Conversion RGB → CMYK en cours...\n")

# =========================================================
# ÉTAPE 1 : CONVERTIR CHAQUE IMAGE EN TIFF CMYK
# =========================================================

tiff_paths = []

for img_path in image_paths:
    basename = os.path.basename(img_path).replace(".png", "")
    tiff_path = os.path.join(OUTPUT_FOLDER, f"{basename}.tiff")
    tiff_paths.append(tiff_path)

    # Commande ImageMagick : RGB → CMYK + compression LZW
    cmd = [
        "convert",
        img_path,
        "-colorspace", "CMYK",
        "-compress", TIFF_COMPRESSION,
        "-density", "300",           # 300 DPI pour impression haute qualité
        tiff_path
    ]

    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  CMJN : {basename}.tiff")

print(f"\n{len(tiff_paths)} fichiers TIFF CMJN générés dans '{OUTPUT_FOLDER}/'")

# =========================================================
# ÉTAPE 2 : CRÉER UN PDF CMJN MULTI-PAGES (optionnel)
# =========================================================

print(f"\nCréation du PDF CMJN : {PDF_FILENAME}")

cmd_pdf = [
    "convert",
    *tiff_paths,
    "-colorspace", "CMYK",
    "-compress", "zip",
    "-density", "300",
    PDF_FILENAME
]

subprocess.run(cmd_pdf, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"\nFichier PDF CMJN créé : {PDF_FILENAME}")
print(f"  Pages        : {len(tiff_paths)}")
print(f"  Color space  : CMYK (Cyan, Magenta, Jaune, Noir)")
print(f"  Résolution   : 300 DPI")
print(f"  Format       : A4 paysage pleine page")
print("\nCe fichier est prêt à être envoyé à l'imprimeur.")
