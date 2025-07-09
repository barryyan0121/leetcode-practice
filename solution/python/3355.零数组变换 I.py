#
# @lc app=leetcode.cn id=3355 lang=python3
# @lcpr version=30201
#
# [3355] 零数组变换 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for start, end in queries:
            diff[start] += 1
            diff[end + 1] -= 1
        acc = accumulate(diff[:-1])
        for n, d in zip(nums, acc):
            if n > d:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    solution = Solution()


#
# @lcpr case=start
# [1,0,1]\n[[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n[[1,3],[0,2]]\n
# @lcpr case=end

#
