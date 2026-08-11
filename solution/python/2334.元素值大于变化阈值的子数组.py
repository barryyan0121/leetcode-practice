#
# @lc app=leetcode.cn id=2334 lang=python3
# @lcpr version=30203
#
# [2334] 元素值大于变化阈值的子数组
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        stack = []
        for right, value in enumerate(nums + [0]):
            while stack and nums[stack[-1]] >= value:
                index = stack.pop()
                left = stack[-1] + 1 if stack else 0
                width = right - left
                if nums[index] * width > threshold:
                    return width
            stack.append(right)
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.validSubarraySize([1, 3, 4, 3, 1], 6) == 3
    assert solution.validSubarraySize([6, 5, 6, 5, 8], 7) == 3
    assert solution.validSubarraySize([1, 1, 1, 1], 10) == -1
    print("测试用例通过")
