from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, Employee
from schemas import EmployeeCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.post("/employees")
def create_employee(employee: EmployeeCreate):

    db = SessionLocal()

    new_employee = Employee(
        id=employee.id,
        name=employee.name,
        department=employee.department,
        salary=employee.salary
    )

    db.add(new_employee)
    db.commit()

    return {"message": "Employee Added"}
@app.get("/employees")
def get_employees():

    db = SessionLocal()

    employees = db.query(Employee).all()

    return employees