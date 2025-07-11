"""Entry point for the Image-to-Code Compiler.

This script takes an image containing a mathematical expression, runs it
through OCR, parses the resulting text into an AST and evaluates it.

The pipeline consists of the following steps:

1. **OCR** using :func:`ocr.extract_text.extract_text` which relies on
   Tesseract.
2. **Image cleaning** performed by :func:`utils.image_cleaner.clean_image` to
   improve OCR accuracy.
3. **Lexing** with :mod:`compiler.lexer` to tokenize the expression.
4. **Parsing** via :mod:`compiler.parser` to build an abstract syntax tree.
5. **Evaluation** with :func:`compiler.evaluator.eval_ast` to compute the
   final result.
"""
from __future__ import annotations

import argparse
from typing import Optional

from ocr.extract_text import extract_text
from utils.image_cleaner import clean_image
from compiler import lexer  # noqa:F401 - ensure lexer is registered
from compiler.parser import parser
from compiler.evaluator import eval_ast


def process_image(image_path: str) -> Optional[float]:
    """Process ``image_path`` and return the evaluated result."""
    cleaned = clean_image(image_path)
    text = extract_text(cleaned)
    if not text:
        print("OCR failed or returned no text")
        return None
    try:
        ast = parser.parse(text)
        return eval_ast(ast)
    except Exception as exc:  # pragma: no cover - runtime failure
        print(f"Failed to evaluate expression: {exc}")
        return None


def main(argv: Optional[list[str]] = None) -> int:
    parser_ = argparse.ArgumentParser(description=__doc__)
    parser_.add_argument("image", help="path to the image file")
    args = parser_.parse_args(argv)

    result = process_image(args.image)
    if result is None:
        return 1
    print(result)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry
    raise SystemExit(main())
