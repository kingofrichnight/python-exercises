"""Structural typing for output sinks

Concepts: Protocol, structural subtyping, annotations
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Define a TextSink protocol with write(str) -> int. Write a report function
accepting any compatible object and emitting one newline-terminated line for
each supplied string. Return the total count reported by write().

HINT
Compatible objects need not inherit from the protocol.

STRETCH
Use an optional static checker to detect an incompatible sink.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from typing import Protocol
from collections.abc import Iterable

class TextSink(Protocol):
    def write(self, text: str) -> int: ...

def write_report(lines: Iterable[str], sink: TextSink) -> int:
    return sum(sink.write(line + '\n') for line in lines)


def check():
    from io import StringIO
    sink = StringIO()
    assert write_report(['one', 'two'], sink) == 8
    assert sink.getvalue() == 'one\ntwo\n'
    assert write_report([], sink) == 0


if __name__ == "__main__":
    check()
    print("PASS: Structural typing for output sinks")
