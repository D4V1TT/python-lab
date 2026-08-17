from typing import TypedDict, NotRequired

class Employee(TypedDict):
    emp_id: int
    name: str
    dept: str
    salary: int
    hired: str
    manager_id: int | None
    rank: NotRequired[int]


class Department(TypedDict):
    dept: str
    location: str
    budget: int
