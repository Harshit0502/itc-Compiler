"""Parser and AST builder for arithmetic expressions using PLY.

This module defines a grammar for simple arithmetic and constructs an
Abstract Syntax Tree (AST) from a source string.  The exposed ``parser``
object can be used directly via ``parser.parse(text, lexer=lexer)`` or
through the convenience :func:`parse` wrapper defined below.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

import ply.yacc as yacc

from .lexer import lexer, tokens
from error_handler import ParserError


@dataclass
class Number:
    value: Union[int, float]


@dataclass
class BinOp:
    op: str
    left: "AST"
    right: "AST"


@dataclass
class Var:
    name: str


@dataclass
class Assignment:
    name: str
    value: "AST"


AST = Union[Number, BinOp, Var, Assignment]


def p_expression_binop(p):
    """expression : expression PLUS term
                  | expression MINUS term"""
    p[0] = BinOp(p[2], p[1], p[3])


def p_expression_term(p):
    """expression : term"""
    p[0] = p[1]


def p_term_binop(p):
    """term : term TIMES factor
            | term DIVIDE factor"""
    p[0] = BinOp(p[2], p[1], p[3])


def p_term_factor(p):
    """term : factor"""
    p[0] = p[1]


def p_factor_number(p):
    """factor : NUMBER"""
    p[0] = Number(p[1])


def p_factor_id(p):
    """factor : ID"""
    p[0] = Var(p[1])


def p_factor_group(p):
    """factor : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_error(p):
    """Hook called by PLY when a syntax error is encountered."""
    if p is None:
        raise ParserError("Syntax error at EOF")
    raise ParserError(f"Syntax error at {p.value!r}")


def p_statement_assign(p):
    """statement : ID ASSIGN expression"""
    p[0] = Assignment(p[1], p[3])


def p_statement_expr(p):
    """statement : expression"""
    p[0] = p[1]


parser = yacc.yacc(start="statement")


def parse(text: str, *, lexer_obj=lexer) -> AST:
    """Parse ``text`` into an AST using ``lexer_obj`` (defaults to :data:`lexer`)."""
    return parser.parse(text, lexer=lexer_obj)

