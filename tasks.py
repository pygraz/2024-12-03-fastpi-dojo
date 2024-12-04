from functools import total_ordering

from pydantic import BaseModel
from datetime import date, timedelta
from enum import Enum


class TaskStatus(str, Enum):
    active = "active"
    completed = "completed"


class Category(str, Enum):
    hobby = "hobby"
    home = "home"
    shopping = "shopping"
    work = "work"


class NewTask(BaseModel):
    title: str
    category: Category = Category.home
    completed_on: date | None = None
    due_on: date | None = None


@total_ordering
class Task(BaseModel):
    id: int
    title: str
    category: Category = Category.home
    completed_on: date | None = None
    due_on: date | None = None

    def __hash__(self):
        # hash(custom_object)
        return self.id

    def __eq__(self, other):
        _check_is_task_comparison_operand(other)
        return self.id == other.id

    def __lt__(self, other):
        _check_is_task_comparison_operand(other)
        return self.id < other.id


def _check_is_task_comparison_operand(other):
    if not hasattr(other, "id"):
        return NotImplemented


class TaskRepository:
    def __init__(self):
        self._id_to_task_map = {}
        self._next_id = 1

    @staticmethod
    def new_demo() -> "TaskRepository":
        result = TaskRepository()
        result.add(title="Buy milk", category=Category.shopping)
        result.add(title="Water the flowers", category=Category.home)
        today = date.today()
        three_days_from_now = today + timedelta(days=3)
        result.add(
            title="Send monthly report to Alice",
            category=Category.work,
            due_on=three_days_from_now,
        )
        two_days_ago = today - timedelta(days=2)
        result.add(
            title="Interview Bob about senior dev job",
            category=Category.work,
            completed_on=two_days_ago,
            due_on=two_days_ago,
        )
        result.add(
            title="Buy bread",
            category=Category.shopping,
            completed_on=today,
            due_on=two_days_ago,
        )
        return result

    @property
    def count(self) -> int:
        return len(self._id_to_task_map)

    def add(
        self,
        *,
        title: str,
        category: Category = Category.home,
        completed_on: date | None = None,
        due_on: date | None = None,
    ) -> Task:
        result = Task(
            id=self._next_id,
            title=title,
            category=category,
            completed_on=completed_on,
            due_on=due_on,
        )
        self._id_to_task_map[self._next_id] = result
        self._next_id += 1
        return result

    def get(self, id: int) -> Task:
        return self._id_to_task_map[id]

    def list(self, filter: TaskStatus) -> list[Task]:
        return sorted(
            [
                task
                for task in self._id_to_task_map.values()
                if (filter == TaskStatus.completed and task.completed_on is not None)
                or (filter == TaskStatus.active and task.completed_on is None)
                or not filter
            ]
        )

    def remove(self, id: int) -> Task:
        return self._id_to_task_map.pop(id)
