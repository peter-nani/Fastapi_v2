from fastapi import FastAPI
from routers.student_router import router as student_route
app = FastAPI()

# STUDENTS = [
#     {"student_name":"Prasanna Kumar", "age":24, "branch":"electronics"},
#     {"student_name":"Sravan", "age":24, "branch":"computers" }
# ]


# @app.get("/students")
# def all_students():
#     return STUDENTS

app.include_router(student_route)