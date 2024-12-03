from tasks import Task, Category, TaskRepository
from datetime import date


def test_can_create_task_with_defaults():
    task = Task(id=1, title="test")
    assert task.id == 1
    assert task.title == "test"
    assert task.category == Category.home
    assert task.completed_on is None
    assert task.due_on is None


def test_can_create_task_with_all_fields_set():
    expected_category = Category.shopping
    expected_completed_on = date(2024, 12, 3)
    expected_due_on = date(2024, 12, 5)
    task = Task(
        id=123,
        title="Buy butter",
        category=expected_category,
        completed_on=expected_completed_on,
        due_on=expected_due_on,
    )
    assert task.id == 123
    assert task.title == "Buy butter"
    assert task.completed_on == expected_completed_on
    assert task.due_on == expected_due_on


def test_can_crud_repository():
    repo = TaskRepository()
    task = repo.add(title="test")
    assert repo.count == 1
    assert repo.get(task.id) == task
    assert repo.list() == [task]
    assert repo.remove(task.id) == task
    assert repo.count == 0


def test_can_add_multiple_tasks():
    repo = TaskRepository()
    task1 = repo.add(title="test1")
    task2 = repo.add(title="test2")
    assert task1.id != task2.id
    assert repo.count == 2
    assert repo.list() == [task1, task2]


def test_can_create_demo_task_repository():
    demo_repo = TaskRepository.new_demo()
    assert demo_repo.count >= 1
