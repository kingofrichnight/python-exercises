"""Validate JSON settings

Concepts: json, serialization, schema validation
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Decode JSON text containing an object with a nonempty string name and a
boolean enabled field. Default enabled to True. Return only those two fields.
Reject malformed JSON, wrong shapes, or wrong field types with ValueError.

HINT
Parsing JSON does not validate your application’s schema.

STRETCH
Add versioned settings migrations.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import json

def load_settings(text):
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError('expected an object')
    name = data.get('name')
    enabled = data.get('enabled', True)
    if not isinstance(name, str) or not name.strip() or type(enabled) is not bool:
        raise ValueError('invalid settings')
    return {'name': name.strip(), 'enabled': enabled}


def check():
    assert load_settings('{"name": " Ada "}') == {'name': 'Ada', 'enabled': True}
    for text in ('[]', '{}', '{"name":"a","enabled":1}', 'not json'):
        try:
            load_settings(text)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid settings accepted')


if __name__ == "__main__":
    check()
    print("PASS: Validate JSON settings")
