"""Register classes at definition time

Concepts: type, metaclasses, class creation
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Create a metaclass that registers classes declaring a nonempty string key
in their own namespace. Reject duplicate keys. Classes without a declared key
are not registered. This is a learning example; prefer simpler designs when possible.

HINT
The metaclass receives the class body as a namespace dictionary.

STRETCH
Implement the same registry using __init_subclass__ or a class decorator.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

class RegistryMeta(type):
    registry = {}

    def __new__(mcls, name, bases, namespace):
        key = namespace.get('key')
        if key is not None:
            if not isinstance(key, str) or not key:
                raise ValueError('key must be a nonempty string')
            if key in mcls.registry:
                raise ValueError('duplicate key')
        cls = super().__new__(mcls, name, bases, namespace)
        if key is not None:
            mcls.registry[key] = cls
        return cls


def check():
    RegistryMeta.registry.clear()
    class Base(metaclass=RegistryMeta):
        pass
    class JsonPlugin(Base):
        key = 'json'
    assert RegistryMeta.registry == {'json': JsonPlugin}
    try:
        class Duplicate(Base):
            key = 'json'
    except ValueError:
        pass
    else:
        raise AssertionError('duplicate registration accepted')


if __name__ == "__main__":
    check()
    print("PASS: Register classes at definition time")
