# Python Exercises: Basics to Advanced

80 self-contained, solved exercises across 16 ordered sections. Every
exercise has a problem statement, concepts, hint, complete reference solution,
executable checks, and a stretch challenge **in the same Python file**.

## Start here

Use Python **3.11 or newer**. All exercises use only the standard library: no
packages, API keys, paid services, or internet access are needed to run them.

```sh
python exercises/01_basics/01_greeting.py
python run_checks.py
python run_checks.py --section 08_oop
python -m unittest discover -s tests -v
```

On Windows, `py` may replace `python`; on macOS/Linux, use `python3` if needed.
Run commands from the repository root. Do not use `python -O`: it disables
the assertion checks. `run_checks.py` rejects optimized mode explicitly.

## How to learn

1. Work through folders and numbered files in order. Read the statement and hint.
2. Try your own implementation in a separate scratch file before reading the solution.
3. Run the provided checks and add at least two cases of your own.
4. Explain why the solution works, then try the stretch problem.
5. Complete the projects without looking at their solutions before moving on.

The reference solutions are intentionally visible because each file contains both
the statement and code. Stretch challenges are unsolved extensions.

## Learning path

| Section | Exercises |
| --- | ---: |
| [01_basics](exercises/01_basics) | 5 |
| [02_control_flow](exercises/02_control_flow) | 5 |
| [03_strings](exercises/03_strings) | 5 |
| [04_collections](exercises/04_collections) | 5 |
| [05_functions](exercises/05_functions) | 5 |
| [06_modules_errors](exercises/06_modules_errors) | 4 |
| [07_files_data](exercises/07_files_data) | 5 |
| [08_oop](exercises/08_oop) | 5 |
| [09_iterators_generators](exercises/09_iterators_generators) | 4 |
| [10_decorators_context](exercises/10_decorators_context) | 4 |
| [11_typing_internals](exercises/11_typing_internals) | 4 |
| [12_standard_library](exercises/12_standard_library) | 8 |
| [13_algorithms](exercises/13_algorithms) | 6 |
| [14_testing_debugging](exercises/14_testing_debugging) | 4 |
| [15_concurrency](exercises/15_concurrency) | 5 |
| [16_projects](exercises/16_projects) | 6 |

See [CATALOG.md](CATALOG.md) for links to every exercise and its concepts, and
[STUDY_PLAN.md](STUDY_PLAN.md) for milestones. Each folder also has its own index.

## Scope

Covers expressions, control flow, strings, containers, functions, recursion,
modules, files, exceptions, OOP, typing, iterators, generators, decorators,
context managers, regular expressions, dates, numeric tools, algorithms,
testing, mocking, logging, CLI design, SQLite, serialization, concurrency,
asyncio, and small applications. Advanced examples introduce descriptors,
abstract classes, protocols, caching, and metaclasses.

No finite repository covers every Python ecosystem topic. Web frameworks,
NumPy/pandas, machine learning, GUI frameworks, deployment, and native extensions
are follow-on subjects outside this standard-library curriculum. Type hints
document contracts; Python does not enforce them at runtime. Static type checking
requires an optional external checker and is not part of the dependency-free run.

## Verification and safety

Each exercise exports `check()`. The runner executes every file in a fresh process,
uses a timeout, and reports failures with output. File exercises use temporary
directories; database examples use in-memory SQLite; concurrency jobs are tiny
and deterministic. HTTP exercises use injected fake responses, not live requests.
Examples are educational and do not claim production readiness.

The `tests` directory contains additional regression checks for the algorithms
and validation boundaries. GitHub Actions runs the suite on Python 3.11–3.14.

## Contributing

Add an exercise with a module docstring (problem, inputs/outputs, behavior at the
boundaries, hint, stretch), a readable solution, and a `check()` function. Keep
imports free of side effects and put executable examples behind the main guard.
Update both indexes and run the verification commands before committing.

