"""Deduplicate while preserving order

Concepts: sets, lists, membership, hashability
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return the first occurrence of each hashable item from an iterable, preserving
order. [3, 1, 3, 2] -> [3, 1, 2]. Do not mutate the input.

HINT
Use a set for membership and a list for ordered output.

STRETCH
Support unhashable items using a caller-provided key.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def unique(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def check():
    values = [3, 1, 3, 2]
    assert unique(values) == [3, 1, 2]
    assert values == [3, 1, 3, 2]
    assert unique(iter('abac')) == ['a', 'b', 'c']


if __name__ == "__main__":
    check()
    print("PASS: Deduplicate while preserving order")
