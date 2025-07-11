
"""Image preprocessing utilities for OCR.

This module provides :func:`preprocess_image` which loads an image from disk
and performs a few typical cleaning steps to make OCR more reliable.  The
function returns the processed image as a NumPy array so it can be passed
directly to :mod:`pytesseract` or other OCR engines.
"""
from __future__ import annotations


from typing import Optional

try:
    import cv2
    import numpy as np
except ImportError:  # pragma: no cover - environment might not have deps
    cv2 = None  # type: ignore
    np = None  # type: ignore


ImageArray = "np.ndarray"


def preprocess_image(image_path: str) -> Optional[ImageArray]:
    """Return a cleaned image array loaded from ``image_path``.

    The function performs the following operations when ``opencv`` is
    available:
    1. Read the image from disk.
    2. Convert it to grayscale.
    3. Apply a slight Gaussian blur.
    4. Binarise the result using Otsu's thresholding.
    5. Resize up if the image is very small to improve OCR accuracy.

    If ``opencv`` is not installed or the image cannot be loaded, ``None`` is
    returned.
    """

    if cv2 is None or np is None:  # pragma: no cover - environment may lack deps
        return None

    img = cv2.imread(image_path)
    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    h, w = thresh.shape[:2]
    if max(h, w) < 600:
        scale = 600.0 / max(h, w)
        thresh = cv2.resize(thresh, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

    return thresh


# Backwards compatibility with previous API
clean_image = preprocess_image

