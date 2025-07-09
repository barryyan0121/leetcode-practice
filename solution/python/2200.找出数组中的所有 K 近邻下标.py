#
# @lc app=leetcode.cn id=2200 lang=python3
# @lcpr version=30201
#
# [2200] 找出数组中的所有 K 近邻下标
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_idx = []
        for i, num in enumerate(nums):
            if num == key:
                key_idx.append(i)

        result = []
        for i in range(len(nums)):
            for j in key_idx:
                if abs(i - j) <= k:
                    result.append(i)
                    break
        return result


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# [3,4,9,1,3,9,5]\n9\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n2\n2\n
# @lcpr case=end

#
