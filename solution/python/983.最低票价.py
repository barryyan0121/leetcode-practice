#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = set(days)
        dp = [0] * (days[-1] + 1)
        for day in range(1, days[-1] + 1):
            if day not in travel:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2],
                )
        return dp[-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.mincostTickets, ([1, 4, 6, 7, 8, 20], [2, 7, 15]), 11),
        (
            solution.mincostTickets,
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]),
            17,
        ),
        (solution.mincostTickets, ([365], [2, 7, 15]), 2),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
