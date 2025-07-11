"""Parser and AST builder for arithmetic expressions using PLY."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Union

import ply.yacc as yacc

from .lexer import tokens


@dataclass
class Number:
    value: Union[int, float]


@dataclass
class BinOp:
    op: str
    left: "AST"
    right: "AST"


AST = Union[Number, BinOp]


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


def p_factor_group(p):
    """factor : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_error(p):
    raise SyntaxError(f"Syntax error at {getattr(p, 'value', None)}")


parser = yacc.yacc(start="expression")
