#
# @lc app=leetcode.cn id=2464 lang=python3
# @lcpr version=30203
#
# [2464] 有效分割中的最少子数组数目
#

import math
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for end in range(1, n + 1):
            for start in range(end):
                if math.gcd(nums[start], nums[end - 1]) > 1:
                    dp[end] = min(dp[end], dp[start] + 1)
        return -1 if dp[n] > n else dp[n]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.validSubarraySplit([2, 6, 3, 4, 3]) == 2
    assert solution.validSubarraySplit([3, 5]) == 2
    assert solution.validSubarraySplit([1, 2, 1]) == -1
    print("测试用例通过")
