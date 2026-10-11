"""Inventory reconciliation

Concepts: dict union, sets, comprehensions, sorting
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given old and new item-to-quantity dictionaries, return sorted added, removed,
and changed item names. A changed item exists in both but has a different value.

HINT
Compare key sets before comparing values.

STRETCH
Return quantity deltas as a separate mapping.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def reconcile(old, new):
    old_keys, new_keys = set(old), set(new)
    return {
        'added': sorted(new_keys - old_keys),
        'removed': sorted(old_keys - new_keys),
        'changed': sorted(key for key in old_keys & new_keys if old[key] != new[key]),
    }


def check():
    assert reconcile({'a': 2, 'b': 1}, {'a': 3, 'c': 4}) == {
        'added': ['c'], 'removed': ['b'], 'changed': ['a']}
    assert reconcile({}, {}) == {'added': [], 'removed': [], 'changed': []}


if __name__ == "__main__":
    check()
    print("PASS: Inventory reconciliation")
