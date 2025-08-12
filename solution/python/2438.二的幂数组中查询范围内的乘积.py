#
# @lc app=leetcode.cn id=2438 lang=python3
# @lcpr version=30202
#
# [2438] 二的幂数组中查询范围内的乘积
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        bins, rep = [], 1
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            n //= 2
            rep *= 2

        m = len(bins)
        results = [[0] * m for _ in range(m)]
        for i in range(m):
            cur = 1
            for j in range(i, m):
                cur = cur * bins[j] % mod
                results[i][j] = cur

        ans = []
        for left, right in queries:
            ans.append(results[left][right])
        return ans
# @lc code=end
        pass

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 15\n[[0,1],[2,2],[0,3]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,0]]\n
# @lcpr case=end

#

