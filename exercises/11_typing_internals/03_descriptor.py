"""Reusable positive-number descriptor

Concepts: descriptors, __set_name__, __get__, __set__
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Build a descriptor enforcing finite positive numeric values on assignment.
Use it for Rectangle.width and height. Keep values per instance and return
the descriptor itself for access through the class. Exclude booleans.

HINT
Do not store each instance’s value on the shared descriptor.

STRETCH
Generalize the descriptor to configurable minimum and maximum values.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from math import isfinite

class Positive:
    def __set_name__(self, owner, name):
        self.storage_name = '_' + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError('expected a number')
        if not isfinite(value) or value <= 0:
            raise ValueError('expected finite positive value')
        setattr(instance, self.storage_name, value)

class Rectangle:
    width = Positive()
    height = Positive()

    def __init__(self, width, height):
        self.width, self.height = width, height


def check():
    first, second = Rectangle(2, 3), Rectangle(4, 5)
    first.width = 7
    assert first.width == 7 and second.width == 4
    assert isinstance(Rectangle.width, Positive)
    for value in (0, -1, True, float('nan')):
        try:
            first.width = value
        except ValueError:
            pass
        else:
            raise AssertionError('invalid value accepted')


if __name__ == "__main__":
    check()
    print("PASS: Reusable positive-number descriptor")
