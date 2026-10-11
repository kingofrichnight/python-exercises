"""Two-dimensional vectors

Concepts: operator overloading, NotImplemented, __iter__
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Implement an immutable Vector(x, y) supporting addition with another Vector,
iteration over coordinates, and abs(vector) for length. Return NotImplemented
for addition with unsupported types so Python can dispatch correctly.

HINT
Special methods let objects participate in Python syntax.

STRETCH
Add scalar multiplication including __rmul__.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from dataclasses import dataclass
from math import hypot

@dataclass(frozen=True)
class Vector:
    x: float
    y: float

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __abs__(self):
        return hypot(self.x, self.y)


def check():
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)
    assert tuple(Vector(1, 2)) == (1, 2)
    assert abs(Vector(3, 4)) == 5
    assert Vector(1, 2).__add__(3) is NotImplemented


if __name__ == "__main__":
    check()
    print("PASS: Two-dimensional vectors")
