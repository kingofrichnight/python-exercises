"""Avoid shared mutable defaults

Concepts: None sentinel, mutation, default arguments
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Append an item to a provided list and return that list. When no list is
provided, create a fresh one on every call. An explicitly passed empty list
must be used rather than replaced.

HINT
Use is None instead of a truthiness check.

STRETCH
Design an immutable version that never mutates the caller’s list.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


def check():
    assert append_item('a') == ['a']
    assert append_item('b') == ['b']
    existing = []
    assert append_item(1, existing) is existing
    assert existing == [1]


if __name__ == "__main__":
    check()
    print("PASS: Avoid shared mutable defaults")
