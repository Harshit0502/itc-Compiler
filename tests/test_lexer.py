import pytest

from compiler.lexer import lexer
from error_handler import LexerError


def test_multi_digit_number():
    lexer.input("123 + 45")
    tokens = [tok.type for tok in lexer]
    assert tokens == ["NUMBER", "PLUS", "NUMBER"]


def test_identifier_token():
    lexer.input("var")
    tok = next(lexer)
    assert tok.type == "ID"


def test_illegal_char_raises():
    with pytest.raises(LexerError):
        lexer.input("$")
        next(lexer)
