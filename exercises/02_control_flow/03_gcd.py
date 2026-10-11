"""Euclidean greatest common divisor

Concepts: while, simultaneous assignment, abs
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return the nonnegative greatest common divisor of two integers, including
negative arguments. Define gcd(0, 0) as 0. Do not use math.gcd.

HINT
Replace (a, b) with (b, a % b).

STRETCH
Compute least common multiples with a zero-safe formula.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def check():
    assert gcd(48, 18) == 6
    assert gcd(-8, 12) == 4
    assert gcd(0, 0) == 0
    assert gcd(0, 9) == 9


if __name__ == "__main__":
    check()
    print("PASS: Euclidean greatest common divisor")
