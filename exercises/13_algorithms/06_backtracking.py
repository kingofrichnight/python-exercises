"""Generate balanced parentheses

Concepts: backtracking, pruning, recursion
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return all balanced parentheses strings with n pairs, in lexicographic
order. n is a nonnegative integer; n=0 -> [""]. Reject negative n.
Use partial-state validity to avoid exploring impossible prefixes.

HINT
A prefix cannot contain more closing than opening parentheses.

STRETCH
Yield results lazily and analyze the Catalan-number output size.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def parentheses(n):
    if n < 0:
        raise ValueError('n must be nonnegative')
    result = []
    def visit(prefix, opened, closed):
        if closed == n:
            result.append(prefix)
            return
        if opened < n:
            visit(prefix + '(', opened + 1, closed)
        if closed < opened:
            visit(prefix + ')', opened, closed + 1)
    visit('', 0, 0)
    return result


def check():
    assert parentheses(0) == ['']
    assert parentheses(2) == ['(())', '()()']
    assert len(parentheses(3)) == 5


if __name__ == "__main__":
    check()
    print("PASS: Generate balanced parentheses")
