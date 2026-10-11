"""Command-line unit converter

Concepts: argparse, CLI, choices, optional arguments
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Build a CLI parser accepting a numeric temperature and --to C or F (default F).
Return the converted number from main(argv), allowing tests to supply arguments.
The file main guard runs checks; call main([...]) to exercise CLI parsing directly.

HINT
Accept argv explicitly for testability.

STRETCH
Create a standalone CLI entry point with subcommands.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import argparse

def main(argv=None):
    parser = argparse.ArgumentParser(description='Convert between Celsius and Fahrenheit')
    parser.add_argument('temperature', type=float)
    parser.add_argument('--to', choices=['C', 'F'], default='F')
    args = parser.parse_args(argv)
    if args.to == 'F':
        return args.temperature * 9 / 5 + 32
    return (args.temperature - 32) * 5 / 9


def check():
    assert main(['0']) == 32
    assert main(['212', '--to', 'C']) == 100
    assert main(['-40', '--to', 'F']) == -40


if __name__ == "__main__":
    check()
    print("PASS: Command-line unit converter")
