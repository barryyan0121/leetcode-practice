#
# @lc app=leetcode.cn id=185 lang=python3
# @lcpr version=30203
#
# [185] 部门工资前三高的所有员工
#

import sys
import os
import sqlite3

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def departmentTopThreeSalaries(self) -> str:
        return """
SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.DepartmentId = e.DepartmentId AND e2.Salary > e.Salary
)
ORDER BY d.Name, e.Salary DESC, e.Name
"""


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def run_query(
        departments: List[Tuple[int, str]],
        employees: List[Tuple[int, str, int, int]],
    ) -> List[Tuple[str, str, int]]:
        conn = sqlite3.connect(":memory:")
        cur = conn.cursor()
        cur.execute("CREATE TABLE Department (Id INTEGER, Name TEXT)")
        cur.execute(
            "CREATE TABLE Employee (Id INTEGER, Name TEXT, Salary INTEGER, DepartmentId INTEGER)"
        )
        cur.executemany("INSERT INTO Department (Id, Name) VALUES (?, ?)", departments)
        cur.executemany(
            "INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES (?, ?, ?, ?)",
            employees,
        )
        rows = cur.execute(solution.departmentTopThreeSalaries()).fetchall()
        conn.close()
        return rows

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_query,
            [
                [(1, "IT"), (2, "Sales")],
                [
                    (1, "Joe", 70000, 1),
                    (2, "Jim", 90000, 1),
                    (3, "Henry", 80000, 2),
                    (4, "Sam", 60000, 2),
                    (5, "Max", 90000, 1),
                    (6, "Jack", 85000, 1),
                    (7, "Tom", 90000, 2),
                    (8, "Lucy", 70000, 2),
                ],
            ],
            [
                ("IT", "Jim", 90000),
                ("IT", "Max", 90000),
                ("IT", "Jack", 85000),
                ("IT", "Joe", 70000),
                ("Sales", "Tom", 90000),
                ("Sales", "Henry", 80000),
                ("Sales", "Lucy", 70000),
            ],
        ),
        (
            run_query,
            [
                [(1, "A")],
                [(1, "X", 1, 1), (2, "Y", 2, 1), (3, "Z", 3, 1), (4, "W", 4, 1)],
            ],
            [("A", "W", 4), ("A", "Z", 3), ("A", "Y", 2)],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# Department\n1,IT\n2,Sales\n
# Employee\n1,Joe,70000,1\n2,Jim,90000,1\n3,Henry,80000,2\n4,Sam,60000,2\n5,Max,90000,1\n
# @lcpr case=end

#
