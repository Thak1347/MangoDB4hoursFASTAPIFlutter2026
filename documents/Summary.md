# Summary Lesson: MongoDB + FastAPI + Flutter

## Overview

This document summarizes the four lessons for building a Student Management application using MongoDB, FastAPI, and Flutter.

**Learning objectives**
- Understand MongoDB fundamentals.
- Perform CRUD operations and query filtering.
- Build REST API endpoints with FastAPI.
- Connect Flutter to FastAPI and display student records.

## Lesson 1: MongoDB Fundamentals

### Key concepts

- **Database:** Stores collections.
- **Collection:** Stores related documents.
- **Document:** Stores data as key-value pairs.
- **Field:** A single property inside a document.
- **BSON:** The binary representation MongoDB uses to store documents.
- **`_id`:** A unique identifier automatically created for documents unless provided.

### Example document

```javascript
{
  student_code: "ST001",
  name: "Dara",
  age: 20,
  major: "Software Development",
  year: 2,
  is_active: true
}
```

### Important commands

```javascript
show dbs
use student_management
db.createCollection("students")
db.students.find()
```

**Practice:** Create a database and a `students` collection. Insert several student documents and retrieve them.

## Lesson 2: CRUD Operations and Query Filters

CRUD stands for **Create, Read, Update, and Delete**.

| Operation | MongoDB method | Purpose |
|---|---|---|
| Create | `insertOne()` | Insert one document |
| Read | `find()` / `findOne()` | Retrieve documents |
| Update | `updateOne()` | Update a document |
| Delete | `deleteOne()` | Delete a document |

### Create

```javascript
db.students.insertOne({
  student_code: "ST002",
  name: "Lina",
  age: 21,
  major: "Computer Science",
  year: 3,
  is_active: true
})
```

### Read with a filter

```javascript
db.students.find({ major: "Software Development" })
db.students.find({ age: { $gte: 20 } })
db.students.find({ year: { $in: [2, 3] } })
```

### Update one field

```javascript
db.students.updateOne(
  { student_code: "ST001" },
  { $set: { age: 22 } }
)
```

### Delete

```javascript
db.students.deleteOne({ student_code: "ST002" })
```

**Important:** `updateOne()` updates only the first matching document. Use `$set` to change selected fields without replacing the whole document.

## Lesson 3: MongoDB + FastAPI Backend

FastAPI provides HTTP endpoints that allow applications to interact with MongoDB.

### Typical project structure

```text
student-management-api/
├── app/
│   ├── main.py
│   └── database.py
├── .env
├── requirements.txt
└── README.md
```

### Install dependencies

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

Use a compatible PyMongo version that supports the async API if your backend uses `AsyncMongoClient`.

### Configure the database

Store your MongoDB connection string in `.env`:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=student_management
```

Do not commit credentials or sensitive connection strings to GitHub.

### REST API endpoints

| HTTP method | Endpoint | Purpose |
|---|---|---|
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_code}` | Retrieve one student |
| PUT | `/students/{student_code}` | Replace a student's data |
| PATCH | `/students/{student_code}` | Update selected fields |
| DELETE | `/students/{student_code}` | Delete a student |

### Test the API

Run the development server:

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

**Important:** `PUT` generally represents replacing a resource, while `PATCH` represents a partial update. Your API's validation and implementation should match that behavior.

## Lesson 4: Flutter + FastAPI

Flutter is the client application. FastAPI is the backend, and MongoDB stores the data.

### Data flow

```text
Flutter UI
   ↓ HTTP request
FastAPI endpoint
   ↓ Database query
MongoDB
   ↓ JSON response
FastAPI
   ↓ HTTP response
Flutter parses JSON
   ↓
Student list displayed
```

### Main Flutter tasks

1. Add an HTTP client package, such as `http` or Dio.
2. Send a GET request to the FastAPI endpoint.
3. Check the HTTP status code.
4. Decode the JSON response.
5. Convert JSON maps into Dart model objects.
6. Display the records using widgets such as `ListView.builder`.
7. Handle loading, empty, and error states.

### Example JSON response

```json
[
  {
    "student_code": "ST001",
    "name": "Dara",
    "age": 20,
    "major": "Software Development",
    "year": 2,
    "is_active": true
  }
]
```

### Important networking note

When testing on an Android emulator, `localhost` normally refers to the emulator itself. For a FastAPI server running on your development computer, use:

```text
http://10.0.2.2:8000
```

This address is for the standard Android Studio emulator. A physical device usually needs your computer's reachable local network IP address, with the server listening on an accessible interface.

## Final Practice Project: Student Management

Build a small application with the following features:

- Display all students.
- View an individual student's details.
- Add a new student.
- Edit a student's information.
- Delete a student.
- Show loading indicators and error messages.
- Validate required fields.
- Refresh the student list after a successful change.

### Recommended implementation order

1. Verify MongoDB CRUD operations.
2. Finish and test the FastAPI endpoints.
3. Test each endpoint in `/docs`.
4. Create the Flutter student model.
5. Implement the API service.
6. Build the student list screen.
7. Add create, edit, and delete forms.
8. Test the full flow from Flutter to MongoDB.

## Self-Assessment Checklist

- [ ] I can explain databases, collections, and documents.
- [ ] I can use `insertOne()`, `find()`, `updateOne()`, and `deleteOne()`.
- [ ] I understand common query filters such as `$gte`, `$in`, `$and`, and `$or`.
- [ ] I can create and test REST API endpoints with FastAPI.
- [ ] I can connect FastAPI to MongoDB.
- [ ] I understand JSON request and response bodies.
- [ ] I can send an HTTP request from Flutter.
- [ ] I can parse JSON and display student records.
- [ ] I can debug common connection, validation, and HTTP errors.

## Final Summary

MongoDB stores the student data, FastAPI exposes that data through REST API endpoints, and Flutter provides the user interface. Understanding how these three parts communicate is the foundation for building a complete student management system.

**Next step:** Build and test the complete student list feature before moving on to create, update, and delete features.
