"""Shortest path in an unweighted graph

Concepts: BFS, deque, graph traversal, parent map
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Given an adjacency mapping, start, and goal, return a shortest path as a list
of nodes or None when unreachable. Missing keys have no outgoing edges.
Nodes must be hashable; neighbor order breaks ties. start == goal -> [start].

HINT
Mark nodes visited when enqueuing to avoid cycles and duplicate work.

STRETCH
Implement Dijkstra’s algorithm for nonnegative weighted edges.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from collections import deque

def shortest_path(graph, start, goal):
    queue = deque([start])
    parent = {start: start}
    while queue:
        node = queue.popleft()
        if node == goal:
            path = [node]
            while node != start:
                node = parent[node]
                path.append(node)
            return path[::-1]
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return None


def check():
    graph = {'a': ['b', 'c'], 'b': ['a', 'd'], 'c': ['d']}
    assert shortest_path(graph, 'a', 'd') == ['a', 'b', 'd']
    assert shortest_path(graph, 'a', 'z') is None
    assert shortest_path({}, 'a', 'a') == ['a']


if __name__ == "__main__":
    check()
    print("PASS: Shortest path in an unweighted graph")
