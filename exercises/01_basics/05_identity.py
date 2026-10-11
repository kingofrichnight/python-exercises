"""Copies, equality, and identity

Concepts: is, ==, mutable objects, shallow and deep copy
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given a nested list, return a shallow copy and a deep copy. Demonstrate that
outer lists are distinct, a shallow copy shares inner lists, and a deep copy
does not. Do not mutate the original inside the function.

HINT
Assignment binds a name; it does not copy an object.

STRETCH
Predict the effect of appending to the shallow copy versus its first row.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from copy import deepcopy

def copies(rows):
    return rows.copy(), deepcopy(rows)


def check():
    original = [[1], [2]]
    shallow, deep = copies(original)
    assert shallow == deep == original
    assert shallow is not original
    assert shallow[0] is original[0]
    assert deep[0] is not original[0]
    deep[0].append(9)
    assert original == [[1], [2]]


if __name__ == "__main__":
    check()
    print("PASS: Copies, equality, and identity")
