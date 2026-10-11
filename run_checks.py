"""Run all exercise files in isolated processes; return nonzero on failures."""

import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def main(argv=None):
    if not __debug__:
        raise SystemExit('Do not use -O: exercise assertions must be enabled.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--section', help='Exact folder name, e.g. 08_oop')
    args = parser.parse_args(argv)
    files = sorted((ROOT / 'exercises').glob('*/*.py'))
    if args.section:
        files = [path for path in files if path.parent.name == args.section]
    if not files:
        parser.error('no exercises matched')
    failures = []
    for path in files:
        relative = path.relative_to(ROOT)
        try:
            result = subprocess.run(
                [sys.executable, '-I', str(path)], cwd=ROOT,
                capture_output=True, text=True, encoding='utf-8', errors='replace',
                timeout=45,
            )
        except subprocess.TimeoutExpired:
            failures.append(str(relative))
            print(f'FAIL {relative}: exceeded 45 seconds')
            continue
        if result.returncode:
            failures.append(str(relative))
            print(f'FAIL {relative}\n{result.stdout}\n{result.stderr}')
        else:
            print(f'PASS {relative}')
    print(f'\n{len(files) - len(failures)}/{len(files)} exercises passed.')
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
