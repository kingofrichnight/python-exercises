"""Typed first-match search

Concepts: TypeVar, Iterable, Callable, union types
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Write a generic first_match function returning the first item satisfying
a predicate, or None if no match exists. Consume only enough input to find
a match. Note that a matched None is indistinguishable from no match.

HINT
Use one TypeVar to connect input items and the return type.

STRETCH
Return an explicit Found/Missing result to remove None ambiguity.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from collections.abc import Callable, Iterable
from typing import TypeVar

T = TypeVar('T')

def first_match(items: Iterable[T], predicate: Callable[[T], bool]) -> T | None:
    for item in items:
        if predicate(item):
            return item
    return None


def check():
    assert first_match([1, 3, 4, 6], lambda n: n % 2 == 0) == 4
    assert first_match([], bool) is None
    iterator = iter([1, 2, 3])
    assert first_match(iterator, lambda n: n == 2) == 2
    assert next(iterator) == 3


if __name__ == "__main__":
    check()
    print("PASS: Typed first-match search")
