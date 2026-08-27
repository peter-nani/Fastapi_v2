from repositories.student import StudentRepository
from database.session import get_session
from sqlmodel import Session
from fastapi import Depends
from services.student import StudentService

def get_student_repository(session:Session = Depends(get_session))->StudentRepository:
    return StudentRepository(session)

def get_student_service(repository:StudentRepository = Depends(get_student_repository))->StudentService:
    return StudentService(repository)