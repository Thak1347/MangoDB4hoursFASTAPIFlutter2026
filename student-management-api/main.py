
import os
from contextlib import asynccontextmanager

from bson import ObjectId
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pymongo import AsyncMongoClient
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()



MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv(
    "MONGODB_DATABASE",
    "student_managemnet"
)

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI is not configured")


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncMongoClient(MONGODB_URI)

    try:
        await client.admin.command("ping")
        app.state.mongo_client = client
        app.state.database = client[DATABASE_NAME]
        yield
    finally:
        await client.close()


app = FastAPI(lifespan=lifespan)

# 3. Configure CORS for Flutter Web on Chrome
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentCreate(BaseModel):
    student_code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    age: int = Field(ge=1, le=120)
    major: str
    year: int = Field(ge=1, le=10)
    is_active: bool = True


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    age: int | None = Field(default=None, ge=1, le=120)
    major: str | None = None
    year: int | None = Field(default=None, ge=1, le=10)
    is_active: bool | None = None


def serialize_student(student: dict) -> dict:
    student["_id"] = str(student["_id"])
    return student


@app.get("/")
async def root():
    return {"message": "Student Management API is running"}


@app.get("/health/db")
async def database_health():
    await app.state.database.command("ping")
    return {
        "status": "connected",
        "database": DATABASE_NAME
    }


@app.post("/students", status_code=201)
async def create_student(student: StudentCreate):
    db = app.state.database
    document = student.model_dump()

    existing = await db.students.find_one(
        {"student_code": document["student_code"]}
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Student code already exists"
        )

    result = await db.students.insert_one(document)

    created = await db.students.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_student(created)


@app.get("/students")
async def list_students():
    db = app.state.database

    students = await db.students.find().to_list(
        length=100
    )

    return [serialize_student(s) for s in students]


@app.get("/students/{student_code}")
async def get_student(student_code: str):
    db = app.state.database

    student = await db.students.find_one(
        {"student_code": student_code}
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return serialize_student(student)


@app.put("/students/{student_code}")
async def update_student(
    student_code: str,
    student: StudentCreate
):
    db = app.state.database

    result = await db.students.update_one(
        {"student_code": student_code},
        {"$set": student.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updated = await db.students.find_one(
        {"student_code": student_code}
    )

    return serialize_student(updated)


@app.patch("/students/{student_code}")
async def partial_update_student(
    student_code: str,
    student: StudentUpdate
):
    db = app.state.database

    # Get only the fields provided in the request
    update_data = student.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    result = await db.students.update_one(
        {"student_code": student_code},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updated = await db.students.find_one(
        {"student_code": student_code}
    )

    return serialize_student(updated)


@app.delete("/students/{student_code}")
async def delete_student(student_code: str):
    db = app.state.database

    result = await db.students.delete_one(
        {"student_code": student_code}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}


