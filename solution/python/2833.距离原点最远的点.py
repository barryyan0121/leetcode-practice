#
# @lc app=leetcode.cn id=2833 lang=python3
# @lcpr version=30203
#
# [2833] 距离原点最远的点
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count("R") - moves.count("L")) + moves.count("_")


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.furthestDistanceFromOrigin("L_RL__R") == 3
    assert solution.furthestDistanceFromOrigin("_R__LL_") == 5
    assert solution.furthestDistanceFromOrigin("_______") == 7
    print("测试用例通过")
