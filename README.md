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
-
