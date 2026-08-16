from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


# In-memory task storage
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False,
    },
    {
        "id": 2,
        "title": "Build CRUD API",
        "done": False,
    },
    {
        "id": 3,
        "title": "Push project to GitHub",
        "done": False,
    },
]


# Request models
class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


# Root endpoint
@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
    }


# Health check
@app.get("/health")
def health():
    return {"status": "ok"}


# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# Get a single task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found",
    )


# Create a new task
@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    new_id = max(task["id"] for task in tasks) + 1

    new_task = {
        "id": new_id,
        "title": task_data.title,
        "done": False,
    }

    tasks.append(new_task)

    return new_task


# Update an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:

            if task_data.title is not None:
                task["title"] = task_data.title

            if task_data.done is not None:
                task["done"] = task_data.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found",
    )


# Delete a task
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found",
    )