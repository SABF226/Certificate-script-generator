from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Configuration (même que le script principal)
TEMPLATE_PATH = "FJIFE_Attestation_participants_LV.png"
SIGNATURE_PATH = "signature.png"
FONT_PATH = "Montserrat-BoldItalic.ttf"
FONT_SIZE = 96
CERT_FONT_SIZE = 76
TEXT_COLOR = (0, 0, 0, 0)
NAME_X = 2590
NAME_Y = 1024
CERT_NUMBER_X = 1760
CERT_NUMBER_Y = 760
SIGNATURE_MARGIN_X = 500  # Marge horizontale en pixels
SIGNATURE_MARGIN_Y = 120  # Marge verticale en pixels

# Charger le premier participant
participants = pd.read_csv("FJIFE – Attestations_Participants - Feuille 1.csv")
participant_name = participants.iloc[45]["Nom"]

# Génération du numéro d'attestation unique
cert_number = f"N°AiKDG26.27-FJIFE2026A0046"

# Charger la police
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
cert_font = ImageFont.truetype(FONT_PATH, CERT_FONT_SIZE)

# Charger le cachet signature
signature = Image.open(SIGNATURE_PATH)

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

# Ajouter le cachet signature en bas à droite
signature_x = image.width - signature.width - SIGNATURE_MARGIN_X
signature_y = image.height - signature.height - SIGNATURE_MARGIN_Y
image.paste(signature, (signature_x, signature_y), signature)

# Sauvegarder le test
image.save("test_position.png")
print(f"Test généré pour: {participant_name}")
print(f"Numéro d'attestation: {cert_number}")
print("Vérifiez le fichier test_position.png")
