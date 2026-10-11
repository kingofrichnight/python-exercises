"""Bound asynchronous work

Concepts: async/await, Semaphore, gather, asyncio.run
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Apply an asynchronous worker to inputs with at most limit calls active at
once. Return results in input order. Reject nonpositive limits. Use a simulated
worker in tests, not live requests. This function is designed for successful jobs;
see the TaskGroup exercise for structured sibling cancellation on failure.

HINT
Hold a semaphore slot across the entire awaited operation.

STRETCH
Use a queue and fixed workers to avoid creating one task per input.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import asyncio

async def bounded_map(worker, items, limit):
    if limit <= 0:
        raise ValueError('limit must be positive')
    semaphore = asyncio.Semaphore(limit)
    async def run(item):
        async with semaphore:
            return await worker(item)
    return await asyncio.gather(*(run(item) for item in items))


def check():
    async def scenario():
        active = peak = 0
        async def worker(number):
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            try:
                await asyncio.sleep(0)
                return number * 2
            finally:
                active -= 1
        assert await bounded_map(worker, range(5), 2) == [0, 2, 4, 6, 8]
        assert peak == 2 and active == 0
        assert await bounded_map(worker, [], 1) == []
    asyncio.run(scenario())


if __name__ == "__main__":
    check()
    print("PASS: Bound asynchronous work")
