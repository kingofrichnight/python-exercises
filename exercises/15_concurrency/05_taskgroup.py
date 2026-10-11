"""Cancel sibling tasks on failure

Concepts: TaskGroup, ExceptionGroup, except*, cancellation
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Start a waiting task and a task that raises ValueError after the first has
started. Use TaskGroup to cancel the waiting sibling. Verify its finally block
runs and handle the grouped ValueError with except*. Avoid timing-dependent sleeps.

HINT
Use an Event to coordinate the test rather than guessing durations.

STRETCH
Add an asyncio.timeout boundary and verify cleanup still happens.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import asyncio

async def run_group():
    events = []
    started = asyncio.Event()
    async def waiting():
        try:
            started.set()
            await asyncio.Event().wait()
        finally:
            events.append('cleaned')
    async def failing():
        await started.wait()
        raise ValueError('failed')
    try:
        async with asyncio.TaskGroup() as group:
            group.create_task(waiting())
            group.create_task(failing())
    except* ValueError as errors:
        events.append(f'errors:{len(errors.exceptions)}')
    return events


def check():
    assert asyncio.run(run_group()) == ['cleaned', 'errors:1']


if __name__ == "__main__":
    check()
    print("PASS: Cancel sibling tasks on failure")
