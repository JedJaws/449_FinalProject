from typing import Optional
from fastapi import Body, FastAPI, Path
from pydantic import BaseModel
app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

class Book(BaseModel):
    title: str
    author: str
    description: str
    price: float
    stock: int

class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


@app.get('/')
def index():
    return {'name': 'First Data'}

# path parameter
@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(description="The ID of the student you wantto view", gt=0, lt=3)):
    return students[student_id]

# Query parameter
@app.get('/get-by-name')
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

# Query parameter (Optional)
@app.get('/get-by-name-optional')
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

# Query parameter (Optional) - ERROR without *
# * allows us to write parameters anywhere we want
@app.get('/get-by-name-optional')
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

# combining path and query parameters
@app.get('/get-by-name-optional/{student_id}')
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

# Request Body and the Post Method
@app.post("create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

# PUT method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exists"}
    students[student_id] = student
    return students[student_id]

# On updating just the name, other values gets overwritten by null.
# {
# name: "alex"
# age: null
# year: null
# }

# PUT method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exists"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]

# On updating just the name, other values remains as it is.
# {
# name: "alex"
# age: 24
# year: 2021
# }

# Delete Method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exists"}
    del students[student_id]
    return {"Message": "student deleted successfully"}
