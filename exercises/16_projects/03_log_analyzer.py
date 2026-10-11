"""Project: streaming status-code report

Concepts: streaming, Counter, parsing, malformed records
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Process lines formatted METHOD PATH STATUS. Count status codes and the
three most frequent paths among valid records. Accept only GET/POST/PUT/DELETE,
paths beginning with /, and integer statuses 100..599. Count malformed records
separately. Break path-frequency ties alphabetically.

HINT
Consume lines incrementally; store only aggregate counts.

STRETCH
Add time-window filters and estimate memory use with many unique paths.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

from collections import Counter

def analyze(lines):
    statuses, paths = Counter(), Counter()
    invalid = 0
    for line in lines:
        parts = line.split()
        if len(parts) != 3:
            invalid += 1
            continue
        method, path, code = parts
        try:
            status = int(code)
        except ValueError:
            invalid += 1
            continue
        if method not in {'GET', 'POST', 'PUT', 'DELETE'} or not path.startswith('/') or not 100 <= status <= 599:
            invalid += 1
            continue
        statuses[status] += 1
        paths[path] += 1
    return {'statuses': dict(statuses),
            'top_paths': sorted(paths.items(), key=lambda pair: (-pair[1], pair[0]))[:3],
            'invalid': invalid}


def check():
    report = analyze(iter(['GET /a 200', 'GET /b 404', 'POST /a 201', 'bad', 'GET /x 999']))
    assert report == {'statuses': {200: 1, 404: 1, 201: 1},
                      'top_paths': [('/a', 2), ('/b', 1)], 'invalid': 2}
    assert analyze([]) == {'statuses': {}, 'top_paths': [], 'invalid': 0}


if __name__ == "__main__":
    check()
    print("PASS: Project: streaming status-code report")
