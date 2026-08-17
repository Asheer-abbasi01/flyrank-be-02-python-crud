# 🚀 Task API — FastAPI + PostgreSQL + Docker

A production-oriented **RESTful CRUD API** built with **Python, FastAPI, PostgreSQL, and Docker**.

This project provides a complete task management API with persistent PostgreSQL storage, request validation, proper HTTP status codes, automatic database initialization, seed data, interactive API documentation, and containerized development using Docker Compose.

The project was developed as part of the **FlyRank AI Backend AI Engineering Internship — Week 3 (BE-02)** and demonstrates the transition from a basic CRUD API to a database-backed, containerized backend application.

---

## ✨ Features

- ✅ RESTful CRUD API for tasks
- ✅ Create, read, update, and delete tasks
- ✅ FastAPI backend
- ✅ PostgreSQL relational database
- ✅ Psycopg 3 PostgreSQL driver
- ✅ Pydantic request validation
- ✅ Repository pattern for database operations
- ✅ Automatic database initialization
- ✅ Automatic `tasks` table creation
- ✅ Automatic seed data on first startup
- ✅ Environment-based database configuration
- ✅ Dockerized FastAPI application
- ✅ Docker Compose for multi-container orchestration
- ✅ PostgreSQL persistent named volume
- ✅ PostgreSQL health check
- ✅ Interactive Swagger UI documentation
- ✅ ReDoc API documentation
- ✅ Proper RESTful HTTP status codes
- ✅ Clean and modular project structure
- ✅ Data persistence across container recreation

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.12** | Backend programming language |
| **FastAPI** | REST API framework |
| **Uvicorn** | ASGI application server |
| **PostgreSQL 16** | Relational database |
| **Psycopg 3** | PostgreSQL database driver |
| **Pydantic** | Request and response validation |
| **python-dotenv** | Environment variable management |
| **Docker** | Application containerization |
| **Docker Compose** | Multi-container orchestration |
| **Git & GitHub** | Version control |

---

# 📂 Project Structure

```text
flyrank-be-02-python-crud/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── models/
│   │   └── task.py
│   │
│   ├── repositories/
│   │   └── postgres_repository.py
│   │
│   └── routes/
│       └── tasks.py
│
├── .env
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## File Description

| File / Directory | Description |
|---|---|
| `app/main.py` | Creates and configures the FastAPI application |
| `app/models/task.py` | Defines task-related data models and validation schemas |
| `app/routes/tasks.py` | Contains task API endpoints |
| `app/repositories/postgres_repository.py` | Handles PostgreSQL connections, initialization, and CRUD database operations |
| `.env` | Stores local environment variables and database configuration |
| `.gitignore` | Specifies files excluded from Git |
| `.dockerignore` | Specifies files excluded from the Docker build context |
| `Dockerfile` | Defines the FastAPI application Docker image |
| `docker-compose.yml` | Defines and orchestrates the FastAPI and PostgreSQL services |
| `requirements.txt` | Lists Python dependencies |
| `README.md` | Project documentation |

> ⚠️ **Important:** Never commit `.env` to GitHub because it may contain database credentials.

---

# 🏗️ Application Architecture

The application consists of two main Docker services:

```text
                 ┌──────────────────────┐
                 │       Client         │
                 │ Browser / Postman    │
                 │ Swagger / cURL       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      FastAPI App     │
                 │      Port: 8000      │
                 └──────────┬───────────┘
                            │
                     DATABASE_URL
                            │
                            ▼
                 ┌──────────────────────┐
                 │    PostgreSQL 16     │
                 │      Port: 5432      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   postgres_data      │
                 │    Docker Volume     │
                 └──────────────────────┘
```

Docker Compose creates a shared Docker network so that the FastAPI application can communicate with PostgreSQL using the database service name.

Inside Docker, the application connects to PostgreSQL using:

```text
postgresql://postgres:postgres@db:5432/taskdb
```

Here, `db` is the PostgreSQL service name defined in Docker Compose.

---

# ⚙️ Prerequisites

Before running the project, make sure you have installed:

- **Python 3.12+**
- **Docker Desktop**
- **Git**

Verify Docker:

```bash
docker --version
```

Verify Docker Compose:

```bash
docker compose version
```

Verify Python:

```bash
python --version
```

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Asheer-abbasi01/task-api.git
```

