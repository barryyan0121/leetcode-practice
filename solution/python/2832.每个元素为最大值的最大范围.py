#
# @lc app=leetcode.cn id=2832 lang=python3
# @lcpr version=30203
#
# [2832] 每个元素为最大值的最大范围
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [-1] * n
        stack = []
        for index, value in enumerate(nums):
            while stack and nums[stack[-1]] < value:
                stack.pop()
            left[index] = stack[-1] if stack else -1
            stack.append(index)

        right = [n] * n
        stack = []
        for index in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[index]:
                stack.pop()
            right[index] = stack[-1] if stack else n
            stack.append(index)
        return [right[index] - left[index] - 1 for index in range(n)]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumLengthOfRanges([1, 5, 4, 3, 6]) == [1, 4, 2, 1, 5]
    assert solution.maximumLengthOfRanges([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    print("测试用例通过")
