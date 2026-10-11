"""Test a bounded clamp function

Concepts: unittest, subTest, assertRaises, boundaries
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Implement clamp(value, low, high), then test interior values, both
boundaries, outside values, and an invalid interval. Raise ValueError if
low > high. Keep the tests executable from this file’s check() function.

HINT
Choose test cases at transitions in behavior.

STRETCH
Add equal-bound tests and randomized invariant checks.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import unittest

def clamp(value, low, high):
    if low > high:
        raise ValueError('low exceeds high')
    return max(low, min(value, high))

class ClampTests(unittest.TestCase):
    def test_values(self):
        for value, expected in [(-1, 0), (0, 0), (5, 5), (10, 10), (11, 10)]:
            with self.subTest(value=value):
                self.assertEqual(clamp(value, 0, 10), expected)

    def test_invalid_interval(self):
        with self.assertRaises(ValueError):
            clamp(3, 5, 1)


def check():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ClampTests)
    result = unittest.TestResult()
    suite.run(result)
    assert result.wasSuccessful(), result.errors + result.failures
    assert result.testsRun == 2


if __name__ == "__main__":
    check()
    print("PASS: Test a bounded clamp function")
