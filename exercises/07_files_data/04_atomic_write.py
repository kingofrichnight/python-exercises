"""Replace a file after a successful write

Concepts: tempfile, os.replace, finally, pathlib
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Write UTF-8 text to a temporary sibling file and replace the destination only
after writing and closing succeeds. Clean up leftover temporary files on errors.
The destination parent must exist. This is not a power-loss durability guarantee.

HINT
Place the temporary file on the same filesystem as its destination.

STRETCH
Inject a write failure and verify the previous destination survives.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import os
import tempfile
from pathlib import Path

def replace_text(destination, text):
    destination = Path(destination)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8',
                                         dir=destination.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(text)
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def check():
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / 'note.txt'
        replace_text(path, 'first')
        replace_text(path, 'second')
        assert path.read_text(encoding='utf-8') == 'second'
        assert list(Path(folder).iterdir()) == [path]


if __name__ == "__main__":
    check()
    print("PASS: Replace a file after a successful write")
