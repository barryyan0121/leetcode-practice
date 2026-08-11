#
# @lc app=leetcode.cn id=2323 lang=python3
# @lcpr version=30203
#
# [2323] 完成所有工作的最短时间 II
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        return max(
            (job + worker - 1) // worker
            for job, worker in zip(sorted(jobs), sorted(workers))
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumTime([5, 2, 4], [1, 7, 5]) == 2
    assert solution.minimumTime([3, 18, 15, 9], [6, 5, 1, 3]) == 3
    print("测试用例通过")
