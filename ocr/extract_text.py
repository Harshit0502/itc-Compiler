"""Tesseract OCR helper for extracting math expressions from images."""
from __future__ import annotations

from typing import Optional, Union

try:
    import pytesseract
    from PIL import Image
    import numpy as np
except ImportError:  # pragma: no cover - environment might not have deps
    pytesseract = None  # type: ignore
    Image = None  # type: ignore
    np = None  # type: ignore


ImageInput = Union[str, "np.ndarray"]


def _load_image(src: ImageInput) -> Optional["Image.Image"]:
    """Return a PIL image loaded from ``src`` which may be a path or ndarray."""
    if Image is None:
        return None
    if isinstance(src, str):
        try:
            return Image.open(src)
        except Exception:
            return None
    if np is not None and isinstance(src, np.ndarray):
        try:
            return Image.fromarray(src)
        except Exception:
            return None
    return None


def get_expression_from_image(src: ImageInput) -> Optional[str]:
    """Return a cleaned math expression string extracted from ``src``."""
    if pytesseract is None:
        return None

    img = _load_image(src)
    if img is None:
        return None

    try:
        text = pytesseract.image_to_string(img)
    finally:
        img.close()

    # Remove whitespace and newlines
    cleaned = text.replace("\n", "").replace(" ", "").strip()

    # Common OCR corrections
    replacements = {"x": "*", "X": "*", "l": "1"}
    for old, new in replacements.items():
        cleaned = cleaned.replace(old, new)

    return cleaned or None

