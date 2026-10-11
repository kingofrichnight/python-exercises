"""Find the first matching index

Concepts: binary search, invariants, logarithmic search
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given an ascending sorted sequence and target, return the first matching
index or -1 if absent. Handle duplicates and empty inputs. Do not sort or
linearly scan. Time O(log n), extra space O(1).

HINT
Find the leftmost position where a value could be inserted.

STRETCH
Implement upper_bound and use both bounds to count duplicates.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def binary_search(values, target):
    low, high = 0, len(values)
    while low < high:
        middle = (low + high) // 2
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle
    if low < len(values) and values[low] == target:
        return low
    return -1


def check():
    assert binary_search([1, 2, 2, 2, 5], 2) == 1
    assert binary_search([], 1) == -1
    assert binary_search([1, 3], 2) == -1
    assert binary_search([1, 3], 3) == 1


if __name__ == "__main__":
    check()
    print("PASS: Find the first matching index")
