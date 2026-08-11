#
# @lc app=leetcode.cn id=2826 lang=python3
# @lcpr version=30203
#
# [2826] 将三个组排序
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        longest = [0, 0, 0]
        for value in nums:
            index = value - 1
            longest[index] = max(longest[: index + 1]) + 1
        return len(nums) - max(longest)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumOperations([2, 1, 3, 2, 1]) == 3
    assert solution.minimumOperations([1, 3, 2, 1, 3, 3]) == 2
    assert solution.minimumOperations([2, 2, 2, 2, 3, 3]) == 0
    print("测试用例通过")
