#
# @lc app=leetcode.cn id=3169 lang=python3
# @lcpr version=30201
#
# [3169] 无需开会的工作日
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        l, r = 1, 0
        for m in meetings:
            if m[0] > r:
                days -= r - l + 1
                l = m[0]
            r = max(r, m[1])
        days -= r - l + 1
        return days


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    meetings = [[5, 7], [1, 3], [9, 10]]
    days = 10
    result = solution.countDays(days, meetings)
    # your test code here


#
# @lcpr case=start
# 10\n[[5,7],[1,3],[9,10]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[2,4],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[1,6]]\n
# @lcpr case=end

#
