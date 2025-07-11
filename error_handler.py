class LexerError(Exception):
    """Error raised by the lexer when encountering invalid input."""
    pass


class ParserError(Exception):
    """Error raised by the parser for syntax issues."""
    pass


class EvaluationError(Exception):
    """Error raised during evaluation phase."""
    pass


def format_error(line: int, message: str) -> str:
    """Return a formatted error string with line information."""
    return f"Error at line {line}: {message}"
