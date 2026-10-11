"""Bounded event history

Concepts: deque, maxlen, collections
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Keep only the last capacity events from an iterable and return them oldest
to newest. Capacity must be a positive integer; reject nonpositive capacity.

HINT
deque(maxlen=...) evicts the oldest item automatically.

STRETCH
Implement an undo/redo history using two stacks.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from collections import deque

def recent(events, capacity):
    if capacity <= 0:
        raise ValueError('capacity must be positive')
    return list(deque(events, maxlen=capacity))


def check():
    assert recent(range(6), 3) == [3, 4, 5]
    assert recent([], 1) == []
    assert recent(['a'], 4) == ['a']


if __name__ == "__main__":
    check()
    print("PASS: Bounded event history")
