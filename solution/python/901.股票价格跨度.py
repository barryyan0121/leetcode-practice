#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#

import os
import sys


# @lc code=start
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# @lc code=end


def run_prices(prices):
    spanner = StockSpanner()
    return [spanner.next(price) for price in prices]


if __name__ == "__main__":
    test_cases = [
        (run_prices, ([100, 80, 60, 70, 60, 75, 85],), [1, 1, 1, 2, 1, 4, 6]),
        (run_prices, ([31, 41, 48, 59, 79],), [1, 2, 3, 4, 5]),
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
