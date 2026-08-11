#
# @lc app=leetcode.cn id=2297 lang=python3
# @lcpr version=30203
#
# [2297] 跳跃游戏 VIII
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        dp = [0] + [float("inf")] * (len(nums) - 1)
        increasing, decreasing = [], []
        for i, value in enumerate(nums):
            while increasing and nums[increasing[-1]] <= value:
                dp[i] = min(dp[i], dp[increasing.pop()] + costs[i])
            increasing.append(i)
            while decreasing and nums[decreasing[-1]] > value:
                dp[i] = min(dp[i], dp[decreasing.pop()] + costs[i])
            decreasing.append(i)
        return dp[-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minCost, ([3, 2, 4, 4, 1], [3, 7, 6, 4, 2]), 8),
        (solution.minCost, ([0, 1, 2], [1, 1, 1]), 2),
    ]

    for idx, (func, args, expected) in enumerate(test_cases, 1):
        result = func(*args)
        assert result == expected, (idx, result, expected)
        print(f"测试用例 {idx} 通过: result = {result}")
