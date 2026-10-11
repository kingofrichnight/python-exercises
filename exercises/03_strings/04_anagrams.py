"""Group anagrams

Concepts: sorted, defaultdict, canonical keys
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Group a list of words by their case-folded sorted characters. Preserve word
order within each group and group order by first appearance. Spaces count.

HINT
Anagrams share a sorted-character key.

STRETCH
Use character-frequency tuples as keys instead.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.casefold()))
        groups[key].append(word)
    return list(groups.values())


def check():
    assert group_anagrams(['Tea', 'eat', 'bat', 'ate']) == [['Tea', 'eat', 'ate'], ['bat']]
    assert group_anagrams([]) == []
    assert group_anagrams(['', '']) == [['', '']]


if __name__ == "__main__":
    check()
    print("PASS: Group anagrams")
