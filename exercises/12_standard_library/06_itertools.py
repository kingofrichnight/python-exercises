"""Find exact-size combinations

Concepts: combinations, itertools, generator expressions
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return all index tuples of length k whose corresponding integer values sum
to target. Each input position can be used once; duplicate values at different
positions remain distinct. k must be nonnegative.

HINT
Combine indices rather than values to preserve positional identity.

STRETCH
Compare combinatorial enumeration with dynamic programming.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from itertools import combinations

def matching_combinations(values, k, target):
    if k < 0:
        raise ValueError('k must be nonnegative')
    return [indices for indices in combinations(range(len(values)), k)
            if sum(values[index] for index in indices) == target]


def check():
    assert matching_combinations([2, 2, 3], 2, 5) == [(0, 2), (1, 2)]
    assert matching_combinations([], 0, 0) == [()]
    assert matching_combinations([1], 2, 2) == []


if __name__ == "__main__":
    check()
    print("PASS: Find exact-size combinations")
