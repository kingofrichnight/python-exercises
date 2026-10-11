"""Word frequency table

Concepts: split, strip, dict.get, punctuation
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Count whitespace-separated words after case folding and stripping ASCII
punctuation from their ends. Ignore empty tokens; keep internal punctuation.
"Hi, hi!" -> {"hi": 2}. This is deliberately not a full linguistic tokenizer.

HINT
Normalize before counting.

STRETCH
Compare this tokenization to a regex-based approach.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import string

def word_counts(text):
    counts = {}
    for token in text.casefold().split():
        word = token.strip(string.punctuation)
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def check():
    assert word_counts('Hi, hi! ---') == {'hi': 2}
    assert word_counts("don't stop") == {"don't": 1, 'stop': 1}
    assert word_counts('') == {}


if __name__ == "__main__":
    check()
    print("PASS: Word frequency table")
