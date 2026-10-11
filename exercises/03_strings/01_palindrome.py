"""Normalized palindrome

Concepts: casefold, isalnum, slicing, comprehension
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return whether text reads the same both ways after case folding and removing
non-alphanumeric characters. Empty normalized text counts as a palindrome.

HINT
Build one normalized string.

STRETCH
Implement a two-pointer check without making a reversed copy.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def is_palindrome(text):
    normalized = ''.join(char for char in text.casefold() if char.isalnum())
    return normalized == normalized[::-1]


def check():
    assert is_palindrome('A man, a plan, a canal: Panama!')
    assert is_palindrome('')
    assert not is_palindrome('Python')


if __name__ == "__main__":
    check()
    print("PASS: Normalized palindrome")
