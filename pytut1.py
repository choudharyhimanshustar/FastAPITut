from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

class newStudent(BaseModel):
    name:str
    age:int
    clg:str

students={
    1:{
        "name":"Aaron",
        "age":"19",
        "clg":"BTech"
    },
    2:{
        "name":"John",
        "age":"90",
        "clg":"BCA"
    }
}
@app.get("/")
def home():
    return {"msg":"hello World"}

@app.get("/students/{student_id}")
def getStudents(student_id:int=Path(...,description="ID of student")):
    return students[student_id]

@app.get("/studentName")
def getStudentID(*,studentName:Optional[str]=None,age:str):
    for student in students:
        if(students[student]["age"]==age):
            return{"This is the student that we were looking for"}
    return {"Data":"Not Found"}

@app.post("/newStudent/{student_id}")
def newStudent(student_id:int,student:newStudent):
    if student_id in students:
        return {"Message":"Student Already Exists"}
    students[student_id]=student
    return student