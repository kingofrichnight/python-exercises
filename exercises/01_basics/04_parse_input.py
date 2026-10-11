"""Parse a shopping quantity

Concepts: input conversion, int, exceptions, print
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Convert an input string to a nonnegative integer quantity. Return None for
invalid or negative input. Support whitespace and a leading plus sign.
Provide a small interactive function but keep automated checks non-interactive.

HINT
int() can raise ValueError.

STRETCH
Keep asking until a valid quantity is entered.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def parse_quantity(text):
    try:
        quantity = int(text)
    except ValueError:
        return None
    return quantity if quantity >= 0 else None

def interactive():
    quantity = parse_quantity(input('Quantity: '))
    print('Invalid quantity' if quantity is None else f'Quantity: {quantity}')


def check():
    assert parse_quantity(' +12 ') == 12
    assert parse_quantity('0') == 0
    assert parse_quantity('-2') is None
    assert parse_quantity('2.5') is None
    assert parse_quantity('') is None


if __name__ == "__main__":
    check()
    print("PASS: Parse a shopping quantity")
