"""Shape interface

Concepts: ABC, abstractmethod, inheritance, polymorphism
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Define an abstract Shape with area(), and concrete Rectangle and Circle
implementations. Require finite positive dimensions. Sum areas through the
shared interface without inspecting concrete types.

HINT
Call the common method rather than using isinstance branches.

STRETCH
Add a Triangle without changing total_area.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from abc import ABC, abstractmethod
from math import pi, isfinite

class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

def positive(value):
    if not isfinite(value) or value <= 0:
        raise ValueError('dimension must be finite and positive')
    return value

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = positive(width), positive(height)

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = positive(radius)

    def area(self):
        return pi * self.radius ** 2

def total_area(shapes):
    return sum(shape.area() for shape in shapes)


def check():
    from math import isclose
    assert isclose(total_area([Rectangle(2, 3), Circle(1)]), 6 + pi)
    assert total_area([]) == 0
    try:
        Shape()
    except TypeError:
        pass
    else:
        raise AssertionError('abstract class instantiated')


if __name__ == "__main__":
    check()
    print("PASS: Shape interface")
