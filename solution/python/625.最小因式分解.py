#
# @lc app=leetcode.cn id=625 lang=python3
# @lcpr version=30203
#
# [625] 最小因式分解
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 10:
            return num
        digits = []
        for factor in range(9, 1, -1):
            while num % factor == 0:
                digits.append(str(factor))
                num //= factor
        if num != 1:
            return 0
        result = int("".join(reversed(digits)))
        return result if result <= 2**31 - 1 else 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.smallestFactorization, (48,), 68),
        (solution.smallestFactorization, (15,), 35),
        (solution.smallestFactorization, (1,), 1),
        (solution.smallestFactorization, (11,), 0),
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
    print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
    sys.exit(1)
