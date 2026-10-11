"""Immutable inventory records

Concepts: dataclass, frozen, slots, __post_init__
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Define an immutable Product with name, integer price_cents, and integer
quantity (default 0). Validate nonempty name and nonnegative numbers.
Expose total_cents as a computed property.

HINT
Use __post_init__ for validation after generated initialization.

STRETCH
Add a classmethod to load a validated dictionary.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Product:
    name: str
    price_cents: int
    quantity: int = 0

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError('name is required')
        for value in (self.price_cents, self.quantity):
            if type(value) is not int or value < 0:
                raise ValueError('expected nonnegative integers')

    @property
    def total_cents(self):
        return self.price_cents * self.quantity


def check():
    from dataclasses import FrozenInstanceError, replace
    product = Product('Pen', 125, 3)
    assert product.total_cents == 375
    assert replace(product, quantity=4).total_cents == 500
    try:
        product.quantity = 9
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError('record was mutable')


if __name__ == "__main__":
    check()
    print("PASS: Immutable inventory records")
