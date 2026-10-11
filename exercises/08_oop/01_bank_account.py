"""Encapsulated account balance

Concepts: classes, __init__, properties, methods
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Implement a toy account holding a nonnegative integer number of cents.
Deposit and withdraw positive integer cents; reject booleans, nonintegers,
nonpositive amounts, and overdrafts. Expose a read-only balance property.

HINT
Validate before changing state.

STRETCH
Add an immutable transaction log; this toy is not banking software.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

class Account:
    def __init__(self, cents=0):
        if type(cents) is not int or cents < 0:
            raise ValueError('invalid starting balance')
        self._cents = cents

    @property
    def balance(self):
        return self._cents

    def deposit(self, cents):
        self._validate(cents)
        self._cents += cents

    def withdraw(self, cents):
        self._validate(cents)
        if cents > self._cents:
            raise ValueError('insufficient balance')
        self._cents -= cents

    @staticmethod
    def _validate(cents):
        if type(cents) is not int or cents <= 0:
            raise ValueError('amount must be positive integer cents')


def check():
    account = Account(100)
    account.deposit(50)
    account.withdraw(25)
    assert account.balance == 125
    for amount in (126, 0, -1, True, 1.5):
        try:
            account.withdraw(amount)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid withdrawal accepted')
    assert account.balance == 125


if __name__ == "__main__":
    check()
    print("PASS: Encapsulated account balance")
