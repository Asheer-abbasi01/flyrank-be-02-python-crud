# 🚀 Tasks API

A simple and production-style **RESTful CRUD API** built with **Python, FastAPI, and SQLite**.

This project implements a complete task management API with persistent database storage, input validation, proper HTTP status codes, and interactive API documentation using FastAPI's built-in Swagger UI.

The project was developed as part of the **FlyRank Backend AI Engineering Internship – Week 3 (BE-02)** and demonstrates the complete backend workflow from API design to persistent database operations.

---

## ✨ Features

* ✅ Create a new task
* ✅ Retrieve all tasks
* ✅ Retrieve a task by ID
* ✅ Update an existing task
* ✅ Delete a task
* ✅ Persistent data storage using SQLite
* ✅ Automatic database creation
* ✅ Automatic table creation
* ✅ Automatic insertion of sample tasks on first run
* ✅ Request validation using Pydantic
* ✅ Proper RESTful API design
* ✅ Appropriate HTTP status codes
* ✅ Interactive Swagger UI documentation
* ✅ ReDoc API documentation
* ✅ Clean project structure
* ✅ Database persists data across server restarts

---

## 🛠️ Tech Stack

| Technology   | Purpose                                 |
| ------------ | --------------------------------------- |
| **Python**   | Backend programming language            |
| **FastAPI**  | Web framework for building the REST API |
| **SQLite**   | Persistent relational database          |
| **Pydantic** | Request validation and data schemas     |
| **Uvicorn**  | ASGI server                             |
| **SQL**      | Database queries                        |

---

## 📂 Project Structure

```text
task-api/
│
├── database/
│   ├── database.py
│   └── tasks.db
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File / Directory       | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| `main.py`              | Main FastAPI application and API endpoints              |
| `database/database.py` | SQLite database connection, initialization, and queries |
| `database/tasks.db`    | SQLite database file containing persistent task data    |
| `requirements.txt`     | Python project dependencies                             |
| `.gitignore`           | Files and directories excluded from Git                 |
| `README.md`            | Project documentation                                   |

> **Note:** The exact structure may vary slightly depending on your implementation.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Asheer-abbasi01/task-api.git
```

## 2. Navigate to the Project Directory

```bash
cd task-api
```

## 3. Create a Virtual Environment

It is recommended to use a virtual environment to keep project dependencies isolated.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If you haven't created `requirements.txt` yet:

```bash
pip install fastapi uvicorn
```

Then generate it with:

```bash
pip freeze > requirements.txt
```

---

# ▶️ Running the Application

Start the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

or:

```text
http://localhost:8000
```

The `--reload` option automatically restarts the server whenever you make changes to the source code.

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://localhost:8000/docs
```

Swagger UI allows you to:

* View all available endpoints
* Inspect request and response schemas
* Send API requests directly from the browser
* Test CRUD operations
* View validation requirements
* Inspect HTTP responses and status codes

## ReDoc

FastAPI also provides an alternative documentation interface:

```text
http://localhost:8000/redoc
```

---

# 🔗 API Endpoints

| Method   | Endpoint      | Description             |
| -------- | ------------- | ----------------------- |
| `GET`    | `/`           | Returns API information |
| `GET`    | `/tasks`      | Get all tasks           |
| `GET`    | `/tasks/{id}` | Get a task by ID        |
| `POST`   | `/tasks`      | Create a new task       |
| `PUT`    | `/tasks/{id}` | Update an existing task |
| `DELETE` | `/tasks/{id}` | Delete a task           |

---

# 📝 API Usage

## 1. Get API Information

### Request

```http
GET /
```

### Example Response

```json
{
  "message": "Tasks API is running"
}
```

---

## 2. Get All Tasks

### Request

```http
GET /tasks
```

### Example Response

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "done": 0
  },
  {
    "id": 2,
    "title": "Build REST API",
    "done": 0
  },
  {
    "id": 3,
    "title": "Learn SQLite",
    "done": 1
  }
]
```

---

## 3. Get a Task by ID

### Request

```http
GET /tasks/1
```

