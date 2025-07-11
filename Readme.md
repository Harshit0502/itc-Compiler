# Image-to-Code Compiler

This project provides a very small prototype that reads a mathematical
expression from an image using OCR and evaluates the result. The
implementation relies on [pytesseract](https://github.com/madmaze/pytesseract),
OpenCV and the [PLY](https://www.dabeaz.com/ply/) parsing library.

## Usage

```bash
python main.py path/to/expression.png
```

The script will attempt to clean the image, extract the textual
expression, parse it into an AST and print the evaluation result.

diff --git a//dev/null b/README.md
index 0000000000000000000000000000000000000000..6179269009db694d431f942acaa3bb14bd60fa96 100644
--- a//dev/null
+++ b/README.md
@@ -0,0 +1,54 @@
+# Image-to-Code Compiler
+
+**A tiny pipeline turning math expressions in images into evaluated results.**
+
+## 🔍 What it does
+1. **Image ➡ OCR** – Tesseract extracts text from a preprocessed image.
+2. **Parser ➡ AST** – PLY builds an Abstract Syntax Tree of the expression.
+3. **Eval** – The AST is recursively evaluated and the final number is printed.
+
+## 🛠️ Tech stack
+- Python 3
+- OpenCV for image cleaning
+- Pytesseract for OCR
+- PLY (Lex & Yacc) for the lexer/parser
+- Graphviz for optional AST visualisation
+
+## 📦 Installation
+```bash
+pip install -r requirements.txt
+```
+
+## 🧪 How to run
+Run the command line script with an image path:
+```bash
+python main.py path/to/image.png
+```
+Or open `main.ipynb` in Google Colab for an interactive demo that installs the
+dependencies and walks through each step.
+
+## 📷 Sample
+Example input image:
+![Example](docs/images/example.png)
+
+The pipeline reads `2+2` from the image, builds an AST and prints:
+```
+Evaluated result: 4
+```
+
+## 📚 Directory structure
+```
+.
+├── ast/           # AST visualisation helpers
+├── compiler/      # lexer, parser and evaluator modules
+├── ocr/           # OCR utilities
+├── utils/         # image preprocessing utilities
+├── main.py        # command line entry point
+├── main.ipynb     # Colab notebook
+└── docs/images/   # sample image used in this README
+```
+
+## 💡 Credits & future ideas
+- Inspired by classic compiler design exercises and basic OCR tooling.
+- Future improvements could include handwriting recognition, a richer grammar
+  or optimised evaluation.
