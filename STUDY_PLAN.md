# Study plan

Use milestones rather than rushing to a fixed deadline. A session can consist
of one exercise, extra tests, and one stretch challenge. Revisit difficult
exercises the next day without looking at the solution.

| Milestone | Sections | You are ready to move on when… |
| --- | --- | --- |
| Foundations | 01–04 | You can trace loops, choose containers, and explain mutation versus copying. |
| Reusable programs | 05–07 | You can design functions, handle failures, and read/write validated data. |
| Object design | 08 | You can choose composition or inheritance and keep state consistent. |
| Python protocols | 09–11 | You can explain iteration, lazy evaluation, decorators, cleanup, and typing. |
| Standard library | 12 | You can select tools for text, dates, decimals, binary data, and collections. |
| Algorithms | 13 | You can justify correctness, complexity, and boundary behavior. |
| Engineering | 14–15 | You can isolate external dependencies, test failures, and manage concurrent tasks. |
| Integration | 16 | You can rebuild a project independently and add a tested feature. |

## Practice loop

1. Read only the problem and hint at the top of the file.
2. Write your own function or class in a scratch file.
3. Predict outputs before running examples.
4. Test the happy path, an empty/minimum case, and an invalid case where applicable.
5. Compare with the reference and explain each difference.
6. Finish the stretch challenge or document what remains unclear.

## Environment and tooling exercises

The repository runs without third-party packages. To practice isolated environments:

```sh
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` in Windows PowerShell, or
`source .venv/bin/activate` in a POSIX shell. If your system restricts script
activation, invoke `.venv\Scripts\python.exe` directly on Windows. Do not change
security policy just to activate an environment.

Use `python -m pip --version` to inspect the package installer in that environment.
Explore `python -m pdb path/to/exercise.py` for stepping through a solution. Learn
breakpoints, stepping, inspecting local variables, and reading tracebacks.

After this curriculum, create a small package with `pyproject.toml`, a `src/`
layout, tests, and a console entry point. Packaging and third-party frameworks
are follow-on topics, not fully covered by the self-contained exercises here.
