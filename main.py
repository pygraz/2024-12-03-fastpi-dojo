from click import Parameter
from fastapi import FastAPI
from tasks import TaskRepository

demo_repo = TaskRepository.new_demo()

app = FastAPI()


@app.get("/tasks")
async def get_tasks():
    return demo_repo.list()


@app.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int):
    return demo_repo.get(task_id)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
