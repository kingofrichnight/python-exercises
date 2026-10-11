"""Compare timezone-aware timestamps

Concepts: datetime, timezone, ISO 8601, timedelta
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given two ISO 8601 timestamps with explicit UTC offsets, return elapsed
seconds from start to end. Reject naive timestamps. Different offsets may
represent the same instant. Negative elapsed times are valid.

HINT
Convert both instants to UTC before subtraction.

STRETCH
Explore ZoneInfo and ambiguous daylight-saving times.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from datetime import datetime, timezone

def elapsed_seconds(start, end):
    values = [datetime.fromisoformat(text) for text in (start, end)]
    if any(value.tzinfo is None or value.utcoffset() is None for value in values):
        raise ValueError('timezone offset required')
    first, last = [value.astimezone(timezone.utc) for value in values]
    return (last - first).total_seconds()


def check():
    assert elapsed_seconds('2025-01-01T12:00:00+00:00', '2025-01-01T07:00:00-05:00') == 0
    assert elapsed_seconds('2025-01-01T00:00:00+00:00', '2025-01-02T00:00:00+00:00') == 86400
    try:
        elapsed_seconds('2025-01-01T00:00:00', '2025-01-01T00:00:00Z')
    except ValueError:
        pass
    else:
        raise AssertionError('naive timestamp accepted')


if __name__ == "__main__":
    check()
    print("PASS: Compare timezone-aware timestamps")
