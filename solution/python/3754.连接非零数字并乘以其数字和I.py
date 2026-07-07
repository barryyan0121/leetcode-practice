#
# @lc app=leetcode.cn id=3754 lang=python3
# @lcpr version=30203
#
# [3754] 连接非零数字并乘以其数字和 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(ch) for ch in str(n) if ch != "0"]
        if not digits:
            return 0
        x = int("".join(map(str, digits)))
        return x * sum(digits)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sumAndMultiply, (1234,), 12340),
        (solution.sumAndMultiply, (10203004,), 12340),
        (solution.sumAndMultiply, (1000,), 1),
        (solution.sumAndMultiply, (0,), 0),
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
