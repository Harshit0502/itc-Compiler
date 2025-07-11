# Image-to-Code Compiler

**A tiny pipeline turning math expressions in images into evaluated results.**

## 🔍 What it does
1. **Image ➡ OCR** – Tesseract extracts text from a preprocessed image.
2. **Parser ➡ AST** – PLY builds an Abstract Syntax Tree of the expression.
3. **Eval** – The AST is recursively evaluated and the final number is printed.

## 🛠️ Tech stack
- Python 3
- OpenCV for image cleaning
- Pytesseract for OCR
- PLY (Lex & Yacc) for the lexer/parser
- Graphviz for optional AST visualisation

## 📦 Installation
```bash
pip install -r requirements.txt
```

## 🧪 How to run
Run the command line script with an image path:
```bash
python main.py path/to/image.png
```
Or open `main.ipynb` in Google Colab for an interactive demo that installs the
dependencies and walks through each step.

## 📷 Sample
Example input image:
![Example](docs/images/example.png)

The pipeline reads `22` from the image, builds an AST and prints:
```
Evaluated result: 4
```

## 📚 Directory structure
```
.
├── ast/           # AST visualisation helpers
├── compiler/      # lexer, parser and evaluator modules
├── ocr/           # OCR utilities
├── utils/         # image preprocessing utilities
├── main.py        # command line entry point
├── main.ipynb     # Colab notebook
└── docs/images/   # sample image used in this README
```

## 💡 Credits & future ideas
- Inspired by classic compiler design exercises and basic OCR tooling.
- Future improvements could include handwriting recognition, a richer grammar
  or optimised evaluation.

