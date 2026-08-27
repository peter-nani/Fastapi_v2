from fastapi import APIRouter, Depends
from database.session import get_session
from repositories.student import StudentRepository
from sqlmodel import Session
from services.student import StudentService
from dependencies.student import get_student_service

router = APIRouter(
    prefix="/student_dep",
    tags=["student_dependency"],
)



@router.get("/get_student/{stu_id}")
def get_student(stu_id:int, service:StudentService = Depends(get_student_service)):
    return service.get_student(stu_id)