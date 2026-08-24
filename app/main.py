from fastapi import FastAPI

app = FastAPI()

STUDENTS = [
    {"student_name":"Prasanna Kumar", "age":24, "branch":"electronics"},
    {"student_name":"Sravan", "age":24, "branch":"computers" }
]


@app.get("/students")
def all_students():
    return STUDENTS
