#
# @lc app=leetcode.cn id=375 lang=python3
# @lcpr version=30201
#
# [375] 猜数字大小 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = j + f[i][j - 1]
                for k in range (i, j):
                    f[i][j] = min(f[i][j], k + max(f[i][k - 1], f[k + 1][j]))
        return f[1][n]

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

