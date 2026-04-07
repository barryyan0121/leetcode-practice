#
# @lc app=leetcode.cn id=309 lang=python3
# @lcpr version=30203
#
# [309] 买卖股票的最佳时机含冷冻期
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_hold = hold
            hold = max(hold, rest - price)
            rest = max(rest, sold)
            sold = prev_hold + price

        return max(sold, rest)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxProfit, ([1, 2, 3, 0, 2],), 3),
        (solution.maxProfit, ([1],), 0),
        (solution.maxProfit, ([2, 1, 4],), 3),
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
# [1,2,3,0,2]\n
# @lcpr case=end
