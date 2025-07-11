"""OCR utilities using Tesseract.

This module provides a simple wrapper around ``pytesseract`` to extract
text from an image file. It expects an image path and returns the text
recognized by Tesseract OCR.
"""
from typing import Optional

try:
    import pytesseract
    from PIL import Image
except ImportError:  # pragma: no cover - environment might not have deps
    pytesseract = None  # type: ignore
    Image = None  # type: ignore


def extract_text(image_path: str) -> Optional[str]:
    """Return text extracted from ``image_path`` using Tesseract.

    Parameters
    ----------
    image_path:
        Path to the image containing the text to OCR.

    Returns
    -------
    Optional[str]
        Text extracted from the image or ``None`` if OCR fails or
        dependencies are missing.
    """
    if pytesseract is None or Image is None:
        return None
    try:
        with Image.open(image_path) as img:
            return pytesseract.image_to_string(img)
    except Exception:
        return None
