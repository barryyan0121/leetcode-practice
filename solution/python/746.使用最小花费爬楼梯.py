#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        previous = current = 0
        for step in range(2, len(cost) + 1):
            previous, current = current, min(
                current + cost[step - 1], previous + cost[step - 2]
            )
        return current


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minCostClimbingStairs, ([10, 15, 20],), 15),
        (solution.minCostClimbingStairs, ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6),
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
