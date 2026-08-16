import sqlite3


DATABASE_NAME = "tasks.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
        """
    )

    cursor = connection.execute("SELECT COUNT(*) FROM tasks")
    task_count = cursor.fetchone()[0]

    if task_count == 0:
        connection.executemany(
            """
            INSERT INTO tasks (title, done)
            VALUES (?, ?)
            """,
            [
                ("Learn FastAPI", False),
                ("Connect SQLite Database", False),
                ("Push project to GitHub", False),
            ],
        )

    connection.commit()
    connection.close()