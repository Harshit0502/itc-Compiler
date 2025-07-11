from compiler.parser import parser, Assignment, BinOp


def test_parse_assignment():
    ast = parser.parse("a = 1 + 2")
    assert isinstance(ast, Assignment)
    assert ast.name == "a"
    assert isinstance(ast.value, BinOp)


def test_parse_expression():
    ast = parser.parse("1 + 2 * 3")
    assert isinstance(ast, BinOp)
    assert ast.op == "+"
