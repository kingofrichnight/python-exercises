"""Personalized greeting

Concepts: variables, str, f-strings, return
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given a name string, trim surrounding whitespace and return "Hello, NAME!".
Use "friend" when the trimmed name is empty.

HINT
Strings have a strip() method.

STRETCH
Capitalize each word without changing internal apostrophes.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def greet(name):
    clean_name = name.strip()
    return f"Hello, {clean_name or 'friend'}!"


def check():
    assert greet(' Ada ') == 'Hello, Ada!'
    assert greet('   ') == 'Hello, friend!'


if __name__ == "__main__":
    check()
    print("PASS: Personalized greeting")
