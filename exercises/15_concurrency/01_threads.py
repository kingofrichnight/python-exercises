"""Ordered thread-pool results

Concepts: ThreadPoolExecutor, map, executor lifetime
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Use a thread pool to apply a supplied function to inputs and return results
in input order. Propagate worker exceptions. Threads are useful for blocking
I/O; this tiny arithmetic check demonstrates orchestration, not a speedup.

HINT
executor.map preserves input order.

STRETCH
Use as_completed when completion order is preferred.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from concurrent.futures import ThreadPoolExecutor

def threaded_map(function, items, workers=4):
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(function, items))


def check():
    assert threaded_map(lambda n: n * n, [3, 1, 2]) == [9, 1, 4]
    assert threaded_map(str, []) == []
    try:
        threaded_map(lambda n: 10 // n, [1, 0])
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError('worker error swallowed')


if __name__ == "__main__":
    check()
    print("PASS: Ordered thread-pool results")
