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
