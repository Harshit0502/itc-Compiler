"""Recursive evaluator for arithmetic AST nodes."""

from typing import Union

from .parser import AST, BinOp, Number, Assignment, Var
from error_handler import EvaluationError
from symbol_table import SymbolTable

NumberLike = Union[int, float]


def _apply_op(op: str, left: NumberLike, right: NumberLike) -> NumberLike:
    """Return ``left <op> right`` for the four basic arithmetic operations."""
    if op in {"add", "+"}:
        return left + right
    if op in {"sub", "-"}:
        return left - right
    if op in {"mul", "*"}:
        return left * right
    if op in {"div", "/"}:
        return left / right
    raise ValueError(f"Unknown operator: {op}")


def evaluate(node: Union[AST, tuple, NumberLike], symbols: SymbolTable | None = None) -> NumberLike:
    """Recursively evaluate ``node`` and return its numeric result."""
    symbols = symbols or SymbolTable()
    if isinstance(node, Number):
        return node.value
    if isinstance(node, Var):
        try:
            return symbols.get_value(node.name)
        except KeyError:
            raise EvaluationError(f"Undefined variable '{node.name}'")
    if isinstance(node, Assignment):
        value = evaluate(node.value, symbols)
        if node.name in symbols._table:
            symbols.set_value(node.name, value)
        else:
            symbols.add_variable(node.name, value)
        return value
    if isinstance(node, BinOp):
        left = evaluate(node.left, symbols)
        right = evaluate(node.right, symbols)
        return _apply_op(node.op, left, right)
    if isinstance(node, (int, float)):
        return node
    if isinstance(node, tuple) and len(node) == 3:
        op, left, right = node
        left_val = evaluate(left, symbols)
        right_val = evaluate(right, symbols)
        return _apply_op(op, left_val, right_val)
    raise EvaluationError(f"Invalid AST node: {node!r}")


# Backwards compatibility with older code
eval_ast = evaluate

