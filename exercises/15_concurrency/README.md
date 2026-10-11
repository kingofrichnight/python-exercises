# 15_concurrency

Work through these files in order.

- [Ordered thread-pool results](01_threads.py) — ThreadPoolExecutor, map, executor lifetime
- [Protect a shared counter](02_locks.py) — Lock, critical section, futures
- [Process-pool CPU tasks](03_processes.py) — ProcessPoolExecutor, pickle, main guard, spawn
- [Bound asynchronous work](04_asyncio.py) — async/await, Semaphore, gather, asyncio.run
- [Cancel sibling tasks on failure](05_taskgroup.py) — TaskGroup, ExceptionGroup, except*, cancellation
