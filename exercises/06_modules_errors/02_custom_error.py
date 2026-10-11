"""Validate a configuration value

Concepts: custom exceptions, chaining, try/except
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Parse a text TCP port in 1..65535. Raise ConfigError for bad text or an
out-of-range value. Preserve the conversion ValueError as the cause when parsing fails.

HINT
Use raise ... from error to preserve context.

STRETCH
Report multiple configuration errors together.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

class ConfigError(ValueError):
    pass

def parse_port(text):
    try:
        port = int(text)
    except ValueError as error:
        raise ConfigError('port must be an integer') from error
    if not 1 <= port <= 65535:
        raise ConfigError('port must be between 1 and 65535')
    return port


def check():
    assert parse_port('443') == 443
    for text in ('0', '65536', 'oops'):
        try:
            parse_port(text)
        except ConfigError as error:
            if text == 'oops':
                assert isinstance(error.__cause__, ValueError)
        else:
            raise AssertionError('invalid port accepted')


if __name__ == "__main__":
    check()
    print("PASS: Validate a configuration value")
