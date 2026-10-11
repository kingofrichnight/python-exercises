"""Stable leaderboard ranking

Concepts: sorted, lambda, enumerate, tuple keys
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given (name, score) pairs, return (position, name, score) sorted by descending
score, then ascending name. Positions start at 1 and do not share ranks on ties.

HINT
Negate a numeric sort key to reverse only that component.

STRETCH
Implement competition ranking with shared positions.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def rank(players):
    ordered = sorted(players, key=lambda player: (-player[1], player[0]))
    return [(position, name, score) for position, (name, score) in enumerate(ordered, 1)]


def check():
    assert rank([('Zoe', 8), ('Ada', 9), ('Bo', 9)]) == [
        (1, 'Ada', 9), (2, 'Bo', 9), (3, 'Zoe', 8)]
    assert rank([]) == []


if __name__ == "__main__":
    check()
    print("PASS: Stable leaderboard ranking")
