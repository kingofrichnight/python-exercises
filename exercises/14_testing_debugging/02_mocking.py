"""Test an HTTP client without network access

Concepts: Mock, dependency injection, HTTP status, JSON
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Fetch a profile using an injected get(url, timeout=...) callable. Call
raise_for_status() before decoding JSON. Require a JSON object with a string
name. Use mock responses to test success and failure; do not access a real API.

HINT
Inject the network boundary instead of making tests depend on a server.

STRETCH
Test malformed JSON, timeout errors, and invalid response schemas.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def fetch_name(get, url):
    response = get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict) or not isinstance(data.get('name'), str):
        raise ValueError('profile must contain a string name')
    return data['name']


def check():
    from unittest.mock import Mock
    response = Mock()
    response.json.return_value = {'name': 'Ada'}
    get = Mock(return_value=response)
    assert fetch_name(get, 'https://example.invalid/profile') == 'Ada'
    get.assert_called_once_with('https://example.invalid/profile', timeout=5)
    response.raise_for_status.assert_called_once_with()
    response.json.reset_mock()
    response.raise_for_status.side_effect = RuntimeError('HTTP failure')
    try:
        fetch_name(get, 'https://example.invalid/profile')
    except RuntimeError:
        pass
    else:
        raise AssertionError('HTTP error swallowed')
    response.json.assert_not_called()


if __name__ == "__main__":
    check()
    print("PASS: Test an HTTP client without network access")
