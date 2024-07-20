from fastapi import APIRouter

from routers.db import execute_query
from routers.model import StudentCreate

get_data = APIRouter()


@get_data.get("/check/{number}")
def check_value(number: int):
    if number % 2 == 0:
        return {"number": number, "result": "even"}
    else:
        return {"number": number, "result": "odd"}

@get_data.post("/student/{name}/{age}/{grade}")
async def create_student(student:StudentCreate ):
    query=""" INSERT INTO student (name,age,grade) VALUES ($1,$2,$3) RETURNING id;
    """

    student_id=await execute_query(query,student.name ,student.age,student.grade)
    return {**student.dict(),"id":student_id}


