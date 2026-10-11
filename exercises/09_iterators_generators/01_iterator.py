"""Custom countdown iterator

Concepts: __iter__, __next__, StopIteration
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Implement a one-shot Countdown(n) iterator yielding n down to 1. n <= 0
yields nothing. Once exhausted, further next() calls must keep stopping.

HINT
An iterator returns itself from __iter__.

STRETCH
Build a reusable iterable that creates a fresh iterator every time.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

class Countdown:
    def __init__(self, n):
        self.remaining = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.remaining <= 0:
            raise StopIteration
        value = self.remaining
        self.remaining -= 1
        return value


def check():
    counter = Countdown(3)
    assert next(counter) == 3
    assert list(counter) == [2, 1]
    assert list(counter) == []
    assert list(Countdown(0)) == []


if __name__ == "__main__":
    check()
    print("PASS: Custom countdown iterator")
