"""Longest substring without repetition

Concepts: sliding window, dictionaries, linear time
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return the length of the longest substring containing no repeated Unicode
code points. Empty text -> 0. Target O(n) time; do not enumerate all substrings.

HINT
Never move the left boundary backward.

STRETCH
Return the earliest maximal substring as well as its length.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def longest_unique(text):
    last_seen = {}
    left = best = 0
    for right, char in enumerate(text):
        left = max(left, last_seen.get(char, -1) + 1)
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


def check():
    assert longest_unique('abcabcbb') == 3
    assert longest_unique('abba') == 2
    assert longest_unique('') == 0
    assert longest_unique('🙂a🙂') == 2


if __name__ == "__main__":
    check()
    print("PASS: Longest substring without repetition")
