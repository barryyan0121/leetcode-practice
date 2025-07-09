#
# @lc app=leetcode.cn id=498 lang=python3
# @lcpr version=30201
#
# [498] 对角线遍历
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            if i % 2:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            else:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4]]\n
# @lcpr case=end

#
