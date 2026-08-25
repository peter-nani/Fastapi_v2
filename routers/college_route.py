from fastapi import APIRouter
from schemas.college import college_request_model, college_info
router = APIRouter(
    prefix="/college",
    tags=["college"],
)

@router.post("/add_college")
def ad_college(input_college_model:college_request_model)-> college_info:
    return college_info(
        college=input_college_model.college,
        station = None,
        affiliated = None,
        min_stu_count = None,
        max_stu_count = None,
    )