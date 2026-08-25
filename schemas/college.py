
from pydantic import BaseModel

class college_info(BaseModel):
    college : str
    station : str | None
    affiliated : str | None
    min_stu_count : int | None
    max_stu_count : int | None

class college_request_model(BaseModel):
    college : str