Navigate into the project:

```bash
cd task-api
```

> If your GitHub repository uses a different repository name, replace `task-api` with the actual repository name.

---

# 🔐 Environment Configuration

Create a `.env` file in the project root:

```env
POSTGRES_DB=taskdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DATABASE_URL=postgresql://postgres:postgres@db:5432/taskdb
```

### Environment Variables

| Variable | Description |
|---|---|
| `POSTGRES_DB` | PostgreSQL database name |
| `POSTGRES_USER` | PostgreSQL username |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `DATABASE_URL` | Connection URL used by FastAPI |

### ⚠️ Security

Do **not** commit `.env` to GitHub.

Your `.gitignore` should include:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

For production systems, use secure secrets management instead of storing credentials directly in files.

---

# 📦 Python Dependencies

The project uses the following main dependencies:

```text
fastapi==0.128.0
uvicorn[standard]==0.40.0
pydantic==2.12.5
psycopg[binary]==3.3.4
python-dotenv==1.2.1
```

Install them manually for local development with:

```bash
pip install -r requirements.txt
```

---

# 🐳 Running the Application with Docker

Docker Compose is the recommended way to run the complete application because it starts both FastAPI and PostgreSQL.

## 1. Make Sure Docker Desktop Is Running

Start **Docker Desktop** and wait until Docker reports that it is running.

Verify:

```bash
docker info
```

If Docker is working correctly, Docker Engine information will be displayed.

---

## 2. Build the Docker Images

Run:

```bash
docker compose build
```

For a completely fresh build without using the Docker cache:

```bash
docker compose build --no-cache
```

---

## 3. Start the Application

Run:

```bash
docker compose up -d
```

The `-d` option runs the containers in detached mode.

Docker Compose starts:

```text
FastAPI Application
        +
PostgreSQL Database
```

---

## 4. Check Container Status

Run:

```bash
docker compose ps
```

You should see both services running.

Example:

```text
NAME            SERVICE   STATUS
task-api-app    app       Up
task-api-db     db        Up (healthy)
```

The exact container names may vary depending on the Docker Compose project name.

---

# 📋 Viewing Logs

## Application Logs

```bash
docker compose logs app
```

Follow application logs in real time:

```bash
docker compose logs -f app
```

## PostgreSQL Logs

```bash
docker compose logs db
```

Follow PostgreSQL logs:

```bash
docker compose logs -f db
```

---

# 🌐 Access the API

Once the containers are running, the API is available at:

```text
http://localhost:8000
```

You can verify the root endpoint:

```text
http://localhost:8000/
```

---

# 📖 API Documentation

FastAPI automatically generates OpenAPI documentation.

## Swagger UI

Open:

```text
http://localhost:8000/docs
```

Swagger UI allows you to:

- View all API endpoints
- Inspect request schemas
- Inspect response schemas
- Execute API requests
- Test CRUD operations
- View HTTP status codes
- Test validation behavior

## ReDoc

Alternative API documentation:

```text
http://localhost:8000/redoc
```

---

# 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Check API status |
| `GET` | `/tasks` | Get all tasks |
| `GET` | `/tasks/{task_id}` | Get a task by ID |
| `POST` | `/tasks` | Create a task |
| `PUT` | `/tasks/{task_id}` | Update a task |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

---

# 🔄 CRUD Operations

The API follows the standard CRUD pattern:

```text
CREATE  → POST   /tasks
READ    → GET    /tasks
READ    → GET    /tasks/{task_id}
UPDATE  → PUT    /tasks/{task_id}
DELETE  → DELETE /tasks/{task_id}
```

---

# 📝 API Usage

## 1. Check API Status

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

# 📋 2. Get All Tasks

### Request

```http
GET /tasks
```

### cURL

```bash
curl http://localhost:8000/tasks
```

