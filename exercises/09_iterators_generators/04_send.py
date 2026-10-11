"""Running mean coroutine

Concepts: generator.send, priming, finally, close
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Create a generator that initially yields None, accepts numbers via send(),
and yields the running arithmetic mean. Append "closed" to an event list when
the primed generator is closed. Inputs are assumed numeric and finite.

HINT
send(value) supplies the result of the suspended yield expression.

STRETCH
Add reset commands without confusing them with numeric input.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def running_mean(events):
    total, count = 0.0, 0
    try:
        value = yield None
        while True:
            total += value
            count += 1
            value = yield total / count
    finally:
        events.append('closed')


def check():
    events = []
    means = running_mean(events)
    assert next(means) is None
    assert means.send(2) == 2
    assert means.send(4) == 3
    means.close()
    assert events == ['closed']


if __name__ == "__main__":
    check()
    print("PASS: Running mean coroutine")
