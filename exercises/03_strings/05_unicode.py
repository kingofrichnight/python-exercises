"""Unicode and byte boundaries

Concepts: unicodedata, encode, decode, NFC
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Normalize Unicode text to NFC, encode it as UTF-8 bytes, and decode it back.
Return (bytes, decoded_text). Canonically equivalent accents should match.

HINT
A byte count is not necessarily a character count.

STRETCH
Explain why code points are not always user-perceived characters.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import unicodedata

def round_trip(text):
    normalized = unicodedata.normalize('NFC', text)
    encoded = normalized.encode('utf-8')
    return encoded, encoded.decode('utf-8')


def check():
    assert round_trip('caf\u00e9') == round_trip('cafe\u0301')
    data, text = round_trip('🙂')
    assert len(data) == 4 and len(text) == 1
    assert round_trip('') == (b'', '')


if __name__ == "__main__":
    check()
    print("PASS: Unicode and byte boundaries")
