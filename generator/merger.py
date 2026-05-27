"""
PDF Merger using pypdf
"""

from pypdf import PdfReader, PdfWriter
from typing import List, Optional
import os


class PDFMerger:
    """
    Merge multiple PDF files into one.

    Example:
        >>> merger = PDFMerger()
        >>> merger.add("cover.pdf")
        >>> merger.add("content.pdf")
        >>> merger.save("output/complete.pdf")
    """

    def __init__(self):
        """Initialize the merger."""
        self.writer = PdfWriter()
        self.files: List[str] = []

    def add(
        self,
        pdf_path: str,
        pages: Optional[List[int]] = None
    ):
        """
        Add a PDF file to the merger.

        Args:
            pdf_path: Path to PDF file
            pages: Specific pages to include (0-indexed), or None for all
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        reader = PdfReader(pdf_path)
        self.files.append(pdf_path)

        if pages is None:
            # Add all pages
            for page in reader.pages:
                self.writer.add_page(page)
        else:
            # Add specific pages
            for page_num in pages:
                if 0 <= page_num < len(reader.pages):
                    self.writer.add_page(reader.pages[page_num])

        print(f"Added: {pdf_path} ({len(reader.pages)} pages)")

    def add_blank_page(self):
        """Add a blank page (useful for double-sided printing)."""
        self.writer.add_blank_page()

    def get_page_count(self) -> int:
        """Return total page count."""
        return len(self.writer.pages)

    def save(self, output_path: str):
        """
        Save the merged PDF.

        Args:
            output_path: Output file path
        """
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)

        with open(output_path, 'wb') as f:
            self.writer.write(f)

        print(f"Merged PDF saved: {output_path}")
        print(f"Total pages: {self.get_page_count()}")
        print(f"Source files: {len(self.files)}")
        return output_path


if __name__ == "__main__":
    # Demo (requires actual PDF files)
    print("PDFMerger demo")
    print("Usage:")
    print("  merger = PDFMerger()")
    print("  merger.add('file1.pdf')")
    print("  merger.add('file2.pdf')")
    print("  merger.save('merged.pdf')")
