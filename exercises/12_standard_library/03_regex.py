"""Parse structured log lines

Concepts: re, named groups, fullmatch
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Parse "LEVEL: message" where LEVEL is INFO, WARNING, or ERROR and message
is nonempty on one line. Return (level, message); reject malformed lines with
ValueError. Require exactly one separator space, but preserve message whitespace.

HINT
Use fullmatch instead of search to validate the entire input.

STRETCH
Add timestamps and validate them with datetime rather than regex alone.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import re

PATTERN = re.compile(r'(?P<level>INFO|WARNING|ERROR): (?P<message>.+)')

def parse_log(line):
    match = PATTERN.fullmatch(line)
    if match is None:
        raise ValueError('invalid log line')
    return match['level'], match['message']


def check():
    assert parse_log('ERROR: disk full') == ('ERROR', 'disk full')
    for line in ('DEBUG: hi', 'INFO:', 'INFO: ', 'INFO: hi\n'):
        try:
            parse_log(line)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid line accepted')


if __name__ == "__main__":
    check()
    print("PASS: Parse structured log lines")
