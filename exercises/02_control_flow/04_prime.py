"""Prime number checker

Concepts: for/else, break, square-root bound
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return whether an integer n is prime. Values below 2 are not prime.
Only try divisors through the integer square root.

HINT
The loop else clause runs only if no break occurs.

STRETCH
Skip even divisors after handling 2.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            break
    else:
        return True
    return False


def check():
    assert is_prime(2) and is_prime(97)
    assert not is_prime(1) and not is_prime(-3)
    assert not is_prime(49)


if __name__ == "__main__":
    check()
    print("PASS: Prime number checker")
