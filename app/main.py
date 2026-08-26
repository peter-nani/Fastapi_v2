from fastapi import FastAPI
from routers.student_router import router as student_route
from routers.college_route import router as college_route
from routers.db_demonstration import router as db_demon_route
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from database.engine import engine
from routers.service_demonstration import router as service_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

# STUDENTS = [
#     {"student_name":"Prasanna Kumar", "age":24, "branch":"electronics"},
#     {"student_name":"Sravan", "age":24, "branch":"computers" }
# ]


# @app.get("/students")
# def all_students():
#     return STUDENTS

app.include_router(student_route)
app.include_router(college_route)
app.include_router(db_demon_route)
app.include_router(service_route)