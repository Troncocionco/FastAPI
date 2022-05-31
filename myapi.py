from fastapi import FastAPI, Path

""" reate an endpoint for API connectivity
This end will provide a reference point for our requests:
GET
POST
UPDATE
DELETE  """
app = FastAPI()


students = {
    1: {
        "name": "john",
        "age": 18,
        "class": "year 12"
    }
}

#Specify the URL for the API method
@app.get("/index")
def home():
    return {"name": "Caccola"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The I



D of the student you want to view", gt=0)):
    return students[student_id]



