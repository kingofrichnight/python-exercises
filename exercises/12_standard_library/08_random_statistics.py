"""Reproducible simulation

Concepts: random.Random, statistics, local RNG state
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Simulate n rolls of a six-sided die using a local seed. Return rolls and
their arithmetic mean. Require n > 0. Repeated calls with the same seed must
match within the same Python runtime. This RNG is not for security tokens.

HINT
Use Random(seed) instead of changing global random state.

STRETCH
Add sample variance and compare results as sample size grows.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import random
from statistics import mean

def simulate(n, seed):
    if n <= 0:
        raise ValueError('n must be positive')
    rng = random.Random(seed)
    rolls = [rng.randint(1, 6) for _ in range(n)]
    return rolls, mean(rolls)


def check():
    rolls, average = simulate(100, 42)
    assert (rolls, average) == simulate(100, 42)
    assert len(rolls) == 100 and all(1 <= value <= 6 for value in rolls)
    assert 1 <= average <= 6


if __name__ == "__main__":
    check()
    print("PASS: Reproducible simulation")
