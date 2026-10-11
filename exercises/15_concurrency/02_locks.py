"""Protect a shared counter

Concepts: Lock, critical section, futures
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Implement a counter with an increment method protected by a lock. Run a
fixed number of worker tasks, each incrementing a fixed number of times.
Read the final value after all futures complete.

HINT
Protect the whole read-modify-write operation.

STRETCH
Compare shared mutation with workers returning independent subtotals.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from threading import Lock
from concurrent.futures import ThreadPoolExecutor

class Counter:
    def __init__(self):
        self.value = 0
        self._lock = Lock()

    def increment(self):
        with self._lock:
            self.value += 1

def increment_many(counter, count):
    for _ in range(count):
        counter.increment()


def check():
    counter = Counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(increment_many, counter, 500) for _ in range(4)]
        for future in futures:
            future.result()
    assert counter.value == 2000


if __name__ == "__main__":
    check()
    print("PASS: Protect a shared counter")
