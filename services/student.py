from models.student import Student
from repositories.student import StudentRepository

class StudentService:
    def __init__(self, repository:StudentRepository):
        self.repository = repository

    def get_student(self, stu_id:int)-> Student:
        return self.repository.get(stu_id)