#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        mod = 10**9 + 7
        plans = [[0] * (minProfit + 1) for _ in range(n + 1)]
        plans[0][0] = 1
        for members, earned in zip(group, profit):
            for used in range(n - members, -1, -1):
                for current_profit in range(minProfit, -1, -1):
                    next_profit = min(minProfit, current_profit + earned)
                    plans[used + members][next_profit] += plans[used][current_profit]
                    plans[used + members][next_profit] %= mod
        return sum(plans[used][minProfit] for used in range(n + 1)) % mod


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.profitableSchemes, (5, 3, [2, 2], [2, 3]), 2),
        (solution.profitableSchemes, (10, 5, [2, 3, 5], [6, 7, 8]), 7),
        (solution.profitableSchemes, (1, 0, [1], [0]), 2),
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
