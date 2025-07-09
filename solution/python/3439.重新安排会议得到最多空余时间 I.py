#
# @lc app=leetcode.cn id=3439 lang=python3
# @lcpr version=30201
#
# [3439] 重新安排会议得到最多空余时间 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        res = 0
        total = [0] * (n + 1)
        for i in range(n):
            total[i + 1] = total[i] + endTime[i] - startTime[i]
        for i in range(k - 1, n):
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            res = max(res, right - left - (total[i + 1] - total[i - k + 1]))
        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# 5\n1\n[1,3]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# 10\n1\n[0,2,9]\n[1,4,10]\n
# @lcpr case=end

# @lcpr case=start
# 5\n2\n[0,1,2,3,4]\n[1,2,3,4,5]\n
# @lcpr case=end

#
