from datetime import datetime
from typing import Iterable
from collections import defaultdict
from models import Employee

def group_by(rows: Iterable, key: str) -> dict:
    """return employees grouped by key(departments, name ...)"""
    key_func = key if callable(key) else lambda row: row[key]

    groups = defaultdict(list)

    for row in rows:
        groups[key_func(row)].append(row)

    return dict(groups)

def count_by_depts(emps: list[Employee]) -> dict:
    """return number of employees for every department"""
    return {dept: len(row) for dept, row in group_by(emps, "dept").items()}


def salary_stats_by_depts(emps: list[Employee]) -> dict:
    """return stats for every department"""
    stats = {}

    for dept, rows in group_by(emps, "dept").items():
        salaries = [row["salary"] for row in rows]

        stats[dept] = {
            "count": len(salaries),
            "total": sum(salaries),
            "average": sum(salaries) / len(salaries),
            "max": max(salaries),
        }

    return stats


def depts_over(emps: list[Employee], n: int) -> list:
    # return departments where average salary is higher then n
    return sorted(
        [dept for dept, s in salary_stats_by_depts(emps).items() if s["average"] > n]
    )

def hires_by_year(emps: list[Employee]) -> dict:
    """return hire count by year"""
    groups = group_by(
        emps, lambda row: datetime.strptime(row["hired"], "%Y-%m-%d").year
    )

    return dict(sorted((year, len(rows)) for year, rows in groups.items()))
