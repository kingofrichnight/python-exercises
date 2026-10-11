"""Count function calls

Concepts: decorators, functools.wraps, function attributes
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Write a decorator that counts calls, including failing calls, in a calls
attribute while preserving the wrapped function’s name and docstring.
This simple counter is intended for single-threaded use.

HINT
Use wraps before returning the wrapper.

STRETCH
Build a parameterized decorator that logs only every nth call.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from functools import wraps

def count_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return function(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def check():
    @count_calls
    def divide(a, b):
        """Divide two numbers."""
        return a / b
    assert divide(6, b=2) == 3
    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass
    assert divide.calls == 2
    assert divide.__name__ == 'divide'
    assert divide.__doc__ == 'Divide two numbers.'


if __name__ == "__main__":
    check()
    print("PASS: Count function calls")
