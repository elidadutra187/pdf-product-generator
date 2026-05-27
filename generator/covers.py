"""
Cover Generator using Pillow
"""

from PIL import Image, ImageDraw, ImageFont
from typing import Optional, Tuple
import os


class CoverGenerator:
    """
    Generate product covers and thumbnails.

    Example:
        >>> cover = CoverGenerator(1600, 2400)
        >>> cover.add_title("The Ultimate Guide")
        >>> cover.add_subtitle("Everything you need to know")
        >>> cover.save("cover.png")
    """

    def __init__(
        self,
        width: int = 1600,
        height: int = 2400,
        background_color: str = "#1a1a2e",
        text_color: str = "#ffffff"
    ):
        """
        Initialize cover generator.

        Args:
            width: Cover width in pixels
            height: Cover height in pixels
            background_color: Background color (hex)
            text_color: Default text color (hex)
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.text_color = text_color

        # Create base image
        self.image = Image.new('RGB', (width, height), background_color)
        self.draw = ImageDraw.Draw(self.image)

        # Track current Y position for text
        self.current_y = height // 3

    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def _get_font(self, size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
        """Get a font, falling back to default if custom not available."""
        try:
            # Try to use a nice font if available
            font_name = "arial.ttf" if not bold else "arialbd.ttf"
            return ImageFont.truetype(font_name, size)
        except OSError:
            # Fall back to default
            return ImageFont.load_default()

    def add_title(
        self,
        text: str,
        font_size: int = 72,
        color: Optional[str] = None
    ):
        """
        Add main title to cover.

        Args:
            text: Title text
            font_size: Font size in pixels
            color: Text color (hex, optional)
        """
        font = self._get_font(font_size, bold=True)
        text_color = self._hex_to_rgb(color or self.text_color)

        # Calculate text position (centered)
        bbox = self.draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (self.width - text_width) // 2

        self.draw.text((x, self.current_y), text, font=font, fill=text_color)
        self.current_y += font_size + 30

    def add_subtitle(
        self,
        text: str,
        font_size: int = 36,
        color: Optional[str] = None
    ):
        """
        Add subtitle to cover.

        Args:
            text: Subtitle text
            font_size: Font size in pixels
            color: Text color (hex, optional)
        """
        font = self._get_font(font_size)
        text_color = self._hex_to_rgb(color or self.text_color)

        bbox = self.draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (self.width - text_width) // 2

        self.draw.text((x, self.current_y), text, font=font, fill=text_color)
        self.current_y += font_size + 20

    def add_author(
        self,
        name: str,
        font_size: int = 28,
        color: Optional[str] = None
    ):
        """
        Add author name (positioned at bottom).

        Args:
            name: Author name
            font_size: Font size in pixels
            color: Text color (hex, optional)
        """
        font = self._get_font(font_size)
        text_color = self._hex_to_rgb(color or self.text_color)

        bbox = self.draw.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        x = (self.width - text_width) // 2
        y = self.height - 150  # Position near bottom

        self.draw.text((x, y), name, font=font, fill=text_color)

    def add_decorative_line(
        self,
        color: Optional[str] = None,
        width: int = 200,
        thickness: int = 3
    ):
        """Add a centered decorative line."""
        line_color = self._hex_to_rgb(color or self.text_color)
        x1 = (self.width - width) // 2
        x2 = x1 + width
        y = self.current_y

        self.draw.line([(x1, y), (x2, y)], fill=line_color, width=thickness)
        self.current_y += 40

    def save(self, output_path: str, format: str = "PNG"):
        """
        Save the cover image.

        Args:
            output_path: Output file path
            format: Image format (PNG, JPEG, etc.)
        """
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        self.image.save(output_path, format)
        print(f"Cover saved: {output_path}")
        return output_path


if __name__ == "__main__":
    # Demo
    cover = CoverGenerator(
        width=1600,
        height=2400,
        background_color="#1a1a2e"
    )
    cover.add_title("The Ultimate Guide")
    cover.add_decorative_line()
    cover.add_subtitle("To Growth Marketing")
    cover.add_author("Elida Dutra")
    cover.save("output/demo_cover.png")
