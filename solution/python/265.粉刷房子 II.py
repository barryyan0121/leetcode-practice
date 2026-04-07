#
# @lc app=leetcode.cn id=265 lang=python3
# @lcpr version=30203
#
# [265] 粉刷房子 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        prev_min = prev_second = 0
        prev_color = -1

        for row in costs:
            curr_min = curr_second = float("inf")
            curr_color = -1
            for color, cost in enumerate(row):
                total = cost + (prev_second if color == prev_color else prev_min)
                if total < curr_min:
                    curr_second = curr_min
                    curr_min = total
                    curr_color = color
                elif total < curr_second:
                    curr_second = total
            prev_min, prev_second, prev_color = curr_min, curr_second, curr_color

        return prev_min


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minCostII, ([[1, 5, 3], [2, 9, 4]],), 5),
        (solution.minCostII, ([[1, 3], [2, 4]],), 5),
        (solution.minCostII, ([],), 0),
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
# [[1,5,3],[2,9,4]]\n
# @lcpr case=end
