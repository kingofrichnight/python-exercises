"""Temperature converter

Concepts: arithmetic, floats, operator precedence
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Convert a numeric Celsius temperature to Fahrenheit. Example: 0 -> 32.
Negative temperatures are valid; use approximate comparisons for floats.

HINT
Multiply before adding the offset.

STRETCH
Add the inverse converter and verify round trips.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def check():
    from math import isclose
    assert isclose(celsius_to_fahrenheit(0), 32)
    assert isclose(celsius_to_fahrenheit(-40), -40)
    assert isclose(celsius_to_fahrenheit(100), 212)


if __name__ == "__main__":
    check()
    print("PASS: Temperature converter")