### Example Response

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "done": false
  },
  {
    "id": 2,
    "title": "Connect PostgreSQL Database",
    "done": false
  },
  {
    "id": 3,
    "title": "Push project to GitHub",
    "done": false
  }
]
```

---

# 🔍 3. Get a Single Task

### Request

```http
GET /tasks/{task_id}
```

Example:

```http
GET /tasks/1
```

### Example Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

If the task does not exist, the API returns a `404 Not Found` response.

Example:

```json
{
  "detail": "Task not found"
}
```

---

# ➕ 4. Create a Task

### Request

```http
POST /tasks
```

### Request Body

```json
{
  "title": "Learn Docker"
}
```

### Example Response

```json
{
  "id": 4,
  "title": "Learn Docker",
  "done": false
}
```

### Expected Status

```text
201 Created
```

---

# ✏️ 5. Update a Task

### Request

```http
PUT /tasks/{task_id}
```

Example:

```http
PUT /tasks/1
```

### Request Body

```json
{
  "title": "Learn FastAPI and PostgreSQL",
  "done": true
}
```

### Example Response

```json
{
  "id": 1,
  "title": "Learn FastAPI and PostgreSQL",
  "done": true
}
```

### Expected Status

```text
200 OK
```

---

# 🗑️ 6. Delete a Task

### Request

```http
DELETE /tasks/{task_id}
```

Example:

```http
DELETE /tasks/1
```

### Expected Status

```text
200 OK
```

If the task does not exist:

```text
404 Not Found
```

---

# 📌 HTTP Status Codes

| Status Code | Meaning |
|---|---|
| `200 OK` | Request completed successfully |
| `201 Created` | Resource successfully created |
| `400 Bad Request` | Invalid request |
| `404 Not Found` | Requested task does not exist |
| `422 Unprocessable Entity` | FastAPI validation error |
| `500 Internal Server Error` | Unexpected server-side error |

FastAPI automatically validates incoming request data using Pydantic and returns `422 Unprocessable Entity` when the request does not match the expected schema.

---

# 🗄️ PostgreSQL Database

This project uses **PostgreSQL 16** as its relational database.

The application automatically initializes the database when it starts.

The main table is:

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
);
```

## Database Schema

| Column | Type | Description |
|---|---|---|
| `id` | `SERIAL` | Unique task identifier |
| `title` | `TEXT` | Task title |
| `done` | `BOOLEAN` | Task completion status |

Example:

```text
id | title                         | done
---|-------------------------------|------
1  | Learn FastAPI                 | false
2  | Connect PostgreSQL Database   | false
3  | Push project to GitHub       | false
```

---

# 🌱 Automatic Seed Data

When the application starts, it checks whether the `tasks` table already contains data.

If the table is empty, initial sample tasks are inserted.

Example seed data:

```text
Learn FastAPI
Connect PostgreSQL Database
Push project to GitHub
```

This provides useful data immediately after the first application startup.

Existing database records are preserved.

---

# 🏗️ Repository Pattern

Database operations are separated from the API routes using a **Repository Pattern**.

The repository is located at:

```text
app/repositories/postgres_repository.py
```

The repository handles database operations such as:

```text
initialize_database()
get_all_tasks()
get_task()
create_task()
update_task()
delete_task()
```

This separation provides a cleaner architecture:

```text
API Routes
    │
    ▼
Repository Layer
    │
    ▼
PostgreSQL
```

It also makes the database layer easier to maintain and replace in the future.

---

# 🚀 Application Startup Flow

When the application starts, the following process occurs:

```text
FastAPI starts
      │
      ▼
Application startup
      │
      ▼
PostgresRepository.initialize_database()
      │
      ▼
Connect to PostgreSQL
      │
      ▼
Create tasks table if necessary
      │
      ▼
Check existing tasks
      │
      ▼
Seed initial data if database is empty
      │
      ▼
API becomes available
```

---

# 💾 PostgreSQL Persistence

PostgreSQL data is stored using a **Docker named volume**.

The Docker Compose configuration uses a volume similar to:

```yaml
volumes:
  postgres_data:
```

This allows PostgreSQL data to survive container recreation.

For example:

```bash
docker compose down
```

followed by:

```bash
docker compose up -d
```

will recreate the containers while preserving the database data stored in the named volume.

---

# 🧪 Testing the API

The API can be tested using:

- **Swagger UI**
- **Postman**
- **cURL**
- **Browser** for GET requests
- **Insomnia**
- **Thunder Client**

## Swagger

The easiest way to test the API is:

```text
http://localhost:8000/docs
```

Swagger provides an interactive interface for testing all CRUD operations.

---

# 🛑 Stopping the Application

To stop the application:

```bash
docker compose down
```

This stops and removes the application containers and Docker network.

The PostgreSQL named volume is preserved.

