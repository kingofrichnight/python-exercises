"""Project: persistent task tracker

Concepts: dataclasses, JSON, pathlib, validation, state
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Build a TaskBoard supporting add(title), complete(id), save(path), and
load(path). IDs start at 1 and increase; blank titles and unknown IDs are
errors. Persist tasks as JSON and validate loaded types and duplicate IDs.
Saving overwrites only the supplied file; checks use a temporary directory.

HINT
Validate the full document before returning a loaded board.

STRETCH
Add argparse subcommands, deletion, and atomic saving.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

import json
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class Task:
    id: int
    title: str
    done: bool = False

class TaskBoard:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError('title is required')
        task = Task(max((task.id for task in self.tasks), default=0) + 1, title.strip())
        self.tasks.append(task)
        return task.id

    def complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                return
        raise KeyError(task_id)

    def save(self, path):
        Path(path).write_text(json.dumps([asdict(task) for task in self.tasks], indent=2), encoding='utf-8')

    @classmethod
    def load(cls, path):
        data = json.loads(Path(path).read_text(encoding='utf-8'))
        if not isinstance(data, list):
            raise ValueError('expected task list')
        board, seen = cls(), set()
        for row in data:
            if not isinstance(row, dict) or set(row) != {'id', 'title', 'done'}:
                raise ValueError('invalid task fields')
            if type(row['id']) is not int or row['id'] <= 0 or row['id'] in seen:
                raise ValueError('invalid or duplicate id')
            if not isinstance(row['title'], str) or not row['title'].strip() or type(row['done']) is not bool:
                raise ValueError('invalid task values')
            seen.add(row['id'])
            board.tasks.append(Task(**row))
        return board


def check():
    from tempfile import TemporaryDirectory
    board = TaskBoard()
    first = board.add(' Learn Python ')
    assert first == 1
    board.complete(first)
    with TemporaryDirectory() as folder:
        path = Path(folder) / 'tasks.json'
        board.save(path)
        restored = TaskBoard.load(path)
        assert restored.tasks == [Task(1, 'Learn Python', True)]
        assert restored.add('Practice') == 2
        path.write_text('[{"id":1,"title":"a","done":"false"}]', encoding='utf-8')
        try:
            TaskBoard.load(path)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid schema accepted')


if __name__ == "__main__":
    check()
    print("PASS: Project: persistent task tracker")
