# Setup MongoDB for Student Management API

## 1. Introduction

MongoDB is a NoSQL database that stores data in flexible, JSON-like documents. In this project, MongoDB stores student records, while FastAPI provides the REST API used by the frontend.

### Technology stack

- **Database:** MongoDB
- **Backend:** Python + FastAPI
- **Database driver:** PyMongo
- **Configuration:** Python dotenv
- **API testing:** FastAPI Swagger UI

## 2. Install MongoDB

There are two common options.

### Option A: MongoDB Community Server (Local)

Use this option to run MongoDB on your computer.

1. Visit the official MongoDB Community Server download page: https://www.mongodb.com/try/download/community
2. Select Windows as your operating system.
3. Download the MSI installer.
4. Run the installer and follow the setup wizard.
5. Choose to install MongoDB as a Windows service if that option is available.
6. Complete the installation.

The default local connection string is usually:

```text
mongodb://localhost:27017
```

### Option B: MongoDB Atlas (Cloud)

Use Atlas if you prefer a cloud-hosted database.

1. Visit https://www.mongodb.com/cloud/atlas
2. Create an account and a project.
3. Create a database deployment.
4. Create a database user with a strong password.
5. Configure network access to allow your development computer to connect.
6. Open **Connect**, select the application connection option, and copy the connection string.
7. Replace the username, password, and other placeholders with your actual values.

Never publish your database password or connection string containing credentials in a public repository.

## 3. Verify the Installation

### Check the MongoDB service

On Windows, open **Services** and look for the MongoDB service. If installed as a service, ensure it is running.

You can also check the service from PowerShell:

```powershell
Get-Service MongoDB
```

If the service is not installed under that name, check the service name configured during installation.

### Check MongoDB Shell

If `mongosh` is installed, open PowerShell or a terminal and run:

```bash
mongosh
```

To connect explicitly to the local server:

```bash
mongosh "mongodb://localhost:27017"
```

If the command is not recognized, install MongoDB Shell from the official download page:

https://www.mongodb.com/try/download/shell

## 4. Create the Database and Collection

In MongoDB Shell, run:

```javascript
use student_management
```

MongoDB creates the database when data is first stored in it.

Create the collection:

```javascript
db.createCollection("students")
```

Check the available databases:

```javascript
show dbs
```

List collections in the current database:

```javascript
show collections
```

**Note:** An empty database may not appear in `show dbs` until it contains stored data.

## 5. Insert Test Student Data

Insert a student:

```javascript
db.students.insertOne({
  student_code: "ST001",
  name: "Dara",
  age: 20,
  major: "Software Development",
  year: 2,
  is_active: true
})
```

Insert multiple students:

```javascript
db.students.insertMany([
  {
    student_code: "ST002",
    name: "Lina",
    age: 21,
    major: "Computer Science",
    year: 3,
    is_active: true
  },
  {
    student_code: "ST003",
    name: "Vannak",
    age: 19,
    major: "Information Technology",
    year: 1,
    is_active: true
  }
])
```

Retrieve all student records:

```javascript
db.students.find()
```

Display documents in a readable format:

```javascript
db.students.find().pretty()
```

## 6. Connect MongoDB to FastAPI

### Install Python packages

From your backend project directory, run:

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

If your application uses PyMongo's asynchronous API, install a current compatible PyMongo version and use `AsyncMongoClient`.

### Create a `.env` file

Place the `.env` file in your backend project root:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=student_management
```

For MongoDB Atlas, use your Atlas connection string instead.

### Example project structure

```text
student-management-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── database.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Example `database.py` using asynchronous PyMongo

```python
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from pymongo import AsyncMongoClient

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "student_management")

if not MONGODB_URL:
    raise RuntimeError("MONGODB_URL is not configured")


@asynccontextmanager
async def mongodb_lifespan(app):
    client = AsyncMongoClient(MONGODB_URL)

    try:
        await client.admin.command("ping")
        app.state.mongodb_client = client
        app.state.db = client[DATABASE_NAME]
        yield
    finally:
        await client.close()
```

In your FastAPI application, use the lifespan function to initialize and close the database connection:

```python
from fastapi import FastAPI
from app.database import mongodb_lifespan

app = FastAPI(lifespan=mongodb_lifespan)


@app.get("/health/database")
async def database_health():
    await app.state.db.command("ping")
    return {"database": "connected"}
```

This example assumes your installed PyMongo version supports `AsyncMongoClient`.

## 7. Protect Your Environment Variables

Add these entries to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
```

Commit an `.env.example` file containing placeholders, not real credentials:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=student_management
```

For production, use your hosting provider's environment-variable or secret-management settings.

## 8. Test the FastAPI Connection

Start your backend:

```bash
uvicorn app.main:app --reload
```

Open the database health endpoint:

```text
http://127.0.0.1:8000/health/database
```

Expected response:

```json
{
  "database": "connected"
}
```

You can also open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## 9. Common Problems

| Problem | Possible solution |
|---|---|
| `mongosh` is not recognized | Install MongoDB Shell or configure its executable path. |
| Connection refused | Confirm the MongoDB service is running and the port is correct. |
| Authentication failed | Verify the database username, password, and authentication configuration. |
| Atlas connection fails | Check network access rules and the connection string. |
| Environment variable is `None` | Check `.env` location, spelling, and `load_dotenv()`. |
| Database not listed | Insert data first, then run `show dbs`. |
| Port `27017` is unavailable | Check whether another process is using the port or change the MongoDB configuration. |

## 10. Setup Checklist

- [ ] MongoDB Community Server or Atlas is ready.
- [ ] MongoDB Shell is available if needed.
- [ ] MongoDB accepts connections.
- [ ] The `student_management` database is configured.
- [ ] The `students` collection exists.
- [ ] Test student records can be inserted and queried.
- [ ] FastAPI connects successfully to MongoDB.
- [ ] `.env` is excluded from Git.
- [ ] The database health endpoint works.

## Official Documentation

- MongoDB Community Server: https://www.mongodb.com/try/download/community
- MongoDB Shell: https://www.mongodb.com/try/download/shell
- MongoDB Atlas: https://www.mongodb.com/cloud/atlas
- MongoDB Manual: https://www.mongodb.com/docs/manual/
- PyMongo documentation: https://www.mongodb.com/docs/languages/python/pymongo-driver/current/
- FastAPI documentation: https://fastapi.tiangolo.com/

---

**Next step:** Once MongoDB is running and FastAPI can connect, implement and test the student CRUD endpoints.
