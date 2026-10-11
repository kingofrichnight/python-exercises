"""Leap year classifier

Concepts: if, booleans, modulo, and/or
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
For a positive integer Gregorian year, return whether it is a leap year.
Years divisible by 100 are not leap years unless also divisible by 400.

HINT
Handle the 400-year exception.

STRETCH
Return the number of days in a given month and year.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def is_leap_year(year):
    if year <= 0:
        raise ValueError('year must be positive')
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def check():
    assert is_leap_year(2000)
    assert is_leap_year(2024)
    assert not is_leap_year(1900)
    assert not is_leap_year(2023)


if __name__ == "__main__":
    check()
    print("PASS: Leap year classifier")
