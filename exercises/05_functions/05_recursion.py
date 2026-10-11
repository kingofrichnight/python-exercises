"""Flatten nested lists

Concepts: recursion, isinstance, base case
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Flatten a finite, acyclic nested list into leaf values. Only lists are
expanded; tuples and strings remain single leaves. Empty lists add no values.

HINT
Each recursive call handles one inner list.

STRETCH
Use an explicit stack to handle nesting beyond the recursion limit.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def check():
    assert flatten([1, [2, [], [3]], 'ab', (4, 5)]) == [1, 2, 3, 'ab', (4, 5)]
    assert flatten([]) == []


if __name__ == "__main__":
    check()
    print("PASS: Flatten nested lists")
