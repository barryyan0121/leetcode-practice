#
# @lc app=leetcode.cn id=1751 lang=python3
# @lcpr version=30201
#
# [1751] 最多可以参加的会议数目 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x: x[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i, (start, end, val) in enumerate(events):
            p = bisect_left(events, start, hi = n - 1, key=lambda e: e[1])
            for j in range(1, k + 1):
                dp[i + 1][j] = max(dp[i][j], dp[p][j - 1] + events[i][2])

        return dp[n][k]

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [[1,2,4],[3,4,3],[2,3,1]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,4],[3,4,3],[2,3,10]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]\n3\n
# @lcpr case=end

#

