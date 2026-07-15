#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#

import os
import sys
from functools import cache


# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        servings = (n + 24) // 25

        @cache
        def probability(first: int, second: int) -> float:
            if first <= 0 and second <= 0:
                return 0.5
            if first <= 0:
                return 1.0
            if second <= 0:
                return 0.0
            return 0.25 * (
                probability(first - 4, second)
                + probability(first - 3, second - 1)
                + probability(first - 2, second - 2)
                + probability(first - 1, second - 3)
            )

        return probability(servings, servings)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.soupServings, (50,), 0.625),
        (solution.soupServings, (100,), 0.71875),
        (solution.soupServings, (5000,), 1.0),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert abs(result - expected) < 1e-8
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
