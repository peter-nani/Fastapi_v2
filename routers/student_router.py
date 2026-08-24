from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/student",
    tags=["students"],
)

STUDENTS = [
    {"student_name":"Prasanna Kumar", "age":24, "branch":"electronics"},
    {"student_name":"Sravan", "age":24, "branch":"computers" }
]

@router.get("/students_repository")
def get_students():
    return STUDENTS