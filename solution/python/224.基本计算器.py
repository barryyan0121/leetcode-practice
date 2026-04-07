#
# @lc app=leetcode.cn id=224 lang=python3
# @lcpr version=30203
#
# [224] 基本计算器
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        sign = 1
        stack = [1]

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char in "+-":
                result += sign * number
                sign = stack[-1] * (1 if char == "+" else -1)
                number = 0
            elif char == "(":
                stack.append(sign)
            elif char == ")":
                result += sign * number
                number = 0
                stack.pop()
                sign = stack[-1]

        result += sign * number
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.calculate, ("1 + 1",), 2),
        (solution.calculate, (" 2-1 + 2 ",), 3),
        (solution.calculate, ("(1+(4+5+2)-3)+(6+8)",), 23),
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
# "1 + 1"\n
# @lcpr case=end
