"""Temporarily override a dictionary value

Concepts: contextmanager, sentinel, try/finally
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Implement a context manager that temporarily sets one mapping key and
restores the original value even on exceptions. If the key did not exist,
remove it afterward. Correctly preserve an original value of None.

HINT
A unique sentinel distinguishes absent keys from None.

STRETCH
Implement the same behavior with __enter__ and __exit__.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from contextlib import contextmanager

@contextmanager
def temporary_value(mapping, key, value):
    missing = object()
    previous = mapping.get(key, missing)
    mapping[key] = value
    try:
        yield mapping
    finally:
        if previous is missing:
            mapping.pop(key, None)
        else:
            mapping[key] = previous


def check():
    settings = {'mode': None}
    with temporary_value(settings, 'mode', 'test'):
        assert settings['mode'] == 'test'
    assert settings == {'mode': None}
    try:
        with temporary_value(settings, 'new', 1):
            raise RuntimeError('failure')
    except RuntimeError:
        pass
    assert settings == {'mode': None}


if __name__ == "__main__":
    check()
    print("PASS: Temporarily override a dictionary value")
