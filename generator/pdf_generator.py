"""
PDF Generator using ReportLab
"""

from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from typing import Optional, Tuple, List
import os


class PDFGenerator:
    """
    Generate formatted PDF documents with text, images, and styling.

    Example:
        >>> pdf = PDFGenerator("output/guide.pdf")
        >>> pdf.add_title("My Guide")
        >>> pdf.add_paragraph("Introduction text...")
        >>> pdf.save()
    """

    def __init__(
        self,
        output_path: str = "output.pdf",
        page_size: Tuple = A4,
        margins: Tuple = (72, 72, 72, 72)  # top, right, bottom, left
    ):
        """
        Initialize PDF generator.

        Args:
            output_path: Output file path
            page_size: Page size tuple (width, height) or preset
            margins: Page margins (top, right, bottom, left) in points
        """
        self.output_path = output_path
        self.page_size = page_size
        self.margins = margins
        self.elements: List = []
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Configure custom paragraph styles."""
        # Title style
        self.styles.add(ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=28,
            spaceAfter=30,
            alignment=TA_CENTER
        ))

        # Chapter style
        self.styles.add(ParagraphStyle(
            'Chapter',
            parent=self.styles['Heading2'],
            fontSize=20,
            spaceBefore=20,
            spaceAfter=15
        ))

        # Body style
        self.styles.add(ParagraphStyle(
            'CustomBody',
            parent=self.styles['Normal'],
            fontSize=12,
            leading=18,
            alignment=TA_JUSTIFY,
            spaceAfter=12
        ))

    def add_title(self, text: str):
        """Add a centered title."""
        self.elements.append(Paragraph(text, self.styles['CustomTitle']))
        self.elements.append(Spacer(1, 0.5 * inch))

    def add_chapter(self, text: str):
        """Add a chapter heading."""
        self.elements.append(Paragraph(text, self.styles['Chapter']))

    def add_paragraph(self, text: str):
        """Add a body paragraph."""
        self.elements.append(Paragraph(text, self.styles['CustomBody']))

    def add_spacer(self, height: float = 0.25):
        """Add vertical space (in inches)."""
        self.elements.append(Spacer(1, height * inch))

    def add_image(
        self,
        image_path: str,
        width: Optional[float] = None,
        height: Optional[float] = None
    ):
        """
        Add an image to the document.

        Args:
            image_path: Path to image file
            width: Width in points (optional)
            height: Height in points (optional)
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        img = Image(image_path)
        if width:
            img.drawWidth = width
        if height:
            img.drawHeight = height

        self.elements.append(img)
        self.elements.append(Spacer(1, 0.25 * inch))

    def add_page_break(self):
        """Add a page break."""
        self.elements.append(PageBreak())

    def save(self, output_path: Optional[str] = None):
        """
        Build and save the PDF.

        Args:
            output_path: Override output path (optional)
        """
        path = output_path or self.output_path

        # Ensure output directory exists
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)

        doc = SimpleDocTemplate(
            path,
            pagesize=self.page_size,
            topMargin=self.margins[0],
            rightMargin=self.margins[1],
            bottomMargin=self.margins[2],
            leftMargin=self.margins[3]
        )

        doc.build(self.elements)
        print(f"PDF saved: {path}")
        return path


if __name__ == "__main__":
    # Demo
    pdf = PDFGenerator("output/demo.pdf")
    pdf.add_title("Demo Document")
    pdf.add_chapter("Chapter 1: Introduction")
    pdf.add_paragraph(
        "This is a demonstration of the PDF generator. "
        "It supports titles, chapters, paragraphs, images, and more."
    )
    pdf.add_paragraph(
        "You can customize fonts, sizes, margins, and alignment "
        "to create professional-looking documents."
    )
    pdf.add_page_break()
    pdf.add_chapter("Chapter 2: Features")
    pdf.add_paragraph("The generator supports multiple features for document creation.")
    pdf.save()
