from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.repositories.postgres_repository import repository


app = FastAPI(
    title="Task API",
    version="3.0",
    description="FastAPI CRUD API with PostgreSQL database",
)


# Initialize the database when the application starts
@app.on_event("startup")
def startup():
    repository.initialize_database()


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
        "version": "3.0",
        "database": "PostgreSQL",
        "endpoints": ["/tasks"],
    }

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return repository.get_all_tasks()


# Get a single task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = repository.get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found",
        )

    return task


# Create a new task
@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    return repository.create_task(task_data.title)


# Update an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):

    existing_task = repository.get_task(task_id)

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found",
        )

    updated_task = repository.update_task(
        task_id=task_id,
        title=task_data.title,
        done=task_data.done,
    )

    return updated_task


# Delete a task
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    deleted = repository.delete_task(task_id)

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found",
        )

    return