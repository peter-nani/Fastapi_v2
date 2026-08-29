from fastapi import FastAPI, APIRouter, Depends
from schemas.student import StudentCreate, StudentResponse
from models.student import Student
from dependencies.student import get_student_service
from services.student import StudentService

router = APIRouter(
    prefix="/stu_schema",
    tags=["/students_schema"],
)

@router.post("/StudentCreate", response_model=StudentResponse)
def create_student(
    student:StudentCreate,
    service: StudentService = Depends(get_student_service)
    ):
    return service.create_student(student)
