"""Minimum coin count

Concepts: dynamic programming, unreachable states
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given positive integer coin denominations and a nonnegative amount, return
the fewest coins needed with unlimited supply, or None if impossible.
Reject invalid denominations or a negative amount. Empty coins can form only 0.

HINT
Build the answer for each smaller subtotal first.

STRETCH
Return one optimal set of coins, not only its length.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def min_coins(coins, amount):
    coins = tuple(coins)
    if amount < 0 or any(type(coin) is not int or coin <= 0 for coin in coins):
        raise ValueError('invalid coins or amount')
    best = [0] + [float('inf')] * amount
    for subtotal in range(1, amount + 1):
        for coin in coins:
            if coin <= subtotal:
                best[subtotal] = min(best[subtotal], best[subtotal - coin] + 1)
    return None if best[amount] == float('inf') else best[amount]


def check():
    assert min_coins([1, 3, 4], 6) == 2
    assert min_coins([2], 3) is None
    assert min_coins([], 0) == 0
    assert min_coins([], 2) is None


if __name__ == "__main__":
    check()
    print("PASS: Minimum coin count")
