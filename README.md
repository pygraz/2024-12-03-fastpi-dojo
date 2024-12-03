# FastAPI dojo

This is the source code produced during the [PyGRAZ meetuo on 2024-12-03](https://pygraz.org/meetups/2024-12-03).

## Project set up

1. Install [poetry](https://python-poetry.org/).
2. Set uo the project by running:
   ```shell
   poetry install
   ```
3. Activate the [pre-commit](https://pre-commit.com/) hooks by running:
   ```shell
   poetry run pre-commit install
   ```

To start the local development server, run:

```shell
poetry run fastapi dev main.py
```

You can omit the `poetry run` if you start from a poetry shell:

```shell
poetry shell
fastapi dev main.py
```

## Testing

To run the test suite, run:

```shell
poetry run pytest
```

## Code quality

To ensure the source code matches the quality standards of the project, run the pre-commit:

```shell
poetry run pre-commit run
```

To also check historic files committed earlier, run:

```shell
poetry run pre-commit run --all-files
```

## PyCharm

If you open the project in PyCharm Professional, you can utilize the [PyCharm FastAPI integration](https://www.jetbrains.com/help/pycharm/fastapi-project.html).

## Links

- [FastAPI](https://fastapi.tiangolo.com/)
  - [Pydandic](https://docs.pydantic.dev/latest/)
  - [Introduction to pydantic](https://pygraz.org/meetups/sessions/280/) - Juypter notebook from PyGraz lightning talk

## Dojo

For the coding dojo, we are going to build upon an existing FastAPI server (see [#1](https://github.com/pygraz/2024-12-03-fastpi-dojo/issues/1)))that essentially matches the [first steps of the FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/first-steps/).

The server will be extended to be able to manage tasks. Tasks have the following properties (see [#3](https://github.com/pygraz/2024-12-03-fastpi-dojo/issues/3)):

- id: internal integer ID
- title: text
- description: text
- completed_on: date, optional
- due_on: date, optional
- category: enum of: hobby, home, shopping, work

Tasks are comparable and hashable, so they can be compared and stored in sets and dicts. The basis for comparison is the `id`. For the implementation, see `Task.__hash__()`, `__eq__`, `__lt__` and [functools.total_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering).

Tasks are collected in a `TaskRepository` that provides methods to:

- add
- get
- list
- remove

To make it easier we can create a demo task repository that already holds some data:

```python
from tasks import TaskRepository

demo_repo = TaskRepository.new_demo()
```
