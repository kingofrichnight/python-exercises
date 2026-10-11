"""Dispatch structured commands

Concepts: match/case, guards, destructuring
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Accept a command list: ["add", a, b] for two integers or ["echo", text]
for a string. Return the sum or text. Reject all other shapes with ValueError.
Booleans are intentionally excluded from integer operands.

HINT
Use a guard when a shape alone is insufficient.

STRETCH
Add multiply and uppercase commands.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def dispatch(command):
    match command:
        case ['add', a, b] if type(a) is int and type(b) is int:
            return a + b
        case ['echo', str(text)]:
            return text
        case _:
            raise ValueError('unknown command')


def check():
    assert dispatch(['add', 2, 3]) == 5
    assert dispatch(['echo', 'hi']) == 'hi'
    for command in ([], ['add', True, 2], ['echo', 4]):
        try:
            dispatch(command)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid command accepted')


if __name__ == "__main__":
    check()
    print("PASS: Dispatch structured commands")
