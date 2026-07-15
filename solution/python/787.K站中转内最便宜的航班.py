#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            next_prices = prices[:]
            for origin, destination, price in flights:
                next_prices[destination] = min(
                    next_prices[destination], prices[origin] + price
                )
            prices = next_prices
        return -1 if prices[dst] == float("inf") else int(prices[dst])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findCheapestPrice,
            (
                4,
                [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                0,
                3,
                1,
            ),
            700,
        ),
        (
            solution.findCheapestPrice,
            (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
            200,
        ),
        (
            solution.findCheapestPrice,
            (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
            500,
        ),
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
