"""Image preprocessing utilities.

This module contains helper functions to clean and prepare images
for OCR using ``opencv``. The provided :func:`clean_image` function
performs a minimal set of operations (grayscale conversion and
thresholding). If ``opencv`` is not available, the function simply
returns the path to the original image.
"""
from typing import Optional

try:
    import cv2
    import numpy as np
except ImportError:  # pragma: no cover - environment might not have deps
    cv2 = None  # type: ignore
    np = None  # type: ignore


def clean_image(image_path: str) -> Optional[str]:
    """Preprocess ``image_path`` for OCR and return path to cleaned image."""
    if cv2 is None:
        return image_path

    img = cv2.imread(image_path)
    if img is None:
        return image_path

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cleaned_path = image_path.rsplit(".", 1)[0] + "_clean.png"
    cv2.imwrite(cleaned_path, thresh)
    return cleaned_path
