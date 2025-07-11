class SymbolTable:
    """Simple symbol table supporting optional parent scope."""

    def __init__(self, parent: 'SymbolTable | None' = None) -> None:
        self._table: dict[str, object] = {}
        self.parent = parent

    def add_variable(self, name: str, value: object) -> None:
        if name in self._table:
            raise KeyError(f"Variable '{name}' already declared")
        self._table[name] = value

    def get_value(self, name: str) -> object:
        if name in self._table:
            return self._table[name]
        if self.parent is not None:
            return self.parent.get_value(name)
        raise KeyError(f"Variable '{name}' not found")

    def set_value(self, name: str, value: object) -> None:
        if name in self._table:
            self._table[name] = value
            return
        if self.parent is not None:
            self.parent.set_value(name, value)
            return
        raise KeyError(f"Variable '{name}' not found")
