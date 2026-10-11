"""Cleanup even after failure

Concepts: try/except/else/finally, resources
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Call an injected operation. Return its value on success, or None on ValueError.
Append "success" or "invalid" to an event list, and always append "cleanup".
Other exceptions must propagate after cleanup.

HINT
Do not return from finally; it can hide failures.

STRETCH
Rewrite a resource-management example with a context manager.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def run_operation(operation, events):
    try:
        result = operation()
    except ValueError:
        events.append('invalid')
        return None
    else:
        events.append('success')
        return result
    finally:
        events.append('cleanup')


def check():
    events = []
    assert run_operation(lambda: 7, events) == 7
    assert events == ['success', 'cleanup']
    events = []
    assert run_operation(lambda: int('bad'), events) is None
    assert events == ['invalid', 'cleanup']
    events = []
    try:
        run_operation(lambda: 1 / 0, events)
    except ZeroDivisionError:
        assert events == ['cleanup']
    else:
        raise AssertionError('unexpected exception swallowed')


if __name__ == "__main__":
    check()
    print("PASS: Cleanup even after failure")
