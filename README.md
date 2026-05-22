# FJIFE 2026 - Automatic Certificate Generator

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)

## 🎯 Purpose

This Python script automates the generation of customized participation certificates for AIESEC events. It automatically overlays participant names and unique certificate numbers onto a certificate template.

## ✨ Features

- **Automatic Generation**: Creates certificates for all participants using a CSV file.
- **Unique Numbering**: Automatically assigns a unique certificate number to each participant.
- **Easy Customization**: Tweak text position, size, and color to fit your needs.
- **HD Image Support**: Compatible with high-resolution PNG/JPG templates.
- **Auto-Centering**: Centers text automatically based on specified coordinates.
- **PowerPoint Export**: Compiles all certificates into a print-ready PPT presentation.
- **CMYK Conversion**: Converts images to CMYK for professional-grade printing.
- **A4 Layout**: Centers certificates on landscape A4 pages with white margins.

## 📋 Prerequisites

- Python 3.8 or higher
- Required Python libraries:
  ```bash
  pip install pillow pandas python-pptx img2pdf
  ```

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com
   cd fjife-attestation-generator
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure

``
fjife-attestation-generator/
├── attestation_generator_script.py    # Main generation script
├── test_position.py                   # Quick test script (1 certificate)
├── create_ppt.py                      # PowerPoint presentation builder
├── convert_to_cmyk.py                 # RGB → CMYK conversion for printers
├── create_a4_pdf.py                   # Print-ready landscape A4 PDF maker
├── FJIFE_Attestation_participants_LV.png  # Certificate template
├── FJIFE – Attestations_Participants - Feuille 1.csv  # Participant list
├── Montserrat-BoldItalic.ttf          # Font for names
├── Montserrat-Regular.ttf             # Font for numbers
├── output/                            # Generated certificates (PNG)
├── output_cmyk/                       # CMYK certificates (TIFF)
├── output_a4/                         # A4 format certificates (PNG)
├── requirements.txt                   # Python dependencies
└── README.md                          # Documentation
```
## 🎨 Customization

### Modifying the Template

Replace `FJIFE_Attestation_participants_LV.png` with your own template image file.

### Adjusting Text Placement

Edit the following variables inside `attestation_generator_script.py`:

```python
# Name positioning coordinates (X, Y)
NAME_X = 2590
NAME_Y = 1024

# Certificate number positioning coordinates (X, Y)
CERT_NUMBER_X = 1760
CERT_NUMBER_Y = 760

# Font sizes
FONT_SIZE = 96
CERT_FONT_SIZE = 76

# Text color values (R, G, B, A)
TEXT_COLOR = (0, 0, 0, 0)  # Transparent
```

### CSV File Formatting

Your CSV file must include a `Nom` column containing the participant names:

```csv
Nom
KABORE Wendkouni Albertine
BATIANA Abdoul Aziz
ZONGO Ardjouma Doriane
...
```

> **Note**: To ensure data privacy, CSV files are excluded from version control. Use `participants_example.csv` as a structural blueprint.

## 📝 Usage Instructions

### 1. Generate Certificates

```bash
python3 attestation_generator_script.py
```

The output files will save directly to the `output/` directory.

### 2. Test Text Placement (Optional)

```bash
python3 test_position.py
```

Generates `test_position.png` so you can visually verify the layout before running the full batch.

### 3. Build a PowerPoint Slideshow

```bash
python3 create_ppt.py
```

Compiles `FJIFE26_Attestations_Ready_to_Print.pptx` with exactly one slide per certificate.

### 4. Convert to CMYK (For Professional Print Shops)

```bash
python3 convert_to_cmyk.py
```

Converts images to CMYK color profiles and builds a multi-page file:
- `output_cmyk/` — Contains CMYK TIFF files (300 DPI)
- `FJIFE26_Attestations_CMJN_Ready_to_Print.pdf`

### 5. Generate Layout-Ready A4 PDFs

```bash
python3 create_a4_pdf.py
```

Creates `FJIFE26_Attestations_A4_Ready_to_Print.pdf`:
- Standard landscape A4 format (297×210 mm)
- Centered certificates surrounded by clean white margins
- High-definition 300 DPI resolution ready for production

## 🤝 Contributing

Contributions make the open-source community thrive! You can help by:

- 🐛 Reporting software bugs
- 💡 Proposing new functionality
- 📚 Enhancing documentation layouts
- 🔧 Submitting code pull requests

### How to Contribute

1. Fork the project repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your modifications (`git commit -m 'Add some AmazingFeature'`).
4. Push to your branch (`git push origin feature/AmazingFeature`).
5. Open a formal Pull Request.

## 📄 Certificate Serial Format

Serial identification numbers auto-generate using this sequence format:
N°AiKDG26.27-FJIFE2026A001N°AiKDG26.27-FJIFE2026A002...
You can alter this configuration string in the script by modifying this code block:
```python
cert_number = f"N°AiKDG26.27-FJIFE2026A{index + 1:03d}"
```

## 🔧 Advanced Configuration

### Certificate Number Typography

By default, serial numbers use `Montserrat-Regular.ttf` while names render in `Montserrat-BoldItalic.ttf`:

```python
FONT_PATH = "Montserrat-BoldItalic.ttf"      # Primary font choice for names
CERT_FONT_PATH = "Montserrat-Regular.ttf"    # Primary font choice for IDs
```

### Changing System Fonts

Replace `Montserrat-BoldItalic.ttf` with any custom asset file matching `.ttf` or `.otf` format extensions.

### RGB Color Presets

- **Black**: `(0, 0, 0)`
- **White**: `(255, 255, 255)`
- **AIESEC Blue**: `(3, 126, 243)`
- **Transparent**: `(0, 0, 0, 0)` — Use this setting if text placeholders exist on the template and you only need to match positions.

## 📜 License

This software project is licensed under the terms of the MIT License - check out the [LICENSE](LICENSE) file for complete terms.

## 👨‍💻 Author

**Sanon A Ben** - *Python Developer* - Sabf226

## 🙏 Acknowledgments

- AIESEC for providing workflow inspiration and development opportunities.
- The global Python ecosystem for maintaining the excellent PIL and Pandas libraries.

## 📞 Support Channels

If you run into issues or have questions:
- Open an official issue ticket directly on GitHub.
- Contact the author through direct channels.

---

## 🖨️ Recommended Production Workflow

1. **Batch Generate** all graphics assets (`python3 attestation_generator_script.py`)
2. **Visually Inspect** layout placements (`test_position.png`)
3. **Compile Layouts** to clean A4 document media (`python3 create_a4_pdf.py`)
4. **Deliver** the output PDF file to your local print provider.

> **Pro Tip**: If your print house specifically requests CMYK files, run `convert_to_cmyk.py` to produce native CMYK PDF assets.

---

**Note**: This script was intentionally built for the FJIFE 2026 event setup but adapts effortlessly to other target applications.
