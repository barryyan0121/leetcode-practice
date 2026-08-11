#
# @lc app=leetcode.cn id=2463 lang=python3
# @lcpr version=30203
#
# [2463] 最小移动总距离
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        dp = [0] + [float("inf")] * len(robot)
        for position, limit in sorted(factory):
            next_dp = [float("inf")] * (len(robot) + 1)
            for assigned, current in enumerate(dp):
                if current == float("inf"):
                    continue
                distance = 0
                for count in range(min(limit, len(robot) - assigned) + 1):
                    next_dp[assigned + count] = min(
                        next_dp[assigned + count], current + distance
                    )
                    if assigned + count < len(robot):
                        distance += abs(robot[assigned + count] - position)
            dp = next_dp
        return dp[-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumTotalDistance([0, 4, 6], [[2, 2], [6, 2]]) == 4
    assert solution.minimumTotalDistance([1, -1], [[-2, 1], [2, 1]]) == 2
    print("测试用例通过")
