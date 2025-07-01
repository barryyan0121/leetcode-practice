#
# @lc app=leetcode.cn id=594 lang=python3
# @lcpr version=30201
#
# [594] 最长和谐子序列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from collections import Counter

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for key in counter:
            if key + 1 in counter:
                res = max(res, counter[key] + counter[key + 1])
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    res = solution.findLHS(nums)
    print(res)
    # your test code here


#
# @lcpr case=start
# [1,3,2,2,5,2,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#
