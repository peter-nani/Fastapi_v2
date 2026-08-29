from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from exceptions.student import StudentNotFoundException

async def stu_not_found_handler(
        request:Request,
        exec: StudentNotFoundException,
):
    return JSONResponse(
        status_code=404,
        content={
            "message": str(exec),
        }
    )

def register_exception_handlers(app: FastAPI) -> None:# That's just one clean way to organize multiple handlers outside main.py.
    app.add_exception_handler(
        StudentNotFoundException,
        stu_not_found_handler,
    )