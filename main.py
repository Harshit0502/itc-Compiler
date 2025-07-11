"""Entry point for the Image-to-Code Compiler.

This script takes an image containing a mathematical expression, runs it
through OCR, parses the resulting text into an AST and evaluates it.

The pipeline consists of the following steps:
1. **OCR** using :func:`ocr.extract_text.get_expression_from_image` which
   relies on Tesseract.
2. **Image cleaning** performed by :func:`utils.image_cleaner.clean_image` to
   improve OCR accuracy.
3. **Lexing** with :mod:`compiler.lexer` to tokenize the expression.
4. **Parsing** via :mod:`compiler.parser` to build an abstract syntax tree.
5. **Evaluation** with :func:`compiler.evaluator.eval_ast` to compute the
   final result.
"""
"""Tesseract OCR helper for extracting math expressions from images."""


from __future__ import annotations

import argparse
from typing import Optional

from ocr.extract_text import get_expression_from_image

from utils.image_cleaner import clean_image
from compiler import lexer  # noqa:F401 - ensure lexer is registered
from compiler.parser import parser
from compiler.evaluator import eval_ast


def process_image(image_path: str) -> Optional[float]:
    """Process ``image_path`` and return the evaluated result."""
    cleaned = clean_image(image_path)
    print(f"Cleaned image saved to: {cleaned}")
    text = get_expression_from_image(cleaned)
    print(f"Extracted text: {text!r}")
    if not text:
        print("OCR failed or returned no text")
        return None
    try:
        ast = parser.parse(text)
        print(f"Parsed AST: {ast}")
        result = eval_ast(ast)
        print(f"Evaluated result: {result}")
        return result

    except Exception as exc:  # pragma: no cover - runtime failure
        print(f"Failed to evaluate expression: {exc}")
        return None


def main(argv: Optional[list[str]] = None) -> int:
    parser_ = argparse.ArgumentParser(description=__doc__)
    parser_.add_argument("image", nargs="?", help="path to the image file")
    args = parser_.parse_args(argv)

    if not args.image:
        parser_.print_usage()
        return 1

    print(f"Cleaning image: {args.image}")      
      

if __name__ == "__main__":  # pragma: no cover - CLI entry
    raise SystemExit(main())
