#
# @lc app=leetcode.cn id=964 lang=python3
#
# [964] 表示数字的最少运算符
#

import os
import sys
from functools import cache


# @lc code=start
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @cache
        def solve(value):
            if value < x:
                return min(2 * value - 1, 2 * (x - value))
            power = x
            exponent = 1
            while power * x <= value:
                power *= x
                exponent += 1
            if power == value:
                return exponent - 1
            answer = exponent + solve(value - power)
            if power * x - value < value:
                answer = min(answer, exponent + 1 + solve(power * x - value))
            return answer

        return solve(target)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.leastOpsExpressTarget, (3, 19), 5),
        (solution.leastOpsExpressTarget, (5, 501), 8),
        (solution.leastOpsExpressTarget, (100, 100000000), 3),
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
