#
# @lc app=leetcode.cn id=227 lang=python3
# @lcpr version=30203
#
# [227] 基本计算器 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        sign = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    stack.append(stack.pop() * number)
                else:
                    stack.append(int(stack.pop() / number))
                sign = char
                number = 0

        return sum(stack)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.calculate, ("3+2*2",), 7),
        (solution.calculate, (" 3/2 ",), 1),
        (solution.calculate, (" 3+5 / 2 ",), 5),
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
# "3+2*2"\n
# @lcpr case=end
