#
# @lc app=leetcode.cn id=568 lang=python3
# @lcpr version=30203
#
# [568] 最大休假天数
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        weeks = len(days[0]) if days else 0
        dp = [-(10**9)] * n
        dp[0] = 0

        for week in range(weeks):
            next_dp = [-(10**9)] * n
            for city in range(n):
                if dp[city] < 0:
                    continue
                for nxt in range(n):
                    if city == nxt or flights[city][nxt]:
                        next_dp[nxt] = max(next_dp[nxt], dp[city] + days[nxt][week])
            dp = next_dp

        return max(dp) if dp else 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.maxVacationDays,
            (
                [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                [[1, 3, 1], [6, 0, 3], [3, 3, 3]],
            ),
            12,
        ),
        (
            solution.maxVacationDays,
            (
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[7, 1, 7], [6, 0, 3], [3, 3, 3]],
            ),
            15,
        ),
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
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]\n
# @lcpr case=end
#
