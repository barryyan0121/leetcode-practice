#
# @lc app=leetcode.cn id=569 lang=python3
# @lcpr version=30203
#
# [569] 员工薪水中位数
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def medianEmployeeSalary(
        self, employee: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        grouped: Dict[str, List[Dict[str, Any]]] = {}
        for row in employee:
            grouped.setdefault(row["company"], []).append(row)

        result: List[Dict[str, Any]] = []
        for company in sorted(grouped):
            rows = sorted(grouped[company], key=lambda row: (row["salary"], row["id"]))
            n = len(rows)
            if n % 2 == 1:
                mids = [n // 2]
            else:
                mids = [n // 2 - 1, n // 2]
            for idx in mids:
                result.append(
                    {
                        "id": rows[idx]["id"],
                        "company": rows[idx]["company"],
                        "salary": rows[idx]["salary"],
                    }
                )

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.medianEmployeeSalary,
            (
                [
                    {"id": 1, "company": "A", "salary": 2341},
                    {"id": 2, "company": "A", "salary": 341},
                    {"id": 3, "company": "A", "salary": 15},
                    {"id": 4, "company": "A", "salary": 15314},
                    {"id": 5, "company": "A", "salary": 451},
                    {"id": 6, "company": "A", "salary": 513},
                    {"id": 7, "company": "B", "salary": 15},
                    {"id": 8, "company": "B", "salary": 13},
                    {"id": 9, "company": "B", "salary": 1154},
                    {"id": 10, "company": "B", "salary": 1345},
                    {"id": 11, "company": "B", "salary": 1221},
                    {"id": 12, "company": "B", "salary": 234},
                    {"id": 13, "company": "C", "salary": 2345},
                    {"id": 14, "company": "C", "salary": 2645},
                    {"id": 15, "company": "C", "salary": 2645},
                    {"id": 16, "company": "C", "salary": 2652},
                    {"id": 17, "company": "C", "salary": 65},
                ],
            ),
            [
                {"id": 5, "company": "A", "salary": 451},
                {"id": 6, "company": "A", "salary": 513},
                {"id": 12, "company": "B", "salary": 234},
                {"id": 9, "company": "B", "salary": 1154},
                {"id": 14, "company": "C", "salary": 2645},
            ],
        ),
        (
            solution.medianEmployeeSalary,
            (
                [
                    {"id": 1, "company": "X", "salary": 100},
                    {"id": 2, "company": "X", "salary": 100},
                    {"id": 3, "company": "X", "salary": 200},
                    {"id": 4, "company": "Y", "salary": 50},
                    {"id": 5, "company": "Y", "salary": 60},
                ],
            ),
            [
                {"id": 2, "company": "X", "salary": 100},
                {"id": 4, "company": "Y", "salary": 50},
                {"id": 5, "company": "Y", "salary": 60},
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


#
# @lcpr case=start
# Employee = Employee table\n
# @lcpr case=end
#
