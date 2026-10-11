"""Merge named settings

Concepts: *args, **kwargs, unpacking, dict.update
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Accept any number of setting dictionaries and keyword overrides. Return a
new merged dictionary. Later dictionaries win; keyword overrides win last.

HINT
Build a new dictionary instead of updating the first input.

STRETCH
Add an optional allowlist of setting names.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def merge_settings(*layers, **overrides):
    result = {}
    for layer in layers:
        result.update(layer)
    result.update(overrides)
    return result


def check():
    base = {'theme': 'light', 'size': 12}
    assert merge_settings(base, {'size': 14}, theme='dark') == {'theme': 'dark', 'size': 14}
    assert base == {'theme': 'light', 'size': 12}
    assert merge_settings() == {}


if __name__ == "__main__":
    check()
    print("PASS: Merge named settings")
