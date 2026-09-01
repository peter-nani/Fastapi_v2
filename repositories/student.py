from sqlmodel import Session, select
from models.student import Student

class StudentRepository:

    def __init__(self, session:Session):
        self.session = session

    def create(self, student:Student):
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def get(self, student_id: int):
        return self.session.get(Student, student_id)

    def get_all(self,offset:int=0, limit:int=10)->list[Student]:
        statement = (
            select(Student)
            .offset(offset)
            .limit(limit)
            )
        return self.session.exec(statement).all()