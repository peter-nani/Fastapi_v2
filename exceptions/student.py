
class StudentNotFoundException(Exception):
    def __init__(self, stu_id:int):
        self.student_id = stu_id
        message = f"student with id {self.student_id} not found"
        super().__init__(message)