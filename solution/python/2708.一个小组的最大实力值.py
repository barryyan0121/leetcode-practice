#
# @lc app=leetcode.cn id=2708 lang=python3
# @lcpr version=30203
#
# [2708] 一个小组的最大实力值
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        maximum = minimum = nums[0]
        for value in nums[1:]:
            candidates = (value, maximum, minimum, maximum * value, minimum * value)
            maximum, minimum = max(candidates), min(candidates)
        return maximum


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxStrength([3, -1, -5, 2, 5, -9]) == 1350
    assert solution.maxStrength([-4, -5, -4]) == 20
    print("测试用例通过")
