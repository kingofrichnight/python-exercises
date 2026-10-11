# Exercise catalog

Follow the sections and exercises in this order.

## 01_basics

- [Personalized greeting](exercises/01_basics/01_greeting.py) — variables, str, f-strings, return
- [Temperature converter](exercises/01_basics/02_temperature.py) — arithmetic, floats, operator precedence
- [Break seconds into clock units](exercises/01_basics/03_time_breakdown.py) — integers, divmod, tuple unpacking
- [Parse a shopping quantity](exercises/01_basics/04_parse_input.py) — input conversion, int, exceptions, print
- [Copies, equality, and identity](exercises/01_basics/05_identity.py) — is, ==, mutable objects, shallow and deep copy

## 02_control_flow

- [Leap year classifier](exercises/02_control_flow/01_leap_year.py) — if, booleans, modulo, and/or
- [FizzBuzz sequence](exercises/02_control_flow/02_fizzbuzz.py) — for, range, if/elif/else, lists
- [Euclidean greatest common divisor](exercises/02_control_flow/03_gcd.py) — while, simultaneous assignment, abs
- [Prime number checker](exercises/02_control_flow/04_prime.py) — for/else, break, square-root bound
- [Dispatch structured commands](exercises/02_control_flow/05_commands.py) — match/case, guards, destructuring

## 03_strings

- [Normalized palindrome](exercises/03_strings/01_palindrome.py) — casefold, isalnum, slicing, comprehension
- [Word frequency table](exercises/03_strings/02_word_counts.py) — split, strip, dict.get, punctuation
- [Run-length encoding](exercises/03_strings/03_run_length.py) — iteration, state, tuples, join
- [Group anagrams](exercises/03_strings/04_anagrams.py) — sorted, defaultdict, canonical keys
- [Unicode and byte boundaries](exercises/03_strings/05_unicode.py) — unicodedata, encode, decode, NFC

## 04_collections

- [Deduplicate while preserving order](exercises/04_collections/01_deduplicate.py) — sets, lists, membership, hashability
- [Transpose a rectangular matrix](exercises/04_collections/02_matrix.py) — nested lists, zip, unpacking, any
- [Inventory reconciliation](exercises/04_collections/03_inventory.py) — dict union, sets, comprehensions, sorting
- [Stable leaderboard ranking](exercises/04_collections/04_ranking.py) — sorted, lambda, enumerate, tuple keys
- [Bounded event history](exercises/04_collections/05_bounded_history.py) — deque, maxlen, collections

## 05_functions

- [Build a configurable receipt](exercises/05_functions/01_arguments.py) — defaults, keyword-only parameters, round
- [Merge named settings](exercises/05_functions/02_variadic.py) — *args, **kwargs, unpacking, dict.update
- [Avoid shared mutable defaults](exercises/05_functions/03_safe_defaults.py) — None sentinel, mutation, default arguments
- [Independent running counters](exercises/05_functions/04_closure.py) — closures, nonlocal, lexical scope
- [Flatten nested lists](exercises/05_functions/05_recursion.py) — recursion, isinstance, base case

## 06_modules_errors

- [Import and inspect a module](exercises/06_modules_errors/01_modules.py) — importlib, modules, namespaces, main guard
- [Validate a configuration value](exercises/06_modules_errors/02_custom_error.py) — custom exceptions, chaining, try/except
- [Cleanup even after failure](exercises/06_modules_errors/03_cleanup.py) — try/except/else/finally, resources
- [Command-line unit converter](exercises/06_modules_errors/04_cli.py) — argparse, CLI, choices, optional arguments

## 07_files_data

- [Summarize a UTF-8 text file](exercises/07_files_data/01_text_files.py) — pathlib, with, encoding, streaming
- [Validate JSON settings](exercises/07_files_data/02_json.py) — json, serialization, schema validation
- [Aggregate CSV sales](exercises/07_files_data/03_csv.py) — csv.DictReader, StringIO, Decimal
- [Replace a file after a successful write](exercises/07_files_data/04_atomic_write.py) — tempfile, os.replace, finally, pathlib
- [Parameterized SQLite queries](exercises/07_files_data/05_sqlite.py) — sqlite3, SQL, transactions, contextlib.closing

## 08_oop

- [Encapsulated account balance](exercises/08_oop/01_bank_account.py) — classes, __init__, properties, methods
- [Immutable inventory records](exercises/08_oop/02_dataclasses.py) — dataclass, frozen, slots, __post_init__
- [Shape interface](exercises/08_oop/03_polymorphism.py) — ABC, abstractmethod, inheritance, polymorphism
- [Two-dimensional vectors](exercises/08_oop/04_dunder.py) — operator overloading, NotImplemented, __iter__
- [Notification service with injected delivery](exercises/08_oop/05_composition.py) — composition, dependency injection, duck typing

## 09_iterators_generators

- [Custom countdown iterator](exercises/09_iterators_generators/01_iterator.py) — __iter__, __next__, StopIteration
- [Lazy batches](exercises/09_iterators_generators/02_batches.py) — yield, iter, islice, bounded memory
- [Streaming log pipeline](exercises/09_iterators_generators/03_pipeline.py) — generator expressions, yield from, lazy composition
- [Running mean coroutine](exercises/09_iterators_generators/04_send.py) — generator.send, priming, finally, close

