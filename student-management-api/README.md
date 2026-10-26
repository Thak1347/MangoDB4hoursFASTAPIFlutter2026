# Student Management API

A RESTful backend API for a Student Management System built with **FastAPI, Python, and MongoDB**. This project is part of my learning journey to understand backend development, database integration, REST APIs, and Flutter application connectivity.

## Features

- Create a student
- Retrieve all students
- Retrieve a student by student code
- Replace student information
- Partially update student information
- Delete a student
- Validate request data with Pydantic
- Connect to MongoDB asynchronously
- Handle HTTP errors and duplicate student codes
- Enable CORS for Flutter Web development

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11+ | Backend programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| MongoDB | NoSQL database |
| PyMongo | MongoDB database driver |
| Pydantic | Request data validation |
| python-dotenv | Environment variable management |
| Flutter | Frontend application |

## Project Structure

```text
student-management-api/
├── .venv/                  # Python virtual environment
├── .env                    # Environment variables (do not commit)
├── .gitignore              # Files excluded from Git
├── main.py                 # FastAPI application and API endpoints
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Prerequisites

Install the following before starting:

- Python 3.11 or later
- MongoDB Atlas account or a local MongoDB server
- Git (optional)
- Visual Studio Code or another code editor
- Flutter SDK (if connecting a Flutter frontend)

## 1. Clone or Open the Project

If you have already created the project, open your terminal:

```powershell
cd E:\MongoDB\student-management-api
```

## 2. Create and Activate a Virtual Environment

Create the virtual environment if you do not already have one:

```powershell
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

Install the required packages:

```powershell
python -m pip install fastapi "uvicorn[standard]" pymongo python-dotenv
```

Generate a dependency file:

```powershell
python -m pip freeze > requirements.txt
```

If `requirements.txt` already exists, install its dependencies with:

```powershell
python -m pip install -r requirements.txt
```

## 4. Configure MongoDB

Create a `.env` file in the project root:

```dotenv
MONGODB_URI=mongodb+srv://YOUR_USERNAME:YOUR_PASSWORD@YOUR_CLUSTER.mongodb.net/?retryWrites=true&w=majority
MONGODB_DATABASE=student_management
```

Replace the example connection string with your actual MongoDB connection string.

For local MongoDB, you can use:

```dotenv
MONGODB_URI=mongodb://localhost:27017
MONGODB_DATABASE=student_management
```

**Security notes:**

- Never commit `.env` to Git.
- Add `.env` and `.venv/` to `.gitignore`.
- Do not share your MongoDB username, password, or connection string publicly.
- For MongoDB Atlas, configure your database user's permissions and network access.

MongoDB uses the database `student_management` and the collection `students`. The collection can be created automatically when the first student document is inserted.

## 5. Run the Backend

Start the development server:

```powershell
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

When startup succeeds, the API is available at:

- **API base URL:** http://127.0.0.1:8000
- **Interactive Swagger documentation:** http://127.0.0.1:8000/docs
- **Alternative API documentation:** http://127.0.0.1:8000/redoc
- **Database health check:** http://127.0.0.1:8000/health/db

Keep the terminal open while using the API.

## 6. Student Data Model

Each student document contains the following fields:

| Field | Type | Description |
|---|---|---|
| `_id` | String in API response | MongoDB document identifier |
| `student_code` | String | Unique student code, such as `ST001` |
| `name` | String | Student's name |
| `age` | Integer | Student's age, between 1 and 120 |
| `major` | String | Student's major |
| `year` | Integer | Study year, between 1 and 10 |
| `is_active` | Boolean | Whether the student is active |

Example student JSON:

```json
{
  "student_code": "ST001",
  "name": "Dara",
  "age": 21,
  "major": "Software Development",
  "year": 3,
  "is_active": true
}
```

The API validates required fields and numeric ranges. The create endpoint checks for an existing student code and returns HTTP `409 Conflict` if a duplicate is found.

## 7. API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check whether the API is running |
| GET | `/health/db` | Check MongoDB connectivity |
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_code}` | Retrieve one student |
| PUT | `/students/{student_code}` | Replace student fields |
| PATCH | `/students/{student_code}` | Update selected fields |
| DELETE | `/students/{student_code}` | Delete a student |

### Create a Student

**Request**

```http
POST /students
Content-Type: application/json
```

```json
{
  "student_code": "ST007",
  "name": "Maly",
  "age": 20,
  "major": "Software Development",
  "year": 2,
  "is_active": true
}
```

Expected status: `201 Created`.

### Get All Students

```http
GET /students
```

Returns an array of student objects.

### Get One Student

```http
GET /students/ST001
```

Returns the matching student or `404 Not Found` if no student exists.

### Replace Student Information with PUT

