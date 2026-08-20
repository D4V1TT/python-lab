import datetime
from typing import TypedDict, NotRequired
from collections.abc import Callable
from typing import NamedTuple


def parse_date(value: object) -> datetime.date:
    return datetime.datetime.strptime(str(value), "%Y-%m-%d").date()

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

class FileReport(TypedDict):
    name: str
    stem: str
    suffix: str
    size_kb: float
    modified: str

class Field(NamedTuple):
    """One column's contract: name, how to coerce it, whether NULL is allowed."""
    name: str
    coerce: Callable[[object], object]
    nullable: bool = False

class Rejection(NamedTuple):
    line_no: int
    problems: list[str]
    row: dict

EMPLOYEE_SCHEMA = [
    Field("emp_id", int),
    Field("name", str),
    Field("dept", str),
    Field("salary", int),
    Field("hired", parse_date),
    Field("manager_id", int, nullable=True),
]

