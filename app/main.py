from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.database import get_connection, initialize_database

app = FastAPI(
    title="Task API",
    version="2.0",
    description="FastAPI CRUD API with SQLite database",
)


# Initialize the database when the application starts
initialize_database()


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
        "version": "2.0",
        "database": "SQLite",
        "endpoints": ["/tasks"],
    }


# Health check
@app.get("/health")
def health():
    return {"status": "ok"}


# Get all tasks
@app.get("/tasks")
def get_tasks():
    connection = get_connection()

    cursor = connection.execute(
        """
        SELECT id, title, done
        FROM tasks
        ORDER BY id
        """
    )

    tasks = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return tasks


# Get a single task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    connection = get_connection()

    cursor = connection.execute(
        """
        SELECT id, title, done
        FROM tasks
        WHERE id = ?
        """,
        (task_id,),
    )

    task = cursor.fetchone()

    connection.close()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found",
        )

    return dict(task)


# Create a new task
@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tasks (title, done)
        VALUES (?, ?)
        """,
        (task_data.title, False),
    )

    connection.commit()

    task_id = cursor.lastrowid

    cursor = connection.execute(
        """
        SELECT id, title, done
        FROM tasks
        WHERE id = ?
        """,
        (task_id,),
    )

    task = cursor.fetchone()

    connection.close()

    return dict(task)


# Update an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    connection = get_connection()

    cursor = connection.execute(
        """
        SELECT id, title, done
        FROM tasks
        WHERE id = ?
        """,
        (task_id,),
    )

    task = cursor.fetchone()

    if task is None:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found",
        )

    if task_data.title is not None:
        connection.execute(
            """
            UPDATE tasks
            SET title = ?
            WHERE id = ?
            """,
            (task_data.title, task_id),
        )

    if task_data.done is not None:
        connection.execute(
            """
            UPDATE tasks
            SET done = ?
            WHERE id = ?
            """,
            (task_data.done, task_id),
        )

    connection.commit()

    cursor = connection.execute(
        """
        SELECT id, title, done
        FROM tasks
        WHERE id = ?
        """,
        (task_id,),
    )

    updated_task = cursor.fetchone()

    connection.close()

    return dict(updated_task)


# Delete a task
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    connection = get_connection()

    cursor = connection.execute(
        """
        DELETE FROM tasks
        WHERE id = ?
        """,
        (task_id,),
    )

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found",
        )

    return