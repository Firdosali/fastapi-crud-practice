from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    id: int
    name: str
    department: str
    salary: float