from fastapi import FastAPI
from tasks import TaskRepository

demo_repo = TaskRepository.new_demo()

app = FastAPI()


@app.get("/tasks")
async def get_tasks():
    return demo_repo.list()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
