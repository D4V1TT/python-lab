from models import Employee, Department

def count_by_depts(emps: list[Employee]) -> dict:
    return {
        emp["dept"]: len([
            em for em in emps
            if em["dept"] == emp["dept"]
        ])
        for emp in emps
    }


def salary_stats_by_depts(emps: list[Employee]) -> dict:
    return {
        emp["dept"]: {
            "count": len([
                x for x in emps
                if x["dept"] == emp["dept"]
            ]),
            "total": sum([
                x["salary"] for x in emps
                if x["dept"] == emp["dept"]
            ]),
            "avg": sum([
                x["salary"] for x in emps
                if x["dept"] == emp["dept"]
            ]) / len([
                x for x in emps
                if x["dept"] == emp["dept"]
            ]),
            "max": max([
                x["salary"] for x in emps
                if x["dept"] == emp["dept"]
            ])
        }
        for emp in emps
    }


def depts_over(emps: list[Employee], n: int) -> list:
    return sorted(set([
        emp["dept"]
        for emp in emps
        if sum([
            x["salary"] for x in emps
            if x["dept"] == emp["dept"]
        ]) / len([
            x for x in emps
            if x["dept"] == emp["dept"]
        ]) > n
    ]))