#
# @lc app=leetcode.cn id=3443 lang=python3
# @lcpr version=30201
#
# [3443] K 次修改后的最大曼哈顿距离
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        latitude = 0
        longitude = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                latitude += 1
            elif s[i] == "S":
                latitude -= 1
            elif s[i] == "E":
                longitude += 1
            elif s[i] == "W":
                longitude -= 1
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# "NWSE"\n1\n
# @lcpr case=end

# @lcpr case=start
# "NSWWEW"\n3\n
# @lcpr case=end

#
