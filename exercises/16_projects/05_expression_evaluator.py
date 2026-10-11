"""Project: restricted arithmetic evaluator

Concepts: ast, recursion, allowlists, operators
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Evaluate expressions containing numeric int/float literals, +, -, *, /,
unary +/- and parentheses. Reject calls, names, booleans, and other syntax.
Limit source length to 200 characters. Propagate arithmetic errors. This
teaching parser is not a hardened sandbox for hostile workloads; never use eval().

HINT
Walk only explicitly allowed AST node types.

STRETCH
Add modulo and clear user-facing errors while preserving exception causes.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import ast
import operator

OPERATORS = {ast.Add: operator.add, ast.Sub: operator.sub,
             ast.Mult: operator.mul, ast.Div: operator.truediv}

def calculate(expression):
    if len(expression) > 200:
        raise ValueError('expression too long')
    tree = ast.parse(expression, mode='eval')
    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](visit(node.left), visit(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = visit(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        raise ValueError('unsupported expression')
    return visit(tree.body)


def check():
    assert calculate('2 + 3 * (4 - 1)') == 11
    assert calculate('-10 / +2') == -5
    for expression in ('True', 'name', 'sum([1,2])', '2 ** 3', '[1]'):
        try:
            calculate(expression)
        except ValueError:
            pass
        else:
            raise AssertionError('unsupported syntax accepted')


if __name__ == "__main__":
    check()
    print("PASS: Project: restricted arithmetic evaluator")
