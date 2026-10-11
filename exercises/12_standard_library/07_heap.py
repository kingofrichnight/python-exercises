"""Stable priority queue

Concepts: heapq, itertools.count, tuple ordering
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Implement a min-priority queue. Lower numeric priority comes out first;
equal priorities preserve insertion order. Payloads need not be comparable.
Popping an empty queue raises IndexError.

HINT
A monotonically increasing tie-breaker prevents payload comparisons.

STRETCH
Add cancellation using tombstones.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import heapq
from itertools import count

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._sequence = count()

    def push(self, priority, item):
        heapq.heappush(self._heap, (priority, next(self._sequence), item))

    def pop(self):
        return heapq.heappop(self._heap)[2]


def check():
    queue = PriorityQueue()
    queue.push(2, {'name': 'later'})
    queue.push(1, {'name': 'first'})
    queue.push(1, {'name': 'second'})
    assert [queue.pop()['name'] for _ in range(3)] == ['first', 'second', 'later']
    try:
        queue.pop()
    except IndexError:
        pass
    else:
        raise AssertionError('empty pop succeeded')


if __name__ == "__main__":
    check()
    print("PASS: Stable priority queue")
