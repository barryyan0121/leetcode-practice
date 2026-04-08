#
# @lc app=leetcode.cn id=579 lang=python3
# @lcpr version=30203
#
# [579] 查询员工的累计薪水
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def cumulativeSalary(self, employee: List[Dict[str, int]]) -> List[Dict[str, int]]:
        grouped: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for row in employee:
            grouped[row["Id"]].append((row["Month"], row["Salary"]))

        result = []
        for emp_id in sorted(grouped):
            rows = sorted(grouped[emp_id])
            for idx in range(len(rows) - 1):
                month = rows[idx][0]
                total = sum(salary for _, salary in rows[max(0, idx - 2) : idx + 1])
                result.append({"Id": emp_id, "Month": month, "Salary": total})

        result.sort(key=lambda row: (row["Id"], -row["Month"]))
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.cumulativeSalary,
            (
                [
                    {"Id": 1, "Month": 1, "Salary": 20},
                    {"Id": 2, "Month": 1, "Salary": 20},
                    {"Id": 1, "Month": 2, "Salary": 30},
                    {"Id": 2, "Month": 2, "Salary": 30},
                    {"Id": 3, "Month": 2, "Salary": 40},
                    {"Id": 1, "Month": 3, "Salary": 40},
                    {"Id": 3, "Month": 3, "Salary": 60},
                    {"Id": 1, "Month": 4, "Salary": 60},
                    {"Id": 3, "Month": 4, "Salary": 70},
                ],
            ),
            [
                {"Id": 1, "Month": 3, "Salary": 90},
                {"Id": 1, "Month": 2, "Salary": 50},
                {"Id": 1, "Month": 1, "Salary": 20},
                {"Id": 2, "Month": 1, "Salary": 20},
                {"Id": 3, "Month": 3, "Salary": 100},
                {"Id": 3, "Month": 2, "Salary": 40},
            ],
        ),
        (
            solution.cumulativeSalary,
            (
                [
                    {"Id": 7, "Month": 1, "Salary": 10},
                    {"Id": 7, "Month": 3, "Salary": 30},
                    {"Id": 7, "Month": 2, "Salary": 20},
                ],
            ),
            [
                {"Id": 7, "Month": 2, "Salary": 30},
                {"Id": 7, "Month": 1, "Salary": 10},
            ],
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
