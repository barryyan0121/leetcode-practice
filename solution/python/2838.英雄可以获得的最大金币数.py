#
# @lc app=leetcode.cn id=2838 lang=python3
# @lcpr version=30203
#
# [2838] 英雄可以获得的最大金币数
#

import bisect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maximumCoins(
        self, heroes: List[int], monsters: List[int], coins: List[int]
    ) -> List[int]:
        ordered = sorted(zip(monsters, coins))
        strengths = [monster for monster, _ in ordered]
        prefix = [0]
        for _, coin in ordered:
            prefix.append(prefix[-1] + coin)
        return [prefix[bisect.bisect_right(strengths, hero)] for hero in heroes]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumCoins([1, 4, 2], [1, 1, 5, 2, 3], [2, 3, 4, 5, 6]) == [
        5,
        16,
        10,
    ]
    assert solution.maximumCoins([5], [2, 3, 1, 2], [10, 6, 5, 2]) == [23]
    print("测试用例通过")
