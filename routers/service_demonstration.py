from fastapi import APIRouter, Depends, Query
from models.student import Student
from database.session import get_session
from sqlmodel import Session
from services.student import StudentService
from dependencies.student import get_student_service

router = APIRouter(
    prefix="/service_demon",
    tags=["service_demonstration"],
)

@router.get("/get_student/{stu_id}")
def get_student(
    stu_id:int,
    service: StudentService = Depends(get_student_service)
):
    return service.get_student(stu_id)


@router.get("/students")
def get_students(
    offset: int = Query(
        default=0,
        ge=0
    ),

    limit: int = Query(
        default=10,
        ge=1,
        le=100
    ),
    service: StudentService = Depends(get_student_service)
):

    return service.get_students(
        offset=offset,
        limit=limit
    )