"""Capture structured diagnostic messages

Concepts: logging, handlers, formatting, cleanup
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Validate integer quantities and log accepted values at INFO or rejected
negative values at WARNING. Capture logs in memory during checks, restoring
the logger’s previous level and propagation state afterward.

HINT
Library code should not configure the application’s root logger.

STRETCH
Add contextual fields with LoggerAdapter.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import logging

logger = logging.getLogger(__name__)

def accept_quantity(quantity):
    if quantity < 0:
        logger.warning('rejected quantity=%s', quantity)
        return False
    logger.info('accepted quantity=%s', quantity)
    return True


def check():
    from io import StringIO
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter('%(levelname)s:%(message)s'))
    old_level, old_propagate = logger.level, logger.propagate
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    try:
        assert accept_quantity(2)
        assert not accept_quantity(-1)
        assert stream.getvalue().splitlines() == ['INFO:accepted quantity=2', 'WARNING:rejected quantity=-1']
    finally:
        logger.removeHandler(handler)
        handler.close()
        logger.setLevel(old_level)
        logger.propagate = old_propagate


if __name__ == "__main__":
    check()
    print("PASS: Capture structured diagnostic messages")
