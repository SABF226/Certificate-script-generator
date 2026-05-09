# FJIFE 2026 - Générateur Automatique d'Attestations

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)

## 🎯 Objectif

Ce script Python automatise la génération d'attestations de participation personnalisées pour les événements AIESEC. Il ajoute automatiquement les noms des participants et des numéros d'attestation uniques sur un template d'attestation.

## ✨ Fonctionnalités

- **Génération automatique** : Crée des attestations pour tous les participants à partir d'un fichier CSV
- **Numérotation unique** : Attribue automatiquement un numéro d'attestation unique à chaque participant
- **Personnalisation facile** : Ajustez la position, la taille et la couleur du texte selon vos besoins
- **Support des images HD** : Compatible avec les templates PNG/JPG haute résolution
- **Centrage automatique** : Le texte est automatiquement centré selon les coordonnées spécifiées
- **Export PowerPoint** : Rassemble toutes les attestations en une présentation PPT prête à imprimer
- **Conversion CMJN** : Convertit les images en CMYK pour une impression professionnelle de qualité
- **Format A4** : Centre les attestations sur des pages A4 paysage avec marges blanches

## 📋 Prérequis

- Python 3.8 ou supérieur
- Bibliothèques Python :
  ```bash
  pip install pillow pandas python-pptx img2pdf
  ```

## 🚀 Installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/votre-username/fjife-attestation-generator.git
   cd fjife-attestation-generator
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Structure du projet

```
fjife-attestation-generator/
├── attestation_generator_script.py    # Script principal de génération
├── test_position.py                   # Script de test rapide (1 attestation)
├── create_ppt.py                      # Créateur de présentation PowerPoint
├── convert_to_cmyk.py                 # Conversion RGB → CMJN pour imprimeur
├── create_a4_pdf.py                   # PDF A4 paysage prêt à imprimer
├── FJIFE_Attestation_participants_LV.png  # Template d'attestation
├── FJIFE – Attestations_Participants - Feuille 1.csv  # Liste des participants
├── Montserrat-BoldItalic.ttf          # Police des noms
├── Montserrat-Regular.ttf             # Police des numéros
├── output/                            # Attestations générées (PNG)
├── output_cmyk/                       # Attestations en CMJN (TIFF)
├── output_a4/                         # Attestations format A4 (PNG)
├── requirements.txt                   # Dépendances Python
└── README.md                          # Documentation
```

## 🎨 Personnalisation

### Modifier le template

Remplacez `FJIFE_Attestation_participants_LV.png` par votre propre template.

### Ajuster la position du texte

Éditez les variables dans `attestation_generator_script.py` :

```python
# Position du nom (X, Y)
NAME_X = 2590
NAME_Y = 1024

# Position du numéro d'attestation (X, Y)
CERT_NUMBER_X = 1760
CERT_NUMBER_Y = 760

# Taille de police
FONT_SIZE = 96
CERT_FONT_SIZE = 76

# Couleur du texte (R, G, B, A)
TEXT_COLOR = (0, 0, 0, 0)  # Transparent
```

### Format du fichier CSV

Le fichier CSV doit contenir une colonne `Nom` avec les noms des participants :

```csv
Nom
KABORE Wendkouni Albertine
BATIANA Abdoul Aziz
ZONGO Ardjouma Doriane
...
```

> **Note** : Pour la protection des données personnelles, les fichiers CSV ne sont pas versionnés. Utilisez `participants_example.csv` comme modèle.

## 📝 Utilisation

### 1. Générer les attestations

```bash
python3 attestation_generator_script.py
```

Les attestations seront sauvegardées dans `output/`.

### 2. Tester le positionnement (facultatif)

```bash
python3 test_position.py
```

Génère `test_position.png` pour vérifier la position du texte avant de tout lancer.

### 3. Créer un PowerPoint

```bash
python3 create_ppt.py
```

Crée `FJIFE26_Attestations_Ready_to_Print.pptx` avec 1 slide par attestation.

### 4. Conversion CMJN (impression pro)

```bash
python3 convert_to_cmyk.py
```

Convertit les images en CMYK et crée un PDF multi-pages :
- `output_cmyk/` — TIFF CMJN (300 DPI)
- `FJIFE26_Attestations_CMJN_Ready_to_Print.pdf`

### 5. PDF A4 pour imprimeur

```bash
python3 create_a4_pdf.py
```

Crée `FJIFE26_Attestations_A4_Ready_to_Print.pdf` :
- Format A4 paysage (297×210 mm)
- Attestations centrées avec marges blanches
- 300 DPI, prêt à imprimer

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment vous pouvez aider :

- 🐛 Signaler des bugs
- 💡 Suggérer de nouvelles fonctionnalités
- 📚 Améliorer la documentation
- 🔧 Soumettre des pull requests

### Comment contribuer

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Format des numéros d'attestation

Les numéros d'attestation sont générés automatiquement au format :
```
N°AiKDG26.27-FJIFE2026A001
N°AiKDG26.27-FJIFE2026A002
...
```

Vous pouvez modifier ce format dans le script en changeant la ligne :
```python
cert_number = f"N°AiKDG26.27-FJIFE2026A{index + 1:03d}"
```

## 🔧 Configuration avancée

### Police du numéro d'attestation

Par défaut, le numéro d'attestation utilise `Montserrat-Regular.ttf` tandis que le nom utilise `Montserrat-BoldItalic.ttf` :

```python
FONT_PATH = "Montserrat-BoldItalic.ttf"      # Police du nom
CERT_FONT_PATH = "Montserrat-Regular.ttf"    # Police du numéro
```

### Changer la police

Remplacez `Montserrat-BoldItalic.ttf` par votre propre fichier de police (.ttf ou .otf).

### Couleurs RGB

- **Noir** : `(0, 0, 0)`
- **Blanc** : `(255, 255, 255)`
- **Bleu AIESEC** : `(3, 126, 243)`
- **Transparent** : `(0, 0, 0, 0)` — à utiliser si le texte est déjà présent sur le template et que vous souhaitez superposer par-dessus

## 📜 License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteur

**[Votre Nom]** - *Développeur Python* - [Votre GitHub]

## 🙏 Remerciements

- AIESEC pour l'inspiration et l'opportunité
- La communauté Python pour les excellentes bibliothèques PIL/Pandas

## 📞 Support

Pour toute question ou problème, n'hésitez pas à :
- Ouvrir une issue sur GitHub
- Contacter l'auteur directement

---

## 🖨️ Workflow d'impression recommandé

1. **Générer** les attestations (`python3 attestation_generator_script.py`)
2. **Vérifier** visuellement le rendu (`test_position.png`)
3. **Exporter** en PDF A4 (`python3 create_a4_pdf.py`)
4. **Envoyer** le fichier PDF à l'imprimeur

> **Astuce** : Si l'imprimeur demande du CMJN, utilisez `convert_to_cmyk.py` pour obtenir un PDF en CMYK.

---

**Note** : Ce script a été développé pour l'événement FJIFE 2026 mais peut être facilement adapté pour d'autres événements.