PUT requires the complete student request body, including all fields required by `StudentCreate`.

```http
PUT /students/ST001
Content-Type: application/json
```

```json
{
  "student_code": "ST001",
  "name": "Dara",
  "age": 22,
  "major": "Software Development",
  "year": 4,
  "is_active": true
}
```

In the current implementation, the path's student code selects the document to update, while the body supplies the fields to set.

### Partially Update a Student with PATCH

PATCH is useful when you want to change only one or a few fields.

```http
PATCH /students/ST001
Content-Type: application/json
```

```json
{
  "age": 22
}
```

Only the supplied field is updated; other student fields remain unchanged.

### Delete a Student

```http
DELETE /students/ST001
```

Returns a success message or `404 Not Found` if the student does not exist.

## 8. HTTP Status Codes

| Status | Meaning |
|---|---|
| `200 OK` | Request completed successfully |
| `201 Created` | Student created successfully |
| `400 Bad Request` | No fields supplied for a PATCH request |
| `404 Not Found` | Student does not exist |
| `409 Conflict` | Student code already exists |
| `422 Unprocessable Entity` | Request data failed validation |
| `500 Internal Server Error` | Unexpected backend error |

## 9. Connect to Flutter

The correct base URL depends on where Flutter is running.

| Flutter target | API base URL |
|---|---|
| Chrome on the same computer | `http://127.0.0.1:8000` |
| Android emulator | `http://10.0.2.2:8000` |
| Physical Android device | `http://YOUR_COMPUTER_LAN_IP:8000` |

For example, in your Flutter API service:

```dart
static const String baseUrl = 'http://10.0.2.2:8000';
```

Use this URL for the standard Android Studio emulator. `10.0.2.2` routes to the development computer's loopback interface.

### Android Development Notes

For local HTTP development, Android may require Internet permission and cleartext HTTP configuration.

In `android/app/src/main/AndroidManifest.xml`, place the permission directly under the `<manifest>` element:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

If necessary, allow cleartext traffic on the `<application>` element for local development. Do not enable unrestricted cleartext traffic in a production application; use HTTPS for deployed APIs.

### Flutter Web and CORS

FastAPI uses `CORSMiddleware` to allow browser-based requests from Flutter Web. For local development, the API can permit your current Flutter development origin.

Restrict `allow_origins` to trusted production frontend origins before deployment.

## 10. Troubleshooting

### MongoDB connection fails

- Check that `.env` exists and contains the correct `MONGODB_URI`.
- Confirm that your MongoDB Atlas network access and database user permissions are configured.
- Check the backend terminal for the full traceback.

### `422 Unprocessable Entity`

Check the JSON request body. Ensure required fields are present and values have the correct types.

### `404 Student not found`

Verify the student code and confirm that the student exists in the configured database.

### `500 Internal Server Error`

Read the Python traceback in the Uvicorn terminal. The HTTP status alone does not reveal the exact cause.

### Flutter cannot connect

- Confirm that FastAPI is running on port `8000`.
- Verify that the correct base URL is used for the Flutter target.
- For Flutter Web, inspect the Chrome Console for CORS errors.
- For Android, check Internet permission and local HTTP settings.
- Test the API directly at http://127.0.0.1:8000/docs.

### Emulator reports insufficient storage

Free emulator storage or increase the virtual device's internal storage in Android Studio Device Manager. This installation problem is separate from the backend.

## 11. Git Configuration

Create a `.gitignore` file:

```gitignore
# Environment variables
.env
.env.*

# Keep an example configuration if you create one
!.env.example

# Python
.venv/
__pycache__/
*.py[cod]
.pytest_cache/

# IDE and editor
.vscode/
.idea/

# Operating system
.DS_Store
Thumbs.db
```

Never include real credentials in `.env.example`. Use placeholder values.

## Learning Objectives

This project helps me practise:

- REST API design and HTTP methods
- CRUD operations with MongoDB
- Python asynchronous programming
- Request validation with Pydantic
- Environment variable management
- Error handling and API testing
- Flutter-to-backend communication
- CORS and local development networking
- Git and project documentation

## Future Improvements

- Add authentication and role-based authorization.
- Add pagination, search, filtering, and sorting.
- Enforce student-code uniqueness with a MongoDB unique index.
- Add automated tests with Pytest and FastAPI's test client.
- Separate routers, models, services, and database configuration into modules.
- Add structured logging and centralized error handling.
- Deploy the API with HTTPS and production configuration.

## Author

**Pithak Chhorn**

Software Development Student | Full-Stack Developer in Training

GitHub: [Thak1347](https://github.com/Thak1347)

Portfolio: [Personal Portfolio](https://thak1347.github.io/Portfolio_Self/)

---

*Built as a hands-on learning project for backend development and Flutter application integration.*
