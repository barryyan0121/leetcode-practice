#
# @lc app=leetcode.cn id=577 lang=python3
# @lcpr version=30203
#
# [577] 员工奖金
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def employeeBonus(
        self, employee: List[Dict[str, Any]], bonus: List[Dict[str, Any]]
    ) -> List[Dict[str, Optional[int]]]:
        bonus_map = {row["empId"]: row["bonus"] for row in bonus}
        result = []

        for row in employee:
            value = bonus_map.get(row["empId"])
            if value is None or value < 1000:
                result.append({"name": row["name"], "bonus": value})

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.employeeBonus,
            (
                [
                    {"empId": 1, "name": "John", "supervisor": 3, "salary": 1000},
                    {"empId": 2, "name": "Dan", "supervisor": 3, "salary": 2000},
                    {"empId": 3, "name": "Brad", "supervisor": None, "salary": 4000},
                    {"empId": 4, "name": "Thomas", "supervisor": 3, "salary": 4000},
                ],
                [
                    {"empId": 2, "bonus": 500},
                    {"empId": 4, "bonus": 2000},
                ],
            ),
            [
                {"name": "John", "bonus": None},
                {"name": "Dan", "bonus": 500},
                {"name": "Brad", "bonus": None},
            ],
        ),
        (
            solution.employeeBonus,
            (
                [
                    {"empId": 1, "name": "A", "supervisor": None, "salary": 1},
                    {"empId": 2, "name": "B", "supervisor": None, "salary": 1},
                ],
                [{"empId": 2, "bonus": 999}],
            ),
            [{"name": "A", "bonus": None}, {"name": "B", "bonus": 999}],
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
