#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for price in prices[1:]:
            cash, hold = max(cash, hold + price - fee), max(hold, cash - price)
        return cash


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxProfit, ([1, 3, 2, 8, 4, 9], 2), 8),
        (solution.maxProfit, ([1, 3, 7, 5, 10, 3], 3), 6),
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
