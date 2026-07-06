#
# @lc app=leetcode.cn id=592 lang=python3
# @lcpr version=30203
#
# [592] 分数加减运算
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return abs(a)

        numerator = 0
        denominator = 1
        i = 0
        n = len(expression)
        while i < n:
            sign = 1
            if expression[i] in "+-":
                sign = -1 if expression[i] == "-" else 1
                i += 1

            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            i += 1
            den = 0
            while i < n and expression[i].isdigit():
                den = den * 10 + int(expression[i])
                i += 1

            numerator = numerator * den + sign * num * denominator
            denominator *= den
            common = gcd(abs(numerator), denominator)
            numerator //= common
            denominator //= common

        return f"{numerator}/{denominator}"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.fractionAddition, ("-1/2+1/2",), "0/1"),
        (solution.fractionAddition, ("-1/2+1/2+1/3",), "1/3"),
        (solution.fractionAddition, ("1/3-1/2",), "-1/6"),
        (solution.fractionAddition, ("5/3+1/3",), "2/1"),
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
# "-1/2+1/2"\n
# @lcpr case=end

# @lcpr case=start
# "-1/2+1/2+1/3"\n
# @lcpr case=end

# @lcpr case=start
# "1/3-1/2"\n
# @lcpr case=end

#
