from __future__ import annotations

import tempfile
from pathlib import Path

import streamlit as st
from PIL import Image

from utils.image_cleaner import preprocess_image
from ocr.extract_text import get_expression_from_image
from compiler import lexer  # noqa: F401 - register lexer tokens
from compiler.parser import parser
from compiler.evaluator import evaluate
from ast.visualize_ast import get_ast_plot
from symbol_table import SymbolTable


def run_pipeline(img_path: str) -> tuple[str | None, object | None, float | None]:
    """Run OCR ➡ parse ➡ evaluate pipeline on ``img_path``."""
    cleaned = preprocess_image(img_path)
    if cleaned is None:
        return None, None, None

    expr = get_expression_from_image(cleaned)
    if not expr:
        return None, None, None

    symbols = SymbolTable()
    try:
        ast = parser.parse(expr)
        result = evaluate(ast, symbols)
        return expr, ast, result
    except Exception:
        return expr, None, None


def main() -> None:
    st.title("Image-to-Code Compiler")
    st.write("Upload an image containing a math expression. The app will OCR, parse, and evaluate it.")

    uploaded = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if uploaded is not None:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded.name).suffix) as tmp:
            img.save(tmp.name)
            tmp_path = tmp.name

        cleaned = preprocess_image(tmp_path)
        expr = get_expression_from_image(cleaned) if cleaned is not None else None

        if expr is None:
            st.error("Could not extract expression from image.")
            return

        st.text_area("Extracted code", expr, height=100)
        if st.button("Compile"):
            symbols = SymbolTable()
            try:
                ast = parser.parse(expr)
                plot = get_ast_plot(ast)
                st.image(plot, caption="AST")
                result = evaluate(ast, symbols)
                st.success(f"Result: {result}")
            except Exception as exc:
                st.error(str(exc))
        Path(tmp_path).unlink(missing_ok=True)


if __name__ == "__main__":
    main()

