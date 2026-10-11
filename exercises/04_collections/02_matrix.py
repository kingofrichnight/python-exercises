"""Transpose a rectangular matrix

Concepts: nested lists, zip, unpacking, any
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return the transpose of a rectangular list of rows. Empty input -> [].
Reject rows of unequal length with ValueError. Zero-width rows transpose to [].

HINT
zip silently truncates, so validate before using it.

STRETCH
Implement matrix multiplication with dimension checks.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def transpose(rows):
    if not rows:
        return []
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError('ragged matrix')
    return [list(column) for column in zip(*rows)]


def check():
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose([]) == []
    assert transpose([[], []]) == []
    try:
        transpose([[1], [2, 3]])
    except ValueError:
        pass
    else:
        raise AssertionError('ragged input accepted')


if __name__ == "__main__":
    check()
    print("PASS: Transpose a rectangular matrix")
