"""Streaming log pipeline

Concepts: generator expressions, yield from, lazy composition
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given an iterable of log-line groups, lazily flatten groups and yield the
trimmed message from lines starting exactly with "ERROR:". Ignore other lines.

HINT
Keep each stage iterable instead of building intermediate lists.

STRETCH
Include line numbers and source group identifiers.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def flatten_groups(groups):
    for group in groups:
        yield from group

def error_messages(groups):
    lines = flatten_groups(groups)
    return (line.removeprefix('ERROR:').strip()
            for line in lines if line.startswith('ERROR:'))


def check():
    groups = [['INFO: ok', 'ERROR: disk'], [], ['ERROR: network ']]
    assert list(error_messages(groups)) == ['disk', 'network']
    assert list(error_messages([])) == []


if __name__ == "__main__":
    check()
    print("PASS: Streaming log pipeline")
