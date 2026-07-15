#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

import os
import sys

from typing import *


class Employee:
    def __init__(self, employee_id: int, importance: int, subordinates: List[int]):
        self.id = employee_id
        self.importance = importance
        self.subordinates = subordinates


# @lc code=start
class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        by_id = {employee.id: employee for employee in employees}

        def total(employee_id: int) -> int:
            employee = by_id[employee_id]
            return employee.importance + sum(
                total(child) for child in employee.subordinates
            )

        return total(id)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.getImportance,
            ([Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])], 1),
            11,
        ),
        (solution.getImportance, ([Employee(1, 2, [5]), Employee(5, -3, [])], 5), -3),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