---

# 🗑️ Remove Containers and Database Data

If you want to completely remove the containers **and PostgreSQL database volume**, run:

```bash
docker compose down -v
```

> ⚠️ **Warning:** `-v` removes the PostgreSQL Docker volume. All stored database data will be deleted.

After that, starting the application again will create a fresh PostgreSQL database.

---

# 🔧 Useful Docker Commands

### Check running services

```bash
docker compose ps
```

### Check all containers

```bash
docker compose ps -a
```

### View application logs

```bash
docker compose logs app
```

### View PostgreSQL logs

```bash
docker compose logs db
```

### Follow application logs

```bash
docker compose logs -f app
```

### Follow PostgreSQL logs

```bash
docker compose logs -f db
```

### Restart services

```bash
docker compose restart
```

### Stop services

```bash
docker compose down
```

### Rebuild application

```bash
docker compose build --no-cache
```

### Start everything

```bash
docker compose up -d
```

---

# 💻 Local Development Without Docker

Docker Compose is the recommended setup, but the FastAPI application can also be run directly from a local Python virtual environment.

## 1. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure PostgreSQL

Make sure PostgreSQL is running and configure the appropriate `DATABASE_URL`.

> When running the application **outside Docker**, the database hostname normally needs to point to your local PostgreSQL instance rather than the Docker Compose service name `db`.

---

## 4. Start FastAPI

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🔀 Git Workflow

A feature branch can be used for development.

Example:

```bash
git checkout -b feature/postgresql-docker
```

Check the repository status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit:

```bash
git commit -m "feat: connect FastAPI to PostgreSQL and Dockerize app"
```

Push the branch:

```bash
git push origin feature/postgresql-docker
```

After testing, the feature branch can be merged into the main development branch.

---

# 🔒 Git Security Checklist

Before pushing to GitHub, verify that sensitive files are not staged:

```bash
git status
```

Make sure `.env` is ignored.

If `.env` accidentally appears in staged changes:

```bash
git restore --staged .env
```

Never commit:

```text
.env
```

or real database credentials.

---

# 📊 Current Project Status

The current version of the project includes:

- ✅ FastAPI REST API
- ✅ Complete CRUD functionality
- ✅ PostgreSQL integration
- ✅ Psycopg 3 database driver
- ✅ Automatic database initialization
- ✅ Automatic seed data
- ✅ Repository pattern
- ✅ Dockerfile
- ✅ Docker Compose
- ✅ PostgreSQL Docker volume
- ✅ PostgreSQL health check
- ✅ Environment variables
- ✅ Swagger/OpenAPI documentation
- ✅ ReDoc documentation
- ✅ API validation with Pydantic
- ✅ Git/GitHub workflow

---

# 🚀 Future Improvements

Potential improvements for future versions include:

- 🧪 Automated testing with Pytest
- 🗃️ Database migrations with Alembic
- 🔐 Authentication and authorization
- 👤 User accounts
- 🔎 Task searching and filtering
- 📄 Pagination
- 📝 Structured application logging
- 🔄 API versioning
- ❤️ API health checks
- ⚙️ CI/CD with GitHub Actions
- ☁️ Production deployment
- 📊 Monitoring and observability

---

# 📚 Learning Outcomes

Through this project, the following backend development concepts were practiced:

1. Building REST APIs with FastAPI
2. Implementing CRUD operations
3. Working with PostgreSQL
4. Using Psycopg 3
5. Designing a repository layer
6. Separating API routes from database logic
7. Managing environment variables
8. Containerizing Python applications
9. Creating Docker images
10. Running multiple services with Docker Compose
11. Persisting PostgreSQL data with Docker volumes
12. Using database health checks
13. Debugging Docker and database connectivity
14. Validating API requests with Pydantic
15. Testing APIs through Swagger, cURL, and Postman
16. Managing source code with Git and GitHub

---

# 👨‍💻 Author

**Asheer Hidayat**

Computer Science Student  
COMSATS University Islamabad

### GitHub

https://github.com/Asheer-abbasi01

### Portfolio

https://asheer-portfolio.vercel.app/

---

# 📄 License

This project was created for **educational and internship purposes** as part of the **FlyRank AI Backend AI Engineering Internship — Week 3 (BE-02)**.

You are free to use and modify this project for learning and educational purposes.

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.