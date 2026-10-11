"""Project: bounded LRU cache

Concepts: OrderedDict, eviction, sentinel-free lookup, classes
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Implement an LRU cache with positive integer capacity, put(key,value),
and get(key). Reads and writes make a key most recently used. Evict the least
recently used key when capacity is exceeded. Missing get raises KeyError.
Values may be None; updating a key must not increase the number of entries.

HINT
OrderedDict supports moving an entry to the end in constant time.

STRETCH
Add TTL expiration with an injected monotonic clock and tests.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        if type(capacity) is not int or capacity <= 0:
            raise ValueError('capacity must be a positive integer')
        self.capacity = capacity
        self._data = OrderedDict()

    def get(self, key):
        value = self._data[key]
        self._data.move_to_end(key)
        return value

    def put(self, key, value):
        self._data[key] = value
        self._data.move_to_end(key)
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)


def check():
    cache = LRUCache(2)
    cache.put('a', None)
    cache.put('b', 2)
    assert cache.get('a') is None
    cache.put('c', 3)
    try:
        cache.get('b')
    except KeyError:
        pass
    else:
        raise AssertionError('least-recent entry not evicted')
    cache.put('a', 4)
    assert cache.get('c') == 3 and cache.get('a') == 4


if __name__ == "__main__":
    check()
    print("PASS: Project: bounded LRU cache")
