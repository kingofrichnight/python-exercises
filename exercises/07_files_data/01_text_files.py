"""Summarize a UTF-8 text file

Concepts: pathlib, with, encoding, streaming
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given a path, return a dictionary containing line, whitespace-word, and
character counts. Count newline characters; use universal newline translation.
Read line by line. Missing files should raise FileNotFoundError.

HINT
Iterate the file object instead of reading everything at once.

STRETCH
Add a count of nonblank lines.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from pathlib import Path

def summarize(path):
    counts = {'lines': 0, 'words': 0, 'characters': 0}
    with Path(path).open(encoding='utf-8') as source:
        for line in source:
            counts['lines'] += 1
            counts['words'] += len(line.split())
            counts['characters'] += len(line)
    return counts


def check():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as folder:
        path = Path(folder) / 'sample.txt'
        path.write_text('hi all\nbye', encoding='utf-8')
        assert summarize(path) == {'lines': 2, 'words': 3, 'characters': 10}
        path.write_text('', encoding='utf-8')
        assert summarize(path) == {'lines': 0, 'words': 0, 'characters': 0}


if __name__ == "__main__":
    check()
    print("PASS: Summarize a UTF-8 text file")
