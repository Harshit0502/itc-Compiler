
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


def binarize(image: "np.ndarray") -> "np.ndarray":
    """Return a thresholded version of ``image`` using Otsu."""
    if cv2 is None:
        return image
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh


def remove_noise(image: "np.ndarray") -> "np.ndarray":
    """Denoise small elements using median blur."""
    if cv2 is None:
        return image
    return cv2.medianBlur(image, 3)


def clean_image(image: "np.ndarray | str") -> Optional["np.ndarray"]:
    """Clean ``image`` which may be a path or array."""
    if cv2 is None or np is None:
        return None
    if isinstance(image, str):
        img = cv2.imread(image)
        if img is None:
            return None
    else:
        img = image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    gray = remove_noise(gray)
    thresh = binarize(gray)
    return thresh


# Backwards compatibility with previous API
preprocess_image = clean_image
