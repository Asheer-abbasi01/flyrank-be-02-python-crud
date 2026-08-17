from multiprocessing.dummy import connection
import os

import psycopg
from psycopg.rows import dict_row

def get_connection():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError("DATABASE_URL is not set")

    return psycopg.connect(database_url, row_factory=dict_row)

class PostgresRepository:

    def initialize_database(self):
        connection = get_connection()

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                done BOOLEAN NOT NULL DEFAULT FALSE
            )
            """
        )

        cursor = connection.execute(
            "SELECT COUNT(*) AS count FROM tasks"
        )

        task_count = cursor.fetchone()["count"]
        if task_count == 0:
            cur = connection.cursor()

            cur.executemany(
                """
                INSERT INTO tasks (title, done)
                VALUES (%s, %s)
                """,
                [
                    ("Learn FastAPI", False),
                    ("Connect PostgreSQL Database", False),
                    ("Push project to GitHub", False),
                ],
            )

            cur.close()

        connection.commit()
        connection.close()

    def get_all_tasks(self):
        connection = get_connection()

        cursor = connection.execute(
            """
            SELECT id, title, done
            FROM tasks
            ORDER BY id
            """
        )

        tasks = cursor.fetchall()

        connection.close()

        return tasks

    def get_task(self, task_id: int):
        connection = get_connection()

        cursor = connection.execute(
            """
            SELECT id, title, done
            FROM tasks
            WHERE id = %s
            """,
            (task_id,),
        )

        task = cursor.fetchone()

        connection.close()

        return task

    def create_task(self, title: str):
        connection = get_connection()

        cursor = connection.execute(
            """
            INSERT INTO tasks (title, done)
            VALUES (%s, %s)
            RETURNING id, title, done
            """,
            (title, False),
        )

        task = cursor.fetchone()

        connection.commit()
        connection.close()

        return task

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        done: bool | None = None,
    ):
        connection = get_connection()

        if title is not None:
            connection.execute(
                """
                UPDATE tasks
                SET title = %s
                WHERE id = %s
                """,
                (title, task_id),
            )

        if done is not None:
            connection.execute(
                """
                UPDATE tasks
                SET done = %s
                WHERE id = %s
                """,
                (done, task_id),
            )

        cursor = connection.execute(
            """
            SELECT id, title, done
            FROM tasks
            WHERE id = %s
            """,
            (task_id,),
        )

        task = cursor.fetchone()

        connection.commit()
        connection.close()

        return task

    def delete_task(self, task_id: int):
        connection = get_connection()

        cursor = connection.execute(
            """
            DELETE FROM tasks
            WHERE id = %s
            """,
            (task_id,),
        )

        deleted = cursor.rowcount

        connection.commit()
        connection.close()

        return deleted


repository = PostgresRepository()