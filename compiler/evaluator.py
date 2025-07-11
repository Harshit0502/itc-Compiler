"""Evaluate an AST produced by :mod:`compiler.parser`."""
from typing import Union

from .parser import AST, BinOp, Number


def eval_ast(node: AST) -> Union[int, float]:
    """Recursively evaluate ``node`` and return the numeric result."""
    if isinstance(node, Number):
        return node.value
    if isinstance(node, BinOp):
        left = eval_ast(node.left)
        right = eval_ast(node.right)
        if node.op == "+":
            return left + right
        if node.op == "-":
            return left - right
        if node.op == "*":
            return left * right
        if node.op == "/":
            return left / right
    raise TypeError(f"Unsupported AST node {node}")
