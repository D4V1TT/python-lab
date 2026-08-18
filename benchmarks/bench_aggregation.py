import timeit
from python_lab.aggregates import salary_stats_by_depts
from python_lab.data import make_employees
from python_lab.naive import salary_stats_by_depts as salary_naive

def bench(fn, rows, number=3):
    return min(timeit.repeat(lambda: fn(rows), number=number, repeat=3)) / number

if __name__ == "__main__":
    print(f"{'rows':>8} | {'naive O(n^2)':>14} | {'grouped O(n)':>13} | {'speedup':>8}")
    for n in (100, 500, 1_000, 5_000, 10_000):
        rows = make_employees(n)
        naive = bench(salary_naive, rows)
        fast = bench(salary_stats_by_depts, rows)
        print(f"{n:>8} | {naive:>13.4f}s | {fast:>12.4f}s | {naive/fast:>7.0f}x")