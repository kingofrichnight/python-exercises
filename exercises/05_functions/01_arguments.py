"""Build a configurable receipt

Concepts: defaults, keyword-only parameters, round
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return the total for nonnegative numeric prices after a percentage discount
and tax. Discount must be between 0 and 1; tax must be nonnegative. Make both
options keyword-only. Round to two decimals; this float example is not money accounting.

HINT
The * separator makes later parameters keyword-only.

STRETCH
Replace float arithmetic with Decimal.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def total(prices, *, discount=0.0, tax=0.0):
    prices = list(prices)
    if not 0 <= discount <= 1 or tax < 0 or any(price < 0 for price in prices):
        raise ValueError('invalid price, discount, or tax')
    return round(sum(prices) * (1 - discount) * (1 + tax), 2)


def check():
    assert total([10, 20], discount=0.1, tax=0.1) == 29.7
    assert total([]) == 0
    assert total([10], discount=1) == 0


if __name__ == "__main__":
    check()
    print("PASS: Build a configurable receipt")
