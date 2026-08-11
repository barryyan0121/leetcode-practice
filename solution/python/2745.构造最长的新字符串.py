#
# @lc app=leetcode.cn id=2745 lang=python3
# @lcpr version=30203
#
# [2745] 构造最长的新字符串
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return 2 * (2 * min(x, y) + z + (x != y))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestString(2, 5, 1) == 12
    assert solution.longestString(3, 2, 2) == 14
    print("测试用例通过")
