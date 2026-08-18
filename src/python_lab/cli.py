import argparse
import json

from python_lab.aggregates import depts_over, salary_stats_by_depts
from python_lab.data import EMPLOYEES

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query the employee dataset.")
    sub = parser.add_subparsers(dest="command", required=True)

    stats = sub.add_parser("stats", help="Salary statistics per department")
    stats.add_argument("--dept", help="Filter to one department")
    stats.add_argument("--json", action="store_true", help="Emit JSON")

    over = sub.add_parser("depts-over", help="Departments above an average salary")
    over.add_argument("threshold", type=int)

    args = parser.parse_args(argv)
    ...
    return 0

if __name__ == "__main__":
    raise SystemExit(main())