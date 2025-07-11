import pytest

from compiler.parser import parser
from compiler.evaluator import evaluate
from symbol_table import SymbolTable
from error_handler import EvaluationError


def test_evaluate_simple():
    ast = parser.parse("1 + 2")
    result = evaluate(ast)
    assert result == 3


def test_assignment_and_lookup():
    sym = SymbolTable()
    ast = parser.parse("a = 2 + 3")
    result = evaluate(ast, sym)
    assert result == 5
    assert sym.get_value("a") == 5


def test_undefined_variable_error():
    with pytest.raises(EvaluationError):
        ast = parser.parse("b + 1")
        evaluate(ast)
