"""Graphviz-based visualisation of arithmetic ASTs."""
from __future__ import annotations

from pathlib import Path
from typing import Iterator, Union

try:
    from graphviz import Digraph
except Exception:  # pragma: no cover - optional dependency may be missing
    Digraph = None  # type: ignore[misc]

ASTNode = Union[tuple, int, float]


def _add_nodes(dot: Digraph, node: ASTNode, parent_id: str | None, counter: Iterator[int]) -> None:
    node_id = f"n{next(counter)}"
    if isinstance(node, tuple) and len(node) == 3:
        op, left, right = node
        dot.node(node_id, str(op))
        if parent_id is not None:
            dot.edge(parent_id, node_id)
        _add_nodes(dot, left, node_id, counter)
        _add_nodes(dot, right, node_id, counter)
    else:
        dot.node(node_id, str(node))
        if parent_id is not None:
            dot.edge(parent_id, node_id)


def visualize_ast(ast: ASTNode, output_file: str = "ast.png", *,
                  graph_attr: dict[str, str] | None = None,
                  node_attr: dict[str, str] | None = None,
                  edge_attr: dict[str, str] | None = None) -> str:
    """Render ``ast`` to ``output_file`` and return the image path."""
    if Digraph is None:  # pragma: no cover - dependency not installed
        raise RuntimeError("graphviz is required for AST visualization")
    graph_attr = graph_attr or {}
    node_attr = node_attr or {}
    edge_attr = edge_attr or {}

    path = Path(output_file)
    dot = Digraph("AST", graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr)
    dot.format = path.suffix.lstrip(".") or "png"

    counter = iter(range(1000000))
    _add_nodes(dot, ast, None, counter)

    dot.render(outfile=str(path), cleanup=True)
    return str(path)
