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

## 📋 Prérequis

- Python 3.8 ou supérieur
- Bibliothèques Python :
  ```bash
  pip install pillow pandas
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
├── attestation_generator_script.py    # Script principal
├── FJIFE_Attestation_participants_LV.png  # Template d'attestation
├── FJIFE – Attestations_Participants - Feuille 1.csv  # Liste des participants
├── Montserrat-BoldItalic.ttf          # Police utilisée
├── output/                            # Dossier des attestations générées
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

```
Nom
KABORE Wendkouni Albertine
BATIANA Abdoul Aziz
ZONGO Ardjouma Doriane
...
```

## 📝 Utilisation

1. Préparez votre fichier CSV avec les participants
2. Placez votre template d'attestation dans le dossier
3. Ajustez les coordonnées dans le script si nécessaire
4. Exécutez le script :
   ```bash
   python3 attestation_generator_script.py
   ```

Les attestations générées seront sauvegardées dans le dossier `output/`.

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

### Changer la police

Remplacez `Montserrat-BoldItalic.ttf` par votre propre fichier de police (.ttf ou .otf).

### Couleurs RGB

- **Noir** : `(0, 0, 0)`
- **Blanc** : `(255, 255, 255)`
- **Bleu AIESEC** : `(3, 126, 243)`
- **Transparent** : `(0, 0, 0, 0)`

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

**Note** : Ce script a été développé pour l'événement FJIFE 2026 mais peut être facilement adapté pour d'autres événements.
