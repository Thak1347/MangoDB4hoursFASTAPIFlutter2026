# MongoDB 4-Hour Learning Course

A practical, beginner-friendly learning course covering MongoDB fundamentals, CRUD operations, FastAPI backend development, and Flutter HTTP API integration.

The course uses a **Student Management System** as a hands-on project to connect database concepts with real application development.

## Course Overview

| Lesson | Topic | Duration |
|---|---|---:|
| 1 | MongoDB Fundamentals | 1 hour |
| 2 | CRUD Operations and Query Filters | 1 hour |
| 3 | MongoDB and FastAPI | 1 hour |
| 4 | Flutter + FastAPI: Display Student Records | 1 hour |
| **Total** | **Four practical lessons** | **4 hours** |

## Learning Objectives

By completing these four lessons, you should be able to:

- Understand MongoDB databases, collections, documents, and fields.
- Create, read, update, and delete MongoDB documents.
- Apply query filters and update operators.
- Configure a MongoDB connection for a Python application.
- Build REST API endpoints using FastAPI.
- Test backend endpoints using Swagger UI.
- Send HTTP requests from Flutter.
- Parse JSON responses and display student records.
- Troubleshoot common database, API, and network errors.

## Lesson Roadmap

### Lesson 1 — MongoDB Fundamentals (1 Hour)

**File:** `1.MongoDB-Fundamental-1hour.md`

Learn the basic concepts of MongoDB and practice storing student information.

Topics:
- Introduction to NoSQL databases.
- MongoDB versus relational databases.
- Database, collection, document, and field.
- BSON and the `_id` field.
- Installing MongoDB or configuring MongoDB Atlas.
- Creating databases and collections.
- Inserting and retrieving documents.

**Practice task:** Create a `student_management` database, create a `students` collection, insert sample student records, and retrieve them.

### Lesson 2 — CRUD Operations and Query Filters (1 Hour)

**File:** `2.CRUD_and_query_filters-1hour.md`

Learn how to manage student records with MongoDB queries.

Topics:
- Create: `insertOne()` and `insertMany()`.
- Read: `find()` and `findOne()`.
- Update: `updateOne()` and `updateMany()`.
- Delete: `deleteOne()` and `deleteMany()`.
- Comparison operators: `$eq`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`.
- Logical operators: `$and` and `$or`.
- Sorting, projection, and limiting results.
- Update operators such as `$set` and `$inc`.

**Practice task:** Search for students by major, update one student's age, filter students by year, and delete a selected test record.

### Lesson 3 — MongoDB and FastAPI (1 Hour)

**File:** `3.MongoDB-and-FastAPI.md`

Connect MongoDB to a Python backend and expose student data through a REST API.

Topics:
- Introduction to REST APIs.
- FastAPI project structure.
- Connecting Python to MongoDB using PyMongo.
- Environment variables and `.env` configuration.
- Request validation and JSON responses.
- Implementing student CRUD endpoints.
- Testing APIs through Swagger UI.

**Practice task:** Build and test endpoints for creating, listing, retrieving, updating, and deleting student records.

| HTTP method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/students` | Create a student |
| `GET` | `/students` | Get all students |
| `GET` | `/students/{student_code}` | Get one student |
| `PUT` | `/students/{student_code}` | Replace student data |
| `PATCH` | `/students/{student_code}` | Update selected fields |
| `DELETE` | `/students/{student_code}` | Delete a student |

Run the backend from the directory containing the `app` package:

```bash
uvicorn app.main:app --reload
```

Open the API documentation at `http://127.0.0.1:8000/docs`.

### Lesson 4 — Flutter + FastAPI: Display Student Records (1 Hour)

**File:** `4.Flutter_FastAPI_Display_Students.md`

Connect the Flutter frontend to your FastAPI backend and display real student data.

Topics:
- HTTP requests and REST API communication.
- Using an HTTP client package in Flutter.
- Sending GET requests.
- Parsing JSON into Dart model objects.
- Displaying records using `ListView.builder`.
- Handling loading, empty, and error states.
- Configuring the backend URL for an emulator or physical device.

**Practice task:** Fetch students from FastAPI and display each student's code, name, major, and year in a Flutter screen.

## Project Architecture

