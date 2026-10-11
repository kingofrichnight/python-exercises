"""Permission flags with bit masks

Concepts: IntFlag, enums, bitwise operators
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Define READ, WRITE, and EXECUTE flags. Implement has_all(granted, required)
and remove(granted, revoked). Check combinations without converting to strings.
Requiring no flags should succeed for every permission set.

HINT
Use OR to combine bits and AND to test them.

STRETCH
Validate an external integer and reject unknown flag bits.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from enum import IntFlag

class Permission(IntFlag):
    READ = 1
    WRITE = 2
    EXECUTE = 4

def has_all(granted, required):
    return granted & required == required

def remove(granted, revoked):
    return granted & ~revoked


def check():
    granted = Permission.READ | Permission.WRITE
    assert has_all(granted, Permission.READ)
    assert not has_all(granted, Permission.READ | Permission.EXECUTE)
    assert has_all(granted, Permission(0))
    assert remove(granted, Permission.WRITE) == Permission.READ


if __name__ == "__main__":
    check()
    print("PASS: Permission flags with bit masks")
