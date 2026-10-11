"""Measure implementations without brittle thresholds

Concepts: timeit, performance, equivalent behavior
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Compute the sum of squares from 0 through n-1 using a loop and a closed
formula. Reject negative n. Measure both with timeit, but only assert result
equality and nonnegative durations; never assert one timing must be faster.

HINT
Verify correctness before comparing performance.

STRETCH
Use cProfile on a larger application to find actual bottlenecks.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def loop_sum(n):
    if n < 0:
        raise ValueError('n must be nonnegative')
    return sum(value * value for value in range(n))

def formula_sum(n):
    if n < 0:
        raise ValueError('n must be nonnegative')
    return n * (n - 1) * (2 * n - 1) // 6


def check():
    from timeit import timeit
    for n in (0, 1, 2, 100):
        assert loop_sum(n) == formula_sum(n)
    timings = {name: timeit(lambda: function(100), number=20)
               for name, function in [('loop', loop_sum), ('formula', formula_sum)]}
    assert all(duration >= 0 for duration in timings.values())


if __name__ == "__main__":
    check()
    print("PASS: Measure implementations without brittle thresholds")
