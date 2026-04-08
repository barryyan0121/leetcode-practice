#
# @lc app=leetcode.cn id=518 lang=python3
# @lcpr version=30203
#
# [518] 零钱兑换 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for current in range(coin, amount + 1):
                dp[current] += dp[current - coin]
        return dp[amount]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (solution.change, (5, [1, 2, 5]), 4),
        (solution.change, (3, [2]), 0),
        (solution.change, (10, [10]), 1),
        (solution.change, (0, [1, 2, 5]), 1),
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
# 5\n[1,2,5]\n
# @lcpr case=end
#
