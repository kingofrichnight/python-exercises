"""Process-pool CPU tasks

Concepts: ProcessPoolExecutor, pickle, main guard, spawn
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Use a process pool to count divisors of each positive integer. Define the
worker at module scope so it is picklable. Use spawn explicitly and protect
execution with the main guard. Preserve input order; reject nonpositive values.

HINT
Nested functions and lambdas are unsuitable workers with spawn.

STRETCH
Benchmark enough work to account for process startup and serialization costs.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from math import isqrt

def count_divisors(number):
    if number <= 0:
        raise ValueError('number must be positive')
    count = 0
    for divisor in range(1, isqrt(number) + 1):
        if number % divisor == 0:
            count += 1 if divisor * divisor == number else 2
    return count

def process_counts(numbers):
    with ProcessPoolExecutor(max_workers=2, mp_context=get_context('spawn')) as pool:
        return list(pool.map(count_divisors, numbers))


def check():
    assert process_counts([1, 6, 9, 13]) == [1, 4, 3, 2]


if __name__ == "__main__":
    check()
    print("PASS: Process-pool CPU tasks")
