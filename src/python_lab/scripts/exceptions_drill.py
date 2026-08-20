import datetime
from pathlib import Path
from python_lab.models import Employee, EMPLOYEE_SCHEMA, Rejection
from python_lab.errors import DataQualityError
from python_lab.data import make_employees

def read_text_safe(path: Path) -> str | None:
    try:
        with open(path, 'r', encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except PermissionError:
        print(f"Permission denied: {path}")
    except UnicodeDecodeError:
        print(f"Unicode error: {path} Can't read file")
    else:
        return text

def parse_employee_row(row: dict, line_no: int) -> dict:
    """Coerce one raw row to typed values. Raises DataQualityError listing ALL problems."""
    parsed: dict = {}
    problems: list[str] = []

    for field in EMPLOYEE_SCHEMA:
        if field.name not in row:
            problems.append(f"{field.name}: missing")
            continue

        raw = row[field.name]
        if raw is None or raw == "":
            if field.nullable:
                parsed[field.name] = None
            else:
                problems.append(f"{field.name}: null not allowed")
            continue

        try:
            parsed[field.name] = field.coerce(raw)
        except (ValueError, TypeError) as exc:
            problems.append(f"{field.name}: cannot coerce {raw!r} ({exc})")

    if problems:
        raise DataQualityError(line_no, problems)
    return parsed

def parse_all(rows: list[Employee], *, strict: bool = False)-> tuple[list[Employee], list[dict[Employee, tuple]]]:
    good_rows = []
    bad_rows = []

    for line_no, row in enumerate(rows, start=1):
        try:
            parse_employee_row(row, line_no)
        except DataQualityError as exc:
            bad_rows.append(Rejection(exc.line_no, exc.problems, row))
            if strict:
                raise
        else:
            good_rows.append(row)
    return good_rows, bad_rows

if __name__ == '__main__':
    print(read_text_safe(Path.home() / 'Downloads' / 'Untitled.png'))
    #print(parse_employee_row({"emp_id":10, "salary":"", "hired":"2020-12-12"}, 5))
    emp_list = make_employees(10)
    emp_list.append({"emp_id":10, "salary":15, "hired":"2020-22-12"})
    print(parse_all(emp_list))