"""Exact invoice arithmetic

Concepts: Decimal, quantize, ROUND_HALF_UP, finite values
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given nonnegative finite decimal price strings and a tax-rate string, compute
the sum plus tax and round once to cents using ROUND_HALF_UP. Reject negative
or nonfinite values. Keep examples within the default Decimal precision.

HINT
Construct Decimal from strings, not from binary floats.

STRETCH
Specify and implement line-item rounding as an alternate policy.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from decimal import Decimal, ROUND_HALF_UP

def invoice(prices, tax='0'):
    values = [Decimal(value) for value in prices]
    rate = Decimal(tax)
    if any(not value.is_finite() or value < 0 for value in [*values, rate]):
        raise ValueError('expected finite nonnegative amounts')
    subtotal = sum(values, Decimal('0'))
    return (subtotal * (1 + rate)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def check():
    assert invoice(['0.10', '0.20']) == Decimal('0.30')
    assert invoice(['1.005']) == Decimal('1.01')
    assert invoice(['10'], '0.075') == Decimal('10.75')
    assert invoice([]) == Decimal('0.00')


if __name__ == "__main__":
    check()
    print("PASS: Exact invoice arithmetic")
