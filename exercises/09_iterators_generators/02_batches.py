"""Lazy batches

Concepts: yield, iter, islice, bounded memory
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Yield lists of at most size items from any iterable. Preserve order and
include the last partial batch. Reject nonpositive size. Do not load the
entire input. Validation happens when the generator is first advanced.

HINT
Convert one bounded slice at a time.

STRETCH
Add strict mode that rejects an incomplete last batch.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from itertools import islice

def batches(iterable, size):
    if size <= 0:
        raise ValueError('size must be positive')
    iterator = iter(iterable)
    while True:
        batch = list(islice(iterator, size))
        if not batch:
            return
        yield batch


def check():
    assert list(batches(range(5), 2)) == [[0, 1], [2, 3], [4]]
    assert list(batches([], 3)) == []
    from itertools import count
    stream = batches(count(), 2)
    assert next(stream) == [0, 1]
    assert next(stream) == [2, 3]


if __name__ == "__main__":
    check()
    print("PASS: Lazy batches")
