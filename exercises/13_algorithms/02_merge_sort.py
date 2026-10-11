"""Stable merge sort

Concepts: divide and conquer, recursion, stability
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return a sorted copy of a list using merge sort and an optional key function.
Preserve original order for equal keys. Do not call sorted() or list.sort().
Target O(n log n) time; slicing and merged lists use additional memory.

HINT
On ties, choose the item from the left half.

STRETCH
Cache keys to avoid recomputing expensive transformations.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def merge_sort(values, key=lambda value: value):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort(values[:middle], key)
    right = merge_sort(values[middle:], key)
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


def check():
    assert merge_sort([3, 1, 2, 1]) == [1, 1, 2, 3]
    assert merge_sort([]) == []
    records = [('a', 2), ('b', 1), ('c', 2)]
    assert merge_sort(records, key=lambda row: row[1]) == [('b', 1), ('a', 2), ('c', 2)]
    assert records == [('a', 2), ('b', 1), ('c', 2)]


if __name__ == "__main__":
    check()
    print("PASS: Stable merge sort")
