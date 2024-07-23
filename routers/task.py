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


@get_data.put("/student/{id}")
async def update_student(id: int, student: StudentCreate):
    query = """UPDATE student SET name = $1, age = $2, grade = $3 WHERE id = $4 RETURNING id;"""

    u_student_id = await execute_query(query, student.name, student.age, student.grade, id)
    return {**student.dict(), "id": u_student_id}

@get_data.delete("/student/{id}")
async def delete_student(id: int):
    query = """DELETE FROM student WHERE id = $1 RETURNING id; """

    d_student_id = await execute_query(query, id)
    return {"id": d_student_id}