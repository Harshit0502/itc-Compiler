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
    "ID",
    "ASSIGN",
)

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_ASSIGN = r"="

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    return t

def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.value = float(t.value) if "." in t.value else int(t.value)
    return t

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


from error_handler import LexerError


def t_error(t):
    """Handle illegal characters by raising :class:`LexerError`."""
    msg = f"Illegal character {t.value[0]!r} at position {t.lexpos}"
    raise LexerError(msg)


lexer = lex.lex()
