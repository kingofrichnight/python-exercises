"""Bounded retries for transient failures

Concepts: decorator factories, exception tuples, reraise
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Create retry(attempts, exceptions) to retry a synchronous function only for
the supplied exception types. Attempts includes the first call and must be
positive. Re-raise the final failure. This exercise intentionally has no sleeping.

HINT
Catch only failures the caller classifies as transient.

STRETCH
Inject a sleep function for testable exponential backoff; consider idempotency.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from functools import wraps

def retry(attempts, exceptions=(TimeoutError,)):
    if attempts < 1:
        raise ValueError('attempts must be positive')
    def decorate(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return function(*args, **kwargs)
                except exceptions:
                    if attempt == attempts - 1:
                        raise
        return wrapper
    return decorate


def check():
    attempts = []
    @retry(3)
    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise TimeoutError('temporary')
        return 'ok'
    assert flaky() == 'ok' and len(attempts) == 3
    @retry(2)
    def broken():
        raise ValueError('permanent')
    try:
        broken()
    except ValueError:
        pass
    else:
        raise AssertionError('failure swallowed')


if __name__ == "__main__":
    check()
    print("PASS: Bounded retries for transient failures")
