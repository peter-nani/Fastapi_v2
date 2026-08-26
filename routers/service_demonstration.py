from fastapi import APIRouter, Depends
from database.session import get_session
from repositories.student import StudentRepository
from sqlmodel import Session
from services.student import StudentService

router = APIRouter(
    prefix="/student_in",
    tags=["student_information"],
)



@router.get("/get_student/{stu_id}")
def get_student(stu_id:int, session:Session = Depends(get_session)):
    repository = StudentRepository(session)
    service = StudentService(repository)
    return service.get_student(stu_id)