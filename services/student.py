from models.student import Student
from repositories.student import StudentRepository
from schemas.student import StudentCreate
from exceptions.student import StudentNotFoundException

class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def get_student(self, student_id:int)->Student:
        student = self.repository.get(student_id)
        if student is None:
            raise StudentNotFoundException(student_id)
        return student

    def create_student(self, student:StudentCreate)->Student:
        db_student = Student(
            name=student.name,
            age=student.age,
            course=student.course
        )
        return self.repository.create(db_student)