import random
from python_lab.models import Employee

def make_employees(n: int, seed: int = 42) -> list[Employee]:
    """Deterministic synthetic data for benchmarks and tests."""
    rng = random.Random(seed)
    depts = ["IT", "Finance", "Sales", "HR", "Ops"]
    return [
        {
            "emp_id": i,
            "name": f"emp_{i}",
            "dept": rng.choice(depts),
            "salary": rng.randrange(2000, 8000, 100),
            "hired": f"{rng.randint(2015, 2025)}-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}",
            "manager_id": rng.randint(1, max(1, i - 1)) if i > 1 else None,
        }
        for i in range(1, n + 1)
    ]


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