# =========================================================
# FJIFE 2026 — Générateur Automatique d’Attestations
# =========================================================
# OBJECTIF :
# Ajouter automatiquement les noms des participants
# sur votre nouveau template d’attestation.
#
# FORMAT CONSEILLÉ :
# - Template en PNG ou JPG HD
# - Liste des participants dans un fichier CSV
#
# STRUCTURE DOSSIER :
#
# projet/
# ├── template.png
# ├── participants.csv
# ├── generate_attestations.py
# └── output/
#
# INSTALLATION :
# pip install pillow pandas
#
# =========================================================

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# =========================================================
# CONFIGURATION
# =========================================================

TEMPLATE_PATH = "FJIFE_Attestation_participants_LV.png"
OUTPUT_FOLDER = "output"

# Police
FONT_PATH = "Montserrat-BoldItalic.ttf"  # Remplacer si besoin
FONT_SIZE = 96
CERT_FONT_SIZE = 76  # Taille de police pour le numéro d'attestation

# Couleurs FJIFE
TEXT_COLOR = (0, 0, 0, 0)  # Transparent

# Position du nom sur le template
# Ajuster selon votre design (image 4x plus grande)
NAME_X = 2590
NAME_Y = 1024

# Position du numéro d'attestation
CERT_NUMBER_X = 1760
CERT_NUMBER_Y = 760

# =========================================================
# CRÉATION DOSSIER OUTPUT
# =========================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# =========================================================
# CHARGEMENT DES PARTICIPANTS
# =========================================================

# participants.csv doit contenir :
# Nom

participants = pd.read_csv("FJIFE – Attestations_Participants - Feuille 1.csv")

# =========================================================
# CHARGEMENT POLICE
# =========================================================

font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
cert_font = ImageFont.truetype(FONT_PATH, CERT_FONT_SIZE)

# =========================================================
# GÉNÉRATION DES ATTESTATIONS
# =========================================================

for index, row in participants.iterrows():

    participant_name = row["Nom"]

    # Génération du numéro d'attestation unique
    cert_number = f"N°AiKDG26.27-FJIFE2026A{index + 1:03d}"

    # Ouvrir le template
    image = Image.open(TEMPLATE_PATH)

    draw = ImageDraw.Draw(image)

    # Centrage automatique du texte pour le nom
    bbox = draw.textbbox((0, 0), participant_name, font=font)

    text_width = bbox[2] - bbox[0]

    centered_x = NAME_X - (text_width // 2)

    # Ajouter le nom
    draw.text(
        (centered_x, NAME_Y),
        participant_name,
        fill=TEXT_COLOR,
        font=font
    )

    # Centrage automatique du texte pour le numéro d'attestation
    cert_bbox = draw.textbbox((0, 0), cert_number, font=cert_font)
    cert_width = cert_bbox[2] - cert_bbox[0]
    centered_cert_x = CERT_NUMBER_X - (cert_width // 2)

    # Ajouter le numéro d'attestation
    draw.text(
        (centered_cert_x, CERT_NUMBER_Y),
        cert_number,
        fill=TEXT_COLOR,
        font=cert_font
    )

    # Nom du fichier exporté (nettoyer le nom pour éviter les caractères invalides)
    safe_name = participant_name.replace(".", "").replace("/", "").replace("\\", "")
    output_path = f"{OUTPUT_FOLDER}/{safe_name}.png"

    # Sauvegarde
    image.save(output_path)

    print(f"Attestation générée : {participant_name} ({cert_number})")

print("\nToutes les attestations ont été générées avec succès.")