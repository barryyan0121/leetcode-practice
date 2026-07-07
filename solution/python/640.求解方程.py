#
# @lc app=leetcode.cn id=640 lang=python3
# @lcpr version=30203
#
# [640] 求解方程
#

import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr: str) -> Tuple[int, int]:
            x_coef = const = 0
            for token in re.findall(r"[+-]?[^+-]+", expr):
                if token.endswith("x"):
                    num = token[:-1]
                    if num in ("", "+"):
                        x_coef += 1
                    elif num == "-":
                        x_coef -= 1
                    else:
                        x_coef += int(num)
                else:
                    const += int(token)
            return x_coef, const

        left, right = equation.split("=")
        lx, lc = parse(left)
        rx, rc = parse(right)
        x_coef = lx - rx
        const = rc - lc
        if x_coef == 0:
            return "Infinite solutions" if const == 0 else "No solution"
        return f"x={const // x_coef}"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.solveEquation, ("x+5-3+x=6+x-2",), "x=2"),
        (solution.solveEquation, ("x=x",), "Infinite solutions"),
        (solution.solveEquation, ("2x=x",), "x=0"),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)

