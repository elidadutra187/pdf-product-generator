<div align="center">
  <strong>φ</strong>
  <h1>Pdf Product Generator</h1>
  <p><em>Automated digital product generation pipeline using Python</em></p>
  <p>
    <a href="https://github.com/elidadutra187/pdf-product-generator">Repository</a> ·
    <a href="https://github.com/elidadutra187">GitHub Profile</a>
  </p>
</div>


## Positioning

This repository is part of the `φ` portfolio by [Élida Dutra](https://github.com/elidadutra187), focused on practical systems for e-commerce, automation, analytics, content generation and growth operations.

**Repository:** [elidadutra187/pdf-product-generator](https://github.com/elidadutra187/pdf-product-generator)  
**GitHub:** [https://github.com/elidadutra187](https://github.com/elidadutra187)  
**Purpose:** Automated digital product generation pipeline using Python


> Automated digital product generation pipeline using Python

## Overview

PDF Product Generator is a Python toolkit for creating professional digital products at scale. It combines ReportLab for PDF generation, Pillow for image processing, and pypdf for document manipulation.

Built for content creators and e-commerce operators who need to generate formatted PDFs, product covers, and multi-document packages programmatically.

## Stack

- **Language:** Python 3.9+
- **PDF Generation:** ReportLab
- **Image Processing:** Pillow
- **PDF Manipulation:** pypdf
- **Fonts:** Custom TTF support

## Features

- **PDF Creation:** Generate formatted documents with text, images, and styling
- **Cover Generation:** Create product covers from templates
- **Multi-Document Merging:** Combine multiple PDFs into one
- **Batch Processing:** Process multiple products in parallel
- **Template System:** Reusable document templates

## Quick Start

```bash
# Clone the repository
git clone https://github.com/elidadutra/pdf-product-generator.git
cd pdf-product-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run demo
python generate_demo.py
```

## Usage Examples

### Generate a Simple PDF

```python
from generator import PDFGenerator

pdf = PDFGenerator()
pdf.add_title("Product Guide")
pdf.add_paragraph("This is your introduction...")
pdf.add_image("images/product.jpg", width=400)
pdf.add_page_break()
pdf.add_chapter("Chapter 1: Getting Started")
pdf.save("output/guide.pdf")
```

### Create a Product Cover

```python
from covers import CoverGenerator

cover = CoverGenerator(
    width=1600,
    height=2400,
    background_color="#1a1a2e"
)
cover.add_title("The Ultimate Guide", font_size=72)
cover.add_subtitle("Everything you need to know", font_size=36)
cover.add_author("Elida Dutra")
cover.save("output/cover.png")
```

### Merge Multiple PDFs

```python
from merger import PDFMerger

merger = PDFMerger()
merger.add("cover.pdf")
merger.add("content.pdf")
merger.add("bonus.pdf")
merger.save("output/complete-product.pdf")
```

## Project Structure

```
pdf-product-generator/
├── generator/
│   ├── __init__.py
│   ├── pdf_generator.py    # Main PDF creation
│   ├── covers.py           # Cover generation
│   ├── merger.py           # PDF merging
│   └── templates.py        # Document templates
├── fonts/
│   └── .gitkeep            # Add your TTF fonts here
├── templates/
│   └── basic_ebook.py      # Template examples
├── output/
│   └── .gitkeep
├── generate_demo.py        # Demo script
├── requirements.txt
├── README.md
└── LICENSE
```

## Configuration

### PDF Settings

```python
PDF_CONFIG = {
    "page_size": "A4",  # or "LETTER", "A5", custom tuple
    "margin_top": 72,
    "margin_bottom": 72,
    "margin_left": 72,
    "margin_right": 72,
    "default_font": "Helvetica",
    "default_font_size": 12,
}
```

### Cover Settings

```python
COVER_CONFIG = {
    "width": 1600,
    "height": 2400,
    "title_font_size": 72,
    "subtitle_font_size": 36,
    "background_color": "#1a1a2e",
    "text_color": "#ffffff",
}
```

## Templates

### E-book Template

```python
from templates import EbookTemplate

template = EbookTemplate(
    title="My E-book",
    author="Elida Dutra",
    chapters=[
        {"title": "Introduction", "content": "..."},
        {"title": "Chapter 1", "content": "..."},
    ]
)
template.generate("output/ebook.pdf")
```

### Available Templates

- `EbookTemplate` - Full e-book with TOC
- `GuideTemplate` - Step-by-step guide
- `ChecklistTemplate` - Printable checklist
- `WorkbookTemplate` - Interactive workbook

## Use Cases

- **Digital Products:** E-books, guides, workbooks
- **Course Materials:** PDF handouts, certificates
- **Marketing:** Lead magnets, case studies
- **E-commerce:** Product catalogs, price lists

## Roadmap

- [ ] Interactive PDF form fields
- [ ] Table generation from CSV
- [ ] HTML to PDF conversion
- [ ] Cloud storage integration
- [ ] Template marketplace

## Author

**Élida Dutra**
Growth Engineer | E-commerce | AI Marketing Automation

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/elidadutra)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/elidadutra)

## License

MIT

---

<p align="center">
  <strong>φ</strong><br>
  <em>Building intelligent systems at the intersection of marketing, data, and AI</em>
</p>

<div align="center">
  <strong>φ</strong>
  <br />
  <sub>Built and maintained by <a href="https://github.com/elidadutra187">Élida Dutra</a>.</sub>
</div>

