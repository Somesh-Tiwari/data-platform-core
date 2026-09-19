#weekend of week 1: FastAPI

from fastapi import FastAPI, Path  
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = { 
    1: {"name": "John", "age": 20, "major": "Computer Science"},
    2: {"name": "Jane", "age": 22, "major": "Mathematics"},
}

class Student(BaseModel):
    name: str
    age: int
    major: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    major: Optional[str] = None


@app.get("/")
def index():
    return {"message": "Hello World"}

#The Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "student-api"}

#path parameter
@app.get("/get-students/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student to retrieve", gt=0, lt=5)):
    return students[student_id]

#query parameter
# Combined: Path parameter for ID, Query parameter for optional name filtering
@app.get("/get-student-details/{student_id}")
def get_student_combined(student_id: int, name: Optional[str] = None):
    # 1. Check if the ID even exists in our database first
    if student_id not in students:
        return {"Error": "Student ID not found"}
    
    student_data = students[student_id]
    
    # 2. If the user also provided a name, let's verify it matches for extra security/filtering
    if name and student_data["name"].lower() != name.lower():
        return {"Error": "The provided name does not match this student ID"}
        
    # 3. If ID exists (and name matches if provided), return the student
    return student_data


#post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student ID already exists"}

    students[student_id] = student.model_dump() 

    """model_dump() is a method provided by Pydantic's BaseModel that returns the model's data as a dictionary. 
    This is useful for converting the Pydantic model instance into a format that can be easily stored or manipulated, 
    such as when adding it to a dictionary of students."""

    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student ID does not exist"}

    # Update only the fields that are provided in the request
    update_data = student.model_dump(exclude_unset=True)  # Get only the fields that were provided
    students[student_id].update(update_data)

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student ID does not exist"}

    deleted_student = students.pop(student_id)
    return {"message": f"Student with ID {student_id} has been deleted", "deleted_student": deleted_student}