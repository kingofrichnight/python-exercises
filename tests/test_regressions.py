"""Independent boundary and reference-oracle checks for selected exercises."""

import importlib.util
from itertools import product
from pathlib import Path
import random
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(slug):
    matches = list((ROOT / 'exercises').glob(f'*/*_{slug}.py'))
    if len(matches) != 1:
        raise RuntimeError(f'expected one exercise for {slug}: {matches}')
    name = f'exercise_{slug}'
    spec = importlib.util.spec_from_file_location(name, matches[0])
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class RegressionTests(unittest.TestCase):
    def test_binary_search_against_linear_oracle(self):
        search = load('binary_search').binary_search
        rng = random.Random(23)
        for _ in range(100):
            values = sorted(rng.randrange(-5, 6) for _ in range(rng.randrange(30)))
            for target in range(-6, 7):
                expected = values.index(target) if target in values else -1
                self.assertEqual(search(values, target), expected)

    def test_merge_sort_against_builtin(self):
        sort = load('merge_sort').merge_sort
        rng = random.Random(9)
        for length in range(50):
            values = [rng.randrange(-10, 11) for _ in range(length)]
            self.assertEqual(sort(values), sorted(values))

    def test_sliding_window_against_bruteforce(self):
        longest = load('sliding_window').longest_unique
        for length in range(6):
            for chars in product('abc', repeat=length):
                text = ''.join(chars)
                expected = max((end - start for start in range(len(text) + 1)
                                for end in range(start, len(text) + 1)
                                if len(set(text[start:end])) == end - start), default=0)
                self.assertEqual(longest(text), expected)

    def test_gcd_against_standard_library(self):
        from math import gcd
        implementation = load('gcd').gcd
        for a in range(-12, 13):
            for b in range(-12, 13):
                self.assertEqual(implementation(a, b), gcd(a, b))

    def test_retry_exhaustion_and_nontransient_failure(self):
        retry = load('retry').retry
        calls = []
        @retry(3)
        def always_fails():
            calls.append(1)
            raise TimeoutError('unavailable')
        with self.assertRaises(TimeoutError):
            always_fails()
        self.assertEqual(len(calls), 3)
        calls.clear()
        @retry(3)
        def permanent():
            calls.append(1)
            raise ValueError('bad request')
        with self.assertRaises(ValueError):
            permanent()
        self.assertEqual(len(calls), 1)

    def test_generator_cleanup_immediately_after_priming(self):
        mean = load('send').running_mean
        events = []
        generator = mean(events)
        next(generator)
        generator.close()
        self.assertEqual(events, ['closed'])

    def test_invalid_inputs(self):
        cases = [
            (load('time_breakdown').split_seconds, (-1,)),
            (load('leap_year').is_leap_year, (0,)),
            (load('bounded_history').recent, ([], 0)),
            (load('dynamic_programming').min_coins, ([0], 3)),
            (load('decimal').invoice, (['NaN'],)),
            (load('bank_account').Account, (True,)),
        ]
        for function, args in cases:
            with self.subTest(function=function.__name__):
                with self.assertRaises(ValueError):
                    function(*args)
        with self.assertRaises(ValueError):
            list(load('batches').batches([], 0))

    def test_atomic_write_failure_preserves_destination(self):
        from tempfile import TemporaryDirectory
        from unittest.mock import patch
        module = load('atomic_write')
        with TemporaryDirectory() as folder:
            path = Path(folder) / 'note.txt'
            path.write_text('original', encoding='utf-8')
            with patch.object(module.os, 'replace', side_effect=OSError('simulated')):
                with self.assertRaises(OSError):
                    module.replace_text(path, 'replacement')
            self.assertEqual(path.read_text(encoding='utf-8'), 'original')
            self.assertEqual(list(Path(folder).iterdir()), [path])

    def test_topological_order_constraints(self):
        order = load('dependency_scheduler').build_order
        graph = {'a': [], 'b': ['a'], 'c': ['a'], 'd': ['b', 'c']}
        result = order(graph)
        positions = {name: index for index, name in enumerate(result)}
        self.assertEqual(set(result), set(graph))
        for task, prerequisites in graph.items():
            for prerequisite in prerequisites:
                self.assertLess(positions[prerequisite], positions[task])

    def test_bfs_none_node_and_cycles(self):
        search = load('bfs').shortest_path
        self.assertEqual(search({None: ['a'], 'a': [None, 'b']}, None, 'b'), [None, 'a', 'b'])


if __name__ == '__main__':
    unittest.main()
