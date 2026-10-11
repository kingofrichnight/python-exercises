"""Project: dependency-aware build ordering

Concepts: topological sort, graph validation, heap, cycles
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given a mapping of task names to prerequisite task names, return a valid
build order. Choose alphabetically among ready tasks. Reject unknown dependencies
and cycles with ValueError. Repeated dependencies count only once; empty input -> [].

HINT
Track prerequisites and reverse edges; enqueue a task when its set becomes empty.

STRETCH
Execute independent tasks concurrently while preserving failure propagation.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import heapq

def build_order(dependencies):
    remaining = {name: set(prerequisites) for name, prerequisites in dependencies.items()}
    names = set(remaining)
    if any(not prerequisites <= names for prerequisites in remaining.values()):
        raise ValueError('unknown dependency')
    dependents = {name: [] for name in names}
    for name, prerequisites in remaining.items():
        for prerequisite in prerequisites:
            dependents[prerequisite].append(name)
    ready = [name for name, prerequisites in remaining.items() if not prerequisites]
    heapq.heapify(ready)
    result = []
    while ready:
        name = heapq.heappop(ready)
        result.append(name)
        for dependent in dependents[name]:
            remaining[dependent].remove(name)
            if not remaining[dependent]:
                heapq.heappush(ready, dependent)
    if len(result) != len(names):
        raise ValueError('dependency cycle')
    return result


def check():
    assert build_order({'test': ['build'], 'build': ['lint'], 'lint': []}) == ['lint', 'build', 'test']
    assert build_order({'b': [], 'a': [], 'c': ['a', 'a']}) == ['a', 'b', 'c']
    assert build_order({}) == []
    for graph in ({'a': ['b'], 'b': ['a']}, {'a': ['missing']}):
        try:
            build_order(graph)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid graph accepted')


if __name__ == "__main__":
    check()
    print("PASS: Project: dependency-aware build ordering")