## 10_decorators_context

- [Count function calls](exercises/10_decorators_context/01_decorator.py) — decorators, functools.wraps, function attributes
- [Bounded retries for transient failures](exercises/10_decorators_context/02_retry.py) — decorator factories, exception tuples, reraise
- [Temporarily override a dictionary value](exercises/10_decorators_context/03_context_manager.py) — contextmanager, sentinel, try/finally
- [Memoized Fibonacci](exercises/10_decorators_context/04_cache.py) — lru_cache, recursion, cache_info

## 11_typing_internals

- [Typed first-match search](exercises/11_typing_internals/01_generics.py) — TypeVar, Iterable, Callable, union types
- [Structural typing for output sinks](exercises/11_typing_internals/02_protocol.py) — Protocol, structural subtyping, annotations
- [Reusable positive-number descriptor](exercises/11_typing_internals/03_descriptor.py) — descriptors, __set_name__, __get__, __set__
- [Register classes at definition time](exercises/11_typing_internals/04_metaclass.py) — type, metaclasses, class creation

## 12_standard_library

- [Permission flags with bit masks](exercises/12_standard_library/01_flags.py) — IntFlag, enums, bitwise operators
- [Encode a binary record](exercises/12_standard_library/02_binary_records.py) — struct, bytes, endianness, hashlib
- [Parse structured log lines](exercises/12_standard_library/03_regex.py) — re, named groups, fullmatch
- [Compare timezone-aware timestamps](exercises/12_standard_library/04_datetime.py) — datetime, timezone, ISO 8601, timedelta
- [Exact invoice arithmetic](exercises/12_standard_library/05_decimal.py) — Decimal, quantize, ROUND_HALF_UP, finite values
- [Find exact-size combinations](exercises/12_standard_library/06_itertools.py) — combinations, itertools, generator expressions
- [Stable priority queue](exercises/12_standard_library/07_heap.py) — heapq, itertools.count, tuple ordering
- [Reproducible simulation](exercises/12_standard_library/08_random_statistics.py) — random.Random, statistics, local RNG state

## 13_algorithms

- [Find the first matching index](exercises/13_algorithms/01_binary_search.py) — binary search, invariants, logarithmic search
- [Stable merge sort](exercises/13_algorithms/02_merge_sort.py) — divide and conquer, recursion, stability
- [Shortest path in an unweighted graph](exercises/13_algorithms/03_bfs.py) — BFS, deque, graph traversal, parent map
- [Minimum coin count](exercises/13_algorithms/04_dynamic_programming.py) — dynamic programming, unreachable states
- [Longest substring without repetition](exercises/13_algorithms/05_sliding_window.py) — sliding window, dictionaries, linear time
- [Generate balanced parentheses](exercises/13_algorithms/06_backtracking.py) — backtracking, pruning, recursion

## 14_testing_debugging

- [Test a bounded clamp function](exercises/14_testing_debugging/01_unittest.py) — unittest, subTest, assertRaises, boundaries
- [Test an HTTP client without network access](exercises/14_testing_debugging/02_mocking.py) — Mock, dependency injection, HTTP status, JSON
- [Capture structured diagnostic messages](exercises/14_testing_debugging/03_logging.py) — logging, handlers, formatting, cleanup
- [Measure implementations without brittle thresholds](exercises/14_testing_debugging/04_profiling.py) — timeit, performance, equivalent behavior

## 15_concurrency

- [Ordered thread-pool results](exercises/15_concurrency/01_threads.py) — ThreadPoolExecutor, map, executor lifetime
- [Protect a shared counter](exercises/15_concurrency/02_locks.py) — Lock, critical section, futures
- [Process-pool CPU tasks](exercises/15_concurrency/03_processes.py) — ProcessPoolExecutor, pickle, main guard, spawn
- [Bound asynchronous work](exercises/15_concurrency/04_asyncio.py) — async/await, Semaphore, gather, asyncio.run
- [Cancel sibling tasks on failure](exercises/15_concurrency/05_taskgroup.py) — TaskGroup, ExceptionGroup, except*, cancellation

## 16_projects

- [Project: persistent task tracker](exercises/16_projects/01_task_tracker.py) — dataclasses, JSON, pathlib, validation, state
- [Project: monthly expense report](exercises/16_projects/02_expense_report.py) — CSV, Decimal, date parsing, aggregation
- [Project: streaming status-code report](exercises/16_projects/03_log_analyzer.py) — streaming, Counter, parsing, malformed records
- [Project: bounded LRU cache](exercises/16_projects/04_lru_cache.py) — OrderedDict, eviction, sentinel-free lookup, classes
- [Project: restricted arithmetic evaluator](exercises/16_projects/05_expression_evaluator.py) — ast, recursion, allowlists, operators
- [Project: dependency-aware build ordering](exercises/16_projects/06_dependency_scheduler.py) — topological sort, graph validation, heap, cycles
