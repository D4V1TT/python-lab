from typing import Iterable
from python_lab.models import Employee, Department
from python_lab.aggregates import group_by, salary_stats_by_depts

def high_earners(emps: list[Employee], threshold: int) -> list:
    """return names of employees, who earn more than threshold"""
    return [emp["name"] for emp in emps if emp["salary"] > threshold]


def sort_by(emps: list[Employee], key: str, *, desc: bool = False) -> list:
    """return sorted list of employees based on criteria(key=dept,name,salary...)"""
    return sorted(emps, key=lambda row: row[key], reverse=desc)


def distinct_depts(emps: list[Employee]) -> list:
    """return every distinct department"""
    return sorted({emp["dept"] for emp in emps})


def inner_join(emps: list[Employee], depts: list[Department], on: str = "dept") -> list:
    """eturn new list containing full department info only for employees, where we have department info"""
    index = {dept[on]: dept for dept in depts}

    return [emp | index[emp[on]] for emp in emps if emp[on] in index]


def left_join(emps: list[Employee], depts: list[Department], on: str = "dept") -> list[Employee]:
    """return new list containing full department info for all employees"""
    index = {dept[on]: dept for dept in depts}

    null_row = {k: None for d in depts for k in d if on != k}

    return [emp | null_row | index.get(emp[on], {}) for emp in emps]

def sort_and_rank(obj: Iterable, key: str, *, desc: bool = True) -> list:
    ordered = sorted(obj, key=lambda row: row[key], reverse=desc)

    ranked = []
    rank = 0
    prev = object()

    for row in ordered:
        if row[key] != prev:
            rank += 1
            prev = row[key]

        ranked.append(row | {"rank": rank})

    return ranked

def rank_in_dept(emps: list[Employee]) -> list:
    """return employee rank in department by salary"""
    return [
        row
        for group in group_by(emps, "dept").values()
        for row in sort_and_rank(group, "salary")
    ]

def dept_salary_pct(emps: list[Employee]) -> list:
    """return each employee's salary as % of their dept total"""
    stats = salary_stats_by_depts(emps)

    return [
        emp
        | {
            "dept_salary_pct": round(
                emp["salary"] / stats[emp["dept"]]["total"] * 100, 2
            )
        }
        for emp in emps
    ]

def self_join_managers(emps: list[Employee]) -> list:
    """return employee info alongside their manager if available(inner join)"""
    man_emps = {emp["emp_id"]: emp for emp in emps}

    return [
        {"employee": emp, "manager": man_emps.get(emp["manager_id"])}
        for emp in emps
        if emp["manager_id"] is not None
    ]