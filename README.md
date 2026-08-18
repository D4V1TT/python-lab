# python-lab

A structured re-entry into Python, approached from two years of professional
PL/SQL and relational database work. Each exercise implements a SQL concept
in pure Python before reaching for a library, to build the mental model
rather than the muscle memory.

## Contents
- `src/python_lab/plsql_to_python.py` — GROUP BY, JOIN, and window functions from scratch

## Setup

##Results
    rows |   naive O(n^2) |  grouped O(n) |  speedup
     100 |        0.0014s |       0.0000s |      84x
     500 |        0.0404s |       0.0001s |     562x
    1000 |        0.1506s |       0.0001s |    1708x
    5000 |        4.0618s |       0.0005s |    8287x
   10000 |       20.8496s |       0.0040s |    5232x
