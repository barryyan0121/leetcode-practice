#
# @lc app=leetcode.cn id=570 lang=python3
# @lcpr version=30203
#
# [570] 至少有5名直接下属的经理
#

import os
import sys
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findManagersWithAtLeastFiveDirectReports(
        self, employee: List[Dict[str, Any]]
    ) -> List[Dict[str, str]]:
        report_count = defaultdict(int)
        name_by_id = {}
        for row in employee:
            name_by_id[row["id"]] = row["name"]
            manager_id = row.get("managerId")
            if manager_id is not None:
                report_count[manager_id] += 1

        result = []
        for manager_id in sorted(k for k, v in report_count.items() if v >= 5):
            result.append({"name": name_by_id[manager_id]})
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findManagersWithAtLeastFiveDirectReports,
            (
                [
                    {"id": 1, "name": "A", "department": "IT", "managerId": None},
                    {"id": 2, "name": "B", "department": "IT", "managerId": 1},
                    {"id": 3, "name": "C", "department": "IT", "managerId": 1},
                    {"id": 4, "name": "D", "department": "IT", "managerId": 1},
                    {"id": 5, "name": "E", "department": "IT", "managerId": 1},
                    {"id": 6, "name": "F", "department": "IT", "managerId": 1},
                    {"id": 7, "name": "G", "department": "HR", "managerId": 2},
                ],
            ),
            [{"name": "A"}],
        ),
        (
            solution.findManagersWithAtLeastFiveDirectReports,
            (
                [
                    {"id": 1, "name": "M1", "department": "IT", "managerId": None},
                    {"id": 2, "name": "M2", "department": "IT", "managerId": None},
                    {"id": 3, "name": "a", "department": "IT", "managerId": 1},
                    {"id": 4, "name": "b", "department": "IT", "managerId": 1},
                    {"id": 5, "name": "c", "department": "IT", "managerId": 1},
                    {"id": 6, "name": "d", "department": "IT", "managerId": 1},
                    {"id": 7, "name": "e", "department": "IT", "managerId": 1},
                    {"id": 8, "name": "f", "department": "IT", "managerId": 2},
                    {"id": 9, "name": "g", "department": "IT", "managerId": 2},
                    {"id": 10, "name": "h", "department": "IT", "managerId": 2},
                    {"id": 11, "name": "i", "department": "IT", "managerId": 2},
                    {"id": 12, "name": "j", "department": "IT", "managerId": 2},
                ],
            ),
            [{"name": "M1"}, {"name": "M2"}],
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
# Employee = Employee table\n
# @lcpr case=end
#