```text
Flutter Application
  flutterhttdoiapi/
        |
        | HTTP Requests / JSON Responses
        v
FastAPI Backend
  student-management-api/
        |
        | PyMongo
        v
MongoDB Database
  student_management
        |
        v
  students Collection
```

## Repository Structure

```text
MONGODB\DOCUMENTS\
├── README.md
├── 1.MongoDB-Fundamental-1hour.md
├── 2.CRUD_and_query_filters-1hour.md
├── 3.MongoDB-and-FastAPI.md
├── 4.Flutter_FastAPI_Display_Students.md
├── SetupMangoDB.md
├── Summary.md
├── student-management-api/
│   ├── app/
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
└── flutterhttdoiapi/
    ├── lib/
    └── pubspec.yaml
```

> **Note:** The setup guide is named `SetupMangoDB.md` in your current structure. You may rename it to `SetupMongoDB.md` for correct spelling. Update any references if you rename it.

## Setup Guide

Before starting the lessons, follow `SetupMangoDB.md`.

### Prerequisites

- Python and pip.
- MongoDB Community Server or MongoDB Atlas.
- MongoDB Shell (`mongosh`).
- Flutter SDK and Dart.
- Android Studio emulator or a physical Android device.
- Visual Studio Code or another code editor.
- Git and GitHub.

### Backend Setup

Open a terminal in `student-management-api` and install the dependencies:

```bash
pip install -r requirements.txt
```

Configure your `.env` file using `.env.example` as a template. For a local MongoDB server, a typical configuration is:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=student_management
```

Start FastAPI using the command appropriate for your project structure:

```bash
uvicorn app.main:app --reload
```

### Flutter Setup

Open a separate terminal in `flutterhttdoiapi`:

```bash
flutter pub get
flutter run
```

For the standard Android Studio emulator, a local backend running on your computer is usually accessible at:

```text
http://10.0.2.2:8000
```

For Flutter Web, configure the appropriate CORS origin. For a physical device, use a reachable computer IP address and ensure the backend is listening on an accessible interface.

## Final Practice Project

Build a basic Student Management application with the following features:

- [ ] Connect FastAPI to MongoDB.
- [ ] Create and retrieve student records.
- [ ] Update student information.
- [ ] Delete student records.
- [ ] Test API endpoints in Swagger UI.
- [ ] Display students in Flutter.
- [ ] Handle loading and error states.
- [ ] Keep database credentials out of GitHub.
- [ ] Document installation and execution steps.

## Troubleshooting

| Problem | What to check |
|---|---|
| MongoDB connection refused | Confirm the MongoDB service is running and the connection string is correct. |
| HTTP `404` | Check the endpoint path and HTTP method. |
| HTTP `422` | Check request data and FastAPI validation rules. |
| Flutter cannot connect | Check the API URL, server binding, firewall, and device network. |
| CORS error | Configure the frontend origin in FastAPI. |
| MongoDB `ObjectId` JSON error | Convert `ObjectId` to a JSON-compatible string before returning documents. |

## Learning Summary

The four lessons follow a progressive learning path:

1. **Understand** MongoDB fundamentals.
2. **Practice** database CRUD operations and query filters.
3. **Build** a FastAPI backend connected to MongoDB.
4. **Integrate** Flutter with the API and display student records.

After completing this course, the next step is to add Flutter forms for creating and editing students, then implement authentication and role-based authorization.

## Official Documentation

- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [PyMongo Documentation](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Flutter Documentation](https://docs.flutter.dev/)
- [Dart Documentation](https://dart.dev/guides)

---

**Course:** MongoDB 4-Hour Learning Course  
**Project:** Student Management System  
**Level:** Beginner  
**Duration:** 4 hours  
**Learning approach:** Hands-on, project-based practice

---

## About Me

Hi, I'm **Chhorn Pithak**, a Software Development student at the National University of Laos (NUOL), interested in full-stack development, mobile application development, and UI/UX design.

I'm continuously improving my technical skills through hands-on projects and self-study. This MongoDB 4-hour learning course documents my journey in learning database fundamentals, building REST APIs with FastAPI, and connecting Flutter applications to backend services.

I created this repository to organize my learning materials, practice practical development skills, and share my progress with the developer community.

### Connect with Me

- **GitHub:** [@Thak1347](https://github.com/Thak1347)
- **Portfolio:** [View My Portfolio](https://thak1347.github.io/Portfolio_Self/)

*Keep learning, keep building, and keep improving.*


