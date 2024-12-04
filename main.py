from fastapi import FastAPI
from tasks import TaskRepository, NewTask

demo_repo = TaskRepository.new_demo()

app = FastAPI()


@app.get("/tasks")
async def get_tasks():
    return demo_repo.list()


@app.post("/tasks")
async def add_task(new_task: NewTask):
    return demo_repo.add(
        title=new_task.title,
        category=new_task.category,
        completed_on=new_task.completed_on,
        due_on=new_task.due_on,
    )


@app.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int):
    return demo_repo.get(task_id)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
