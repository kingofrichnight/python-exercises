"""Aggregate CSV sales

Concepts: csv.DictReader, StringIO, Decimal
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Read CSV text with product and amount columns. Sum Decimal amounts by product.
Quoted product names containing commas must work. Negative amounts represent
refunds. Assume each row has valid finite decimal text and required columns.

HINT
Do not split CSV rows with str.split(",").

STRETCH
Reject missing columns, empty products, and nonfinite values with row numbers.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import csv
from io import StringIO
from decimal import Decimal

def totals(csv_text):
    result = {}
    for row in csv.DictReader(StringIO(csv_text)):
        product = row['product']
        result[product] = result.get(product, Decimal('0')) + Decimal(row['amount'])
    return result


def check():
    text = 'product,amount\n"Tea, green",1.10\nCoffee,2.00\n"Tea, green",-0.10\n'
    assert totals(text) == {'Tea, green': Decimal('1.00'), 'Coffee': Decimal('2.00')}
    assert totals('product,amount\n') == {}


if __name__ == "__main__":
    check()
    print("PASS: Aggregate CSV sales")
