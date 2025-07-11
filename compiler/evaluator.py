"""Recursive evaluator for arithmetic AST nodes."""


from typing import Union

from .parser import AST, BinOp, Number

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


def evaluate(node: Union[AST, tuple, NumberLike]) -> NumberLike:
    """Recursively evaluate ``node`` and return its numeric result."""
    if isinstance(node, Number):
        return node.value
    if isinstance(node, BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        return _apply_op(node.op, left, right)
    if isinstance(node, (int, float)):
        return node
    if isinstance(node, tuple) and len(node) == 3:
        op, left, right = node
        left_val = evaluate(left)
        right_val = evaluate(right)
        return _apply_op(op, left_val, right_val)
    raise TypeError(f"Invalid AST node: {node!r}")


# Backwards compatibility with older code
eval_ast = evaluate


