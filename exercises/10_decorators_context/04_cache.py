"""Memoized Fibonacci

Concepts: lru_cache, recursion, cache_info
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Compute the nth Fibonacci number with F(0)=0 and F(1)=1 for nonnegative
integers. Reject negative n. Memoize recursive calls; keep examples small
because recursion depth is still limited.

HINT
Caching removes repeated work, not recursive stack frames.

STRETCH
Compare with an iterative constant-space implementation.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 0:
        raise ValueError('n must be nonnegative')
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def check():
    fibonacci.cache_clear()
    assert fibonacci(10) == 55
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    before = fibonacci.cache_info().hits
    assert fibonacci(10) == 55
    assert fibonacci.cache_info().hits == before + 1


if __name__ == "__main__":
    check()
    print("PASS: Memoized Fibonacci")
