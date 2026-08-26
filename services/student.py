from models.student import Student
from repositories.student import StudentRepository

class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def get_student(self, student_id:int)->Student:
        student = self.repository.get(student_id)
        return student