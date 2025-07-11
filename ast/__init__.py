"""Utilities for visualising AST structures without shadowing stdlib ``ast``."""
from __future__ import annotations

import importlib.util
import os
import sysconfig

# Load the standard library ``ast`` module explicitly so other modules relying
# on it continue to work even though this package is named ``ast``.
_stdlib_path = os.path.join(sysconfig.get_path("stdlib"), "ast.py")
_spec = importlib.util.spec_from_file_location("_stdlib_ast", _stdlib_path)
_stdlib_ast = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_stdlib_ast)  # type: ignore[attr-defined]

# Re-export all public names from the stdlib ``ast`` module
for _name in dir(_stdlib_ast):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_stdlib_ast, _name)

del _name  # clean up temporary variable

from .visualize_ast import visualize_ast

__all__ = [*[_n for _n in dir(_stdlib_ast) if not _n.startswith("_")], "visualize_ast"]
