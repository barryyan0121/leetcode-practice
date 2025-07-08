#
# @lc app=leetcode.cn id=2294 lang=python3
# @lcpr version=30201
#
# [2294] 划分数组使最大差为 K
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        mn = -inf
        for i in nums:
            if i - mn > k:
                res += 1
                mn = i
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# [3,6,1,2,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,4,5]\n0\n
# @lcpr case=end

#
