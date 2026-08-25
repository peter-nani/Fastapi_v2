from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/student",
    tags=["students"],
)


# --------------------------------------------------
# In-memory database
# --------------------------------------------------

STUDENTS = [
    {
        "id": 1,
        "name": "Prasanna Kumar",
        "age": 24,
        "branch": "electronics"
    },
    {
        "id": 2,
        "name": "Sravan",
        "age": 24,
        "branch": "computers"
    }
]


# --------------------------------------------------
# Pydantic models
# --------------------------------------------------

class Student(BaseModel):
    name: str
    age: int
    branch: str


class StudentPatch(BaseModel):
    name: str | None = None
    age: int | None = None
    branch: str | None = None


# --------------------------------------------------
# GET - Get all students
# --------------------------------------------------

@router.get("/students")
def get_students():
    return STUDENTS


# --------------------------------------------------
# GET - Get one student
# --------------------------------------------------

@router.get("/students/{student_id}")
def get_student(student_id: int):

    for student in STUDENTS:

        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# --------------------------------------------------
# POST - Create a new student
# --------------------------------------------------

@router.post("/students")
def add_student(student: Student):

    # Generate new ID
    new_id = max(
        [student["id"] for student in STUDENTS],
        default=0
    ) + 1

    new_student = {
        "id": new_id,
        **student.model_dump()
    }

    STUDENTS.append(new_student)

    return new_student


# --------------------------------------------------
# PUT - Replace an entire student
# --------------------------------------------------

@router.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: Student
):

    for index, existing_student in enumerate(STUDENTS):

        if existing_student["id"] == student_id:

            updated_student = {
                "id": student_id,
                **student.model_dump()
            }

            STUDENTS[index] = updated_student

            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# --------------------------------------------------
# PATCH - Partially update a student
# --------------------------------------------------

@router.patch("/students/{student_id}")
def patch_student(
    student_id: int,
    student: StudentPatch
):

    for existing_student in STUDENTS:

        if existing_student["id"] == student_id:

            update_data = student.model_dump(
                exclude_unset=True
            )

            existing_student.update(update_data)

            return existing_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# --------------------------------------------------
# DELETE - Delete a student
# --------------------------------------------------

@router.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(STUDENTS):

        if student["id"] == student_id:

            deleted_student = STUDENTS.pop(index)

            return deleted_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )