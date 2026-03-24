#
# @lc app=leetcode.cn id=177 lang=python3
# @lcpr version=30203
#
# [177] 第 N 高的薪水
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def nthHighestSalary(self, employee: List[Dict[str, int]], n: int) -> Optional[int]:
        salaries = sorted({row["salary"] for row in employee}, reverse=True)
        if n > len(salaries):
            return None
        return salaries[n - 1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.nthHighestSalary,
            (
                [
                    {"id": 1, "salary": 100},
                    {"id": 2, "salary": 200},
                    {"id": 3, "salary": 300},
                ],
                2,
            ),
            200,
        ),
        (
            solution.nthHighestSalary,
            ([{"id": 1, "salary": 100}, {"id": 2, "salary": 100}], 2),
            None,
        ),
        (
            solution.nthHighestSalary,
            (
                [
                    {"id": 1, "salary": 100},
                    {"id": 2, "salary": 200},
                    {"id": 3, "salary": 300},
                ],
                1,
            ),
            300,
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
# employee = Employee table, n = 2\n
# @lcpr case=end
