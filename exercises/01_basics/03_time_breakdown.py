"""Break seconds into clock units

Concepts: integers, divmod, tuple unpacking
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given a nonnegative integer number of seconds, return (hours, minutes, seconds).
Hours may exceed 23. Reject negative values with ValueError. 3661 -> (1, 1, 1).

HINT
Use divmod twice.

STRETCH
Format the result as HH:MM:SS.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def split_seconds(total):
    if total < 0:
        raise ValueError('seconds must be nonnegative')
    hours, remaining = divmod(total, 3600)
    minutes, seconds = divmod(remaining, 60)
    return hours, minutes, seconds


def check():
    assert split_seconds(3661) == (1, 1, 1)
    assert split_seconds(0) == (0, 0, 0)
    assert split_seconds(86400) == (24, 0, 0)
    try:
        split_seconds(-1)
    except ValueError:
        pass
    else:
        raise AssertionError('negative input accepted')


if __name__ == "__main__":
    check()
    print("PASS: Break seconds into clock units")
