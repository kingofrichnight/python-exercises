"""Project: monthly expense report

Concepts: CSV, Decimal, date parsing, aggregation
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given CSV text with date,category,amount columns, aggregate expenses for a
requested YYYY-MM month by category. Amounts are finite decimals; negative
refunds are allowed. Validate every row, including rows from other months.
Raise ValueError with the logical row number on invalid input. Return sorted keys.

HINT
Separate parsing and validation from selecting the requested month.

STRETCH
Export the report as CSV and add row-level error collection.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import csv
import re
from io import StringIO
from datetime import date
from decimal import Decimal, InvalidOperation

def monthly_expenses(text, month):
    if not re.fullmatch(r'\d{4}-\d{2}', month):
        raise ValueError('month must be YYYY-MM')
    date.fromisoformat(month + '-01')
    reader = csv.DictReader(StringIO(text))
    if reader.fieldnames != ['date', 'category', 'amount']:
        raise ValueError('expected date,category,amount header')
    totals = {}
    for number, row in enumerate(reader, 2):
        try:
            if None in row or any(value is None for value in row.values()):
                raise ValueError('wrong column count')
            day = date.fromisoformat(row['date'])
            category = row['category'].strip()
            amount = Decimal(row['amount'])
            if not category or not amount.is_finite():
                raise ValueError('invalid category or amount')
        except (ValueError, InvalidOperation) as error:
            raise ValueError(f'invalid row {number}') from error
        if day.strftime('%Y-%m') == month:
            totals[category] = totals.get(category, Decimal('0')) + amount
    return dict(sorted(totals.items()))


def check():
    text = ('date,category,amount\n2025-01-02,Food,10.50\n'
            '2025-01-03,Food,-1.00\n2025-02-01,Travel,99\n')
    assert monthly_expenses(text, '2025-01') == {'Food': Decimal('9.50')}
    assert monthly_expenses(text, '2024-12') == {}
    try:
        monthly_expenses('date,category,amount\n2025-01-01,Food,NaN\n', '2025-01')
    except ValueError as error:
        assert 'row 2' in str(error)
    else:
        raise AssertionError('nonfinite expense accepted')


if __name__ == "__main__":
    check()
    print("PASS: Project: monthly expense report")