### Example Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": 0
}
```

If the requested task does not exist, the API returns:

```json
{
  "detail": "Task not found"
}
```

with HTTP status:

```text
404 Not Found
```

---

# ➕ Create a Task

### Request

```http
POST /tasks
```

### Request Body

```json
{
  "title": "Learn SQLite"
}
```

### Example Response

```json
{
  "message": "Task created successfully",
  "task": {
    "id": 4,
    "title": "Learn SQLite",
    "done": 0
  }
}
```

### Status Code

```text
201 Created
```

---

# ✏️ Update a Task

### Request

```http
PUT /tasks/4
```

### Request Body

```json
{
  "title": "Master SQLite",
  "done": 1
}
```

### Example Response

```json
{
  "message": "Task updated successfully",
  "task": {
    "id": 4,
    "title": "Master SQLite",
    "done": 1
  }
}
```

### Status Code

```text
200 OK
```

---

# 🗑️ Delete a Task

### Request

```http
DELETE /tasks/4
```

### Example Response

```json
{
  "message": "Task deleted successfully"
}
```

### Status Code

```text
200 OK
```

If the task does not exist:

```text
404 Not Found
```

---

# 📌 HTTP Status Codes

| Status Code                 | Meaning                        |
| --------------------------- | ------------------------------ |
| `200 OK`                    | Request completed successfully |
| `201 Created`               | New task successfully created  |
| `400 Bad Request`           | Invalid request data           |
| `404 Not Found`             | Requested task does not exist  |
| `422 Unprocessable Entity`  | FastAPI validation error       |
| `500 Internal Server Error` | Unexpected server-side error   |

> FastAPI automatically handles many request validation errors and returns `422 Unprocessable Entity` when incoming data does not match the defined Pydantic schema.

---

# 🗄️ SQLite Database

This project uses **SQLite** as its persistent database.

SQLite was selected because it is:

* Lightweight
* Serverless
* Easy to configure
* Suitable for small backend applications
* File-based
* Easy to develop and test locally

No separate database server is required.

---

## Database Initialization

When the application starts:

1. The SQLite database is created if it does not already exist.
2. The `tasks` table is created if it does not already exist.
3. Sample tasks are inserted only when the table is empty.
4. Existing task data is preserved.
5. All CRUD operations interact directly with the SQLite database.

### Database Location

```text
database/tasks.db
```

The database file allows task data to persist even after the FastAPI server is stopped or restarted.

---

# 🧱 Database Schema

The `tasks` table contains the following fields:

| Column  | Type    | Description                         |
| ------- | ------- | ----------------------------------- |
| `id`    | INTEGER | Unique task identifier              |
| `title` | TEXT    | Task title                          |
| `done`  | INTEGER | Task completion status (`0` or `1`) |

Example:

```text
id | title              | done
---|--------------------|-----
1  | Learn FastAPI      | 0
2  | Build REST API     | 0
3  | Learn SQLite       | 1
```

---

# 🔍 SQL Queries

The application uses SQL queries to perform database operations.

## Retrieve All Tasks

```sql
SELECT * FROM tasks;
```

## Retrieve a Task by ID

```sql
SELECT * FROM tasks
WHERE id = ?;
```

## Create a Task

```sql
INSERT INTO tasks (title, done)
VALUES (?, 0);
```

## Update a Task

```sql
UPDATE tasks
SET title = ?, done = ?
WHERE id = ?;
```

## Delete a Task

```sql
DELETE FROM tasks
WHERE id = ?;
```

## Show Completed Tasks

```sql
SELECT * FROM tasks
WHERE done = 1;
```

## Count All Tasks

```sql
SELECT COUNT(*) FROM tasks;
```

## Mark Every Task as Completed

```sql
UPDATE tasks
SET done = 1;
```

## Delete All Completed Tasks

```sql
DELETE FROM tasks
WHERE done = 1;
```

---

# 🧪 Testing the API

The API can be tested using several tools.

### Swagger UI

```text
http://localhost:8000/docs
```

### cURL

Example:

```bash
curl -X POST "http://localhost:8000/tasks" \
-H "Content-Type: application/json" \
-d "{\"title\":\"Learn FastAPI\"}"
```

### Browser

GET endpoints can also be tested directly from a browser:

```text
http://localhost:8000/tasks
```

### API Clients

The API can also be tested using tools such as:

* Postman
* Insomnia
* Thunder Client
* Swagger UI

---

# 🔄 CRUD Workflow

The application follows the standard CRUD architecture:

```text
             ┌──────────────┐
             │    Client    │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │   FastAPI    │
             │ REST Routes  │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │   Database   │
             │    Layer     │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │    SQLite    │
             │  tasks.db    │
             └──────────────┘
```

### CRUD Operations

```text
CREATE  → POST   /tasks
READ    → GET    /tasks
READ    → GET    /tasks/{id}
UPDATE  → PUT    /tasks/{id}
DELETE  → DELETE /tasks/{id}
```

---

# 🛡️ Validation

Request data is validated using **Pydantic**, which is integrated into FastAPI.

For example, creating a task requires a valid task title:

```json
{
  "title": "Learn FastAPI"
}
```

Invalid request data is automatically rejected by FastAPI with an appropriate validation response.

---

# 📸 Screenshots

## Swagger UI

Add a screenshot of the interactive API documentation to:

```text
assets/swagger.png
```

Then include it here:

![Swagger UI](assets/swagger.png)

---

## SQLite Database

Open `tasks.db` using **DB Browser for SQLite**, take a screenshot of the database and save it as:

```text
assets/sqlite-db.png
```

Then include it here:

![SQLite Database](assets/sqlite-db.png)

---

# 📦 Dependencies

The main dependencies used in this project are:

```text
fastapi
uvicorn
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

# 🚀 Future Improvements

Possible improvements for future versions include:

* 🔐 JWT authentication
* 👤 User accounts
* 🗃️ PostgreSQL/MySQL support
* 🔎 Task search and filtering
* 📄 Pagination
* 🏷️ Task categories and tags
* 📅 Due dates
* ⚡ Async database operations
* 🧪 Automated unit and integration tests
* 🐳 Docker support
* ☁️ Cloud deployment
* 🔄 CI/CD pipeline
* 📊 API monitoring and logging

---

# 🎯 Learning Outcomes

Through this project, the following backend development concepts were practiced:

* REST API development
* FastAPI application structure
* HTTP methods and status codes
* CRUD operations
* SQLite database integration
* SQL queries
* Pydantic data validation
* API documentation with Swagger/OpenAPI
* Uvicorn ASGI server
* Persistent data storage
* Backend project organization
* API testing

---

# 👨‍💻 Author

**Asheer Hadayat**

BS Computer Science
COMSATS University Islamabad

* GitHub: [Asheer-abbasi01](https://github.com/Asheer-abbasi01)
* LinkedIn: [Asheer Hadayat](https://www.linkedin.com/in/hashir-abbasi-01a27a302)

---

# 📄 License

This project was created for **educational purposes** as part of the **FlyRank Backend AI Engineering Internship – Week 3 (BE-02)**.

You are free to use and modify the project for learning and educational purposes.

---

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub!
