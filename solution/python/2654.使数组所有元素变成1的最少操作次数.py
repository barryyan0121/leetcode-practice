#
# @lc app=leetcode.cn id=2654 lang=python3
# @lcpr version=30203
#
# [2654] 使数组所有元素变成 1 的最少操作次数
#

import math
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones:
            return len(nums) - ones

        if math.gcd(*nums) != 1:
            return -1

        shortest = len(nums)
        for start in range(len(nums)):
            current = 0
            for end in range(start, len(nums)):
                current = math.gcd(current, nums[end])
                if current == 1:
                    shortest = min(shortest, end - start + 1)
                    break
        return len(nums) + shortest - 2


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.minOperations([2, 6, 3, 4]) == 4
    assert solution.minOperations([2, 10, 6, 14]) == -1
    assert solution.minOperations([1, 2, 3]) == 2
    print("测试用例通过")
