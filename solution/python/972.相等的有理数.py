#
# @lc app=leetcode.cn id=972 lang=python3
#
# [972] 相等的有理数
#

import os
import sys
from fractions import Fraction


# @lc code=start
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(value):
            integer, _, decimal = value.partition(".")
            result = Fraction(int(integer), 1)
            if "(" in decimal:
                finite, repeating = decimal[:-1].split("(")
            else:
                finite, repeating = decimal, ""
            if finite:
                result += Fraction(int(finite), 10 ** len(finite))
            if repeating:
                result += Fraction(
                    int(repeating),
                    10 ** len(finite) * (10 ** len(repeating) - 1),
                )
            return result

        return parse(s) == parse(t)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isRationalEqual, ("0.(52)", "0.5(25)"), True),
        (solution.isRationalEqual, ("0.1666(6)", "0.166(66)"), True),
        (solution.isRationalEqual, ("0.9(9)", "1.0"), True),
        (solution.isRationalEqual, ("1.0", "1"), True),
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
