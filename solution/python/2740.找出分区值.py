#
# @lc app=leetcode.cn id=2740 lang=python3
# @lcpr version=30203
#
# [2740] 找出分区值
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(right - left for left, right in zip(nums, nums[1:]))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.findValueOfPartition([1, 3, 2, 4]) == 1
    assert solution.findValueOfPartition([100, 1, 10]) == 9
    print("测试用例通过")
