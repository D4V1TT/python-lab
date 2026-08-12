from collections import defaultdict
from datetime import datetime

EMPLOYEES = [
    {
        "emp_id": 1,
        "name": "Nino",
        "dept": "IT",
        "salary": 4200,
        "hired": "2021-03-01",
        "manager_id": None,
    },
    {
        "emp_id": 2,
        "name": "Giorgi",
        "dept": "IT",
        "salary": 3800,
        "hired": "2022-07-15",
        "manager_id": 1,
    },
    {
        "emp_id": 3,
        "name": "Ana",
        "dept": "Finance",
        "salary": 5100,
        "hired": "2020-01-20",
        "manager_id": None,
    },
    {
        "emp_id": 4,
        "name": "Luka",
        "dept": "Finance",
        "salary": 2900,
        "hired": "2023-05-10",
        "manager_id": 3,
    },
    {
        "emp_id": 5,
        "name": "Mari",
        "dept": "IT",
        "salary": 6100,
        "hired": "2019-11-05",
        "manager_id": 1,
    },
    {
        "emp_id": 6,
        "name": "Dato",
        "dept": "Sales",
        "salary": 3300,
        "hired": "2023-09-01",
        "manager_id": None,
    },
    {
        "emp_id": 7,
        "name": "Salome",
        "dept": "Sales",
        "salary": 3300,
        "hired": "2024-02-14",
        "manager_id": 6,
    },
]

DEPARTMENTS = [
    {"dept": "IT", "location": "Tbilisi", "budget": 200000},
    {"dept": "Finance", "location": "Batumi", "budget": 150000},
    {"dept": "HR", "location": "Kutaisi", "budget": 80000},
]


def high_earners(emps, threshold):
    """return names of employees, who earn more than threshold"""
    return [emp["name"] for emp in emps if emp["salary"] > threshold]


def sort_by(emps, key, desc=False):
    """return sorted list of employees based on criteria(key=dept,name,salary...)"""
    return sorted(emps, key=lambda row: row[key], reverse=desc)


def distinct_depts(emps):
    """return every distinct department"""
    return sorted({emp["dept"] for emp in emps})


def group_by(rows, key):
    """return employees grouped by key(departments, name ...)"""
    key_func = key if callable(key) else lambda row: row[key]

    groups = defaultdict(list)
    for row in rows:
        groups[key_func(row)].append(row)

    return dict(groups)


def count_by_depts(emps):
    """return number of employees for every department"""
    return {dept: len(row) for dept, row in group_by(emps, "dept").items()}


def salary_stats_by_depts(emps):
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


def depts_over(emps, n):
    # return departments where average salary is higher then n
    return sorted(
        [dept for dept, s in salary_stats_by_depts(emps).items() if s["average"] > n]
    )


"""def count_by_depts(emps):
    return {emp["dept"] : len([em for em in emps if em["dept"] == emp["dept"]]) for emp in emps}

def salary_stats_by_depts(emps):
    return {emp["dept"] : {"count":  len([x for x in emps if x["dept"] == emp["dept"]]), "total": sum([x["salary"] for x in emps if x["dept"] == emp["dept"]]), "avg":sum([x["salary"] for x in emps if x["dept"] == emp["dept"]])/len([x for x in emps if x["dept"] == emp["dept"]]), "max": max([x["salary"] for x in emps if x["dept"] == emp["dept"]])} for emp in emps}

def depts_over(emps, n):
    return sorted(set([emp["dept"] for emp in emps if sum([x["salary"] for x in emps if x["dept"] == emp["dept"]])/len([x for x in emps if x["dept"] == emp["dept"]]) > n]))
"""


def inner_join(emps, depts, on="dept"):
    """eturn new list containing full department info only for employees, where we have department info"""
    index = {dept[on]: dept for dept in depts}
    return [emp | index[emp[on]] for emp in emps if emp[on] in index]


def left_join(emps, depts, on="dept"):
    """return new list containing full department info for all employees"""
    index = {dept[on]: dept for dept in depts}
    null_row = {k: None for d in depts for k in d if on != k}
    return [emp | null_row | index.get(emp[on], {}) for emp in emps]


def dept_salary_pct(emps):
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


def sort_and_rank(obj, key, desc=True):
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


def rank_in_dept(emps):
    """return employee rank in department by salary"""
    return [
        row
        for group in group_by(emps, "dept").values()
        for row in sort_and_rank(group, "salary")
    ]


def self_join_managers(emps):
    """return employee info alongside their manager if available(inner join)"""
    man_emps = {emp["emp_id"]: emp for emp in emps}
    return [
        {"employee": emp, "manager": man_emps.get(emp["manager_id"])}
        for emp in emps
        if emp["manager_id"] is not None
    ]


def hires_by_year(emps):
    """return hire count by year"""
    groups = group_by(
        emps, lambda row: datetime.strptime(row["hired"], "%Y-%m-%d").year
    )
    return dict(sorted((year, len(rows)) for year, rows in groups.items()))


if __name__ == "__main__":
    print(high_earners(EMPLOYEES, 4000))
    print(sort_by(EMPLOYEES, "name"))
    print(distinct_depts(EMPLOYEES))
    print(count_by_depts(EMPLOYEES))
    print(salary_stats_by_depts(EMPLOYEES))
    print(depts_over(EMPLOYEES, 4500))
    print(inner_join(EMPLOYEES, DEPARTMENTS))
    print(left_join(EMPLOYEES, DEPARTMENTS))
    print(dept_salary_pct(EMPLOYEES))
    print(rank_in_dept(EMPLOYEES))
    print(self_join_managers(EMPLOYEES))
    print(hires_by_year(EMPLOYEES))
