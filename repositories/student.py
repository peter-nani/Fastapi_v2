from database.session import get_session
from models.student import Student
from sqlmodel import Session, select

class StudentRepository:
    def __init__(self, session:Session):
        self.session = session

    def create(self, student:Student):
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def get(self, stu_id:int)->Student|None:
        return self.session.get(Student,stu_id)