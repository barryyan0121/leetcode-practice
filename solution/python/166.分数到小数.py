#
# @lc app=leetcode.cn id=166 lang=python3
# @lcpr version=30202
#
# [166] 分数到小数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        num = abs(numerator)
        den = abs(denominator)
        integer = num // den
        rem = num % den
        if rem == 0:
            return sign + str(integer)

        res = [sign + str(integer), "."]
        seen = {}
        while rem:
            if rem in seen:
                idx = seen[rem]
                res.insert(idx, "(")
                res.append(")")
                break
            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den
        return "".join(res)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.fractionToDecimal, [1, 2], "0.5"),
        (solution.fractionToDecimal, [2, 1], "2"),
        (solution.fractionToDecimal, [2, 3], "0.(6)"),
        (solution.fractionToDecimal, [-50, 8], "-6.25"),
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
# 1\n2\n
# @lcpr case=end

#
