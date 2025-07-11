"""Lexical analyzer for arithmetic expressions using :mod:`ply`."""

import ply.lex as lex

# Token names
tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
)

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"

def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.value = float(t.value) if "." in t.value else int(t.value)
    return t

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    """Handle illegal characters by printing an error and skipping."""
    print(f"Illegal character {t.value[0]!r} at position {t.lexpos}")
    t.lexer.skip(1)



lexer = lex.lex()
