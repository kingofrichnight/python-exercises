"""Independent running counters

Concepts: closures, nonlocal, lexical scope
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Make a counter function starting from an integer. Each call optionally takes
an integer step (default 1), updates its private state, and returns the new value.
Different counters must not share state.

HINT
nonlocal assigns to the enclosing function’s binding.

STRETCH
Add reset behavior without using global variables.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def make_counter(start=0):
    value = start
    def increment(step=1):
        nonlocal value
        value += step
        return value
    return increment


def check():
    first, second = make_counter(), make_counter(10)
    assert first() == 1
    assert first(3) == 4
    assert second() == 11
    assert first(-1) == 3


if __name__ == "__main__":
    check()
    print("PASS: Independent running counters")
