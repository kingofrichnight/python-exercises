"""Import and inspect a module

Concepts: importlib, modules, namespaces, main guard
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Load a trusted standard-library module by name and return its public names
in sorted order. Never use this pattern with untrusted module names: importing
a module executes its top-level code. Demonstrate math without shadowing it.

HINT
vars(module) exposes its namespace.

STRETCH
Create a package with __init__.py and compare absolute and relative imports.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import importlib

def public_names(module_name):
    module = importlib.import_module(module_name)
    return sorted(name for name in vars(module) if not name.startswith('_'))


def check():
    names = public_names('math')
    assert 'sqrt' in names and 'pi' in names
    assert names == sorted(names)
    assert all(not name.startswith('_') for name in names)


if __name__ == "__main__":
    check()
    print("PASS: Import and inspect a module")
