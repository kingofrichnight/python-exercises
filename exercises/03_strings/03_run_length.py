"""Run-length encoding

Concepts: iteration, state, tuples, join
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Encode consecutive characters as a list of (character, count) tuples.
"aaabb" -> [("a", 3), ("b", 2)]; empty input -> []. Also decode a valid encoding.

HINT
Track the last run instead of searching the entire output.

STRETCH
Validate malformed encodings and reject negative counts.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def encode(text):
    result = []
    for char in text:
        if result and result[-1][0] == char:
            previous, count = result[-1]
            result[-1] = (previous, count + 1)
        else:
            result.append((char, 1))
    return result

def decode(runs):
    return ''.join(char * count for char, count in runs)


def check():
    assert encode('aaabb') == [('a', 3), ('b', 2)]
    assert encode('') == []
    for text in ('', 'a', 'ababa', '11122', '🙂🙂!'):
        assert decode(encode(text)) == text


if __name__ == "__main__":
    check()
    print("PASS: Run-length encoding")
