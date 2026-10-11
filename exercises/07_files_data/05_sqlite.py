"""Parameterized SQLite queries

Concepts: sqlite3, SQL, transactions, contextlib.closing
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Store supplied (name, score) pairs in an in-memory database and return names
with score >= a threshold, sorted by name. Use parameterized SQL for values.
Duplicate names should raise IntegrityError; always close the connection.

HINT
A connection context manages transactions, not connection closure.

STRETCH
Add updates and demonstrate rollback on a failed transaction.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import sqlite3
from contextlib import closing

def passing_names(students, threshold):
    with closing(sqlite3.connect(':memory:')) as connection:
        with connection:
            connection.execute('CREATE TABLE students (name TEXT PRIMARY KEY, score INTEGER)')
            connection.executemany('INSERT INTO students VALUES (?, ?)', students)
        rows = connection.execute(
            'SELECT name FROM students WHERE score >= ? ORDER BY name', (threshold,))
        return [name for (name,) in rows]


def check():
    assert passing_names([('Ada', 90), ('Bo', 60), ("O'Neil", 80)], 80) == ['Ada', "O'Neil"]
    assert passing_names([], 0) == []
    try:
        passing_names([('Ada', 1), ('Ada', 2)], 0)
    except sqlite3.IntegrityError:
        pass
    else:
        raise AssertionError('duplicate key accepted')


if __name__ == "__main__":
    check()
    print("PASS: Parameterized SQLite queries")
