from fastapi import APIRouter, Depends
from models.student import Student
from database.session import get_session
from sqlmodel import Session

router = APIRouter(
    prefix="/students_in",
    tags=["students_information"],
)

@router.post("/student_add", response_model=Student)
def add_student(
    stu:Student,
    session:Session = Depends(get_session) ,
    )-> Student:
    valid_student = Student.model_validate(stu)
    session.add(valid_student)
    session.commit()
    session.refresh(valid_student)
    return stu
    