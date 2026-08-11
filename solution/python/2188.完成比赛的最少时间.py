#
# @lc app=leetcode.cn id=2188 lang=python3
# @lcpr version=30203
#
# [2188] 完成比赛的最少时间
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int
    ) -> int:
        limit = changeTime + min(f for f, _ in tires)
        best = [float("inf")] * (numLaps + 1)
        for first, ratio in tires:
            lap_time = first
            total = 0
            for laps in range(1, numLaps + 1):
                if lap_time > limit:
                    break
                total += lap_time
                best[laps] = min(best[laps], total)
                lap_time *= ratio

        dp = [0] + [float("inf")] * numLaps
        for laps in range(1, numLaps + 1):
            for segment in range(1, laps + 1):
                dp[laps] = min(
                    dp[laps],
                    best[segment]
                    + (0 if segment == laps else changeTime + dp[laps - segment]),
                )
        return dp[numLaps]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minimumFinishTime, ([[2, 3], [3, 4]], 5, 4), 21),
        (solution.minimumFinishTime, ([[1, 10], [2, 2], [3, 4]], 6, 5), 25),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
    sys.exit(1)
