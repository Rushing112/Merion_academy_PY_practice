from pydantic import BaseModel, EmailStr

#базовая схема (класс) EmployeeBase, наследник BaseModel:
class EmployeeBase(BaseModel):
    full_name: str
    email: EmailStr

#схема (класс) EmployeeCreate, наследник EmployeeBase
class EmployeeCreate(EmployeeBase):
    pass

#схема (класс) Employee, наследник EmployeeBase
class Employee(EmployeeBase):
    id: int
