#
# @lc app=leetcode.cn id=3756 lang=python3
# @lcpr version=30203
#
# [3756] 连接非零数字并乘以其数字和 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        digit_sum = [0]
        nonzero_count = [0]
        values = [0]
        pow10 = [1]

        for ch in s:
            digit = ord(ch) - ord("0")
            digit_sum.append(digit_sum[-1] + digit)
            nonzero_count.append(nonzero_count[-1] + (digit != 0))
            if digit:
                values.append((values[-1] * 10 + digit) % mod)
                pow10.append(pow10[-1] * 10 % mod)

        ans = []
        for left, right in queries:
            start = nonzero_count[left]
            end = nonzero_count[right + 1]
            x = (values[end] - values[start] * pow10[end - start]) % mod
            total = digit_sum[right + 1] - digit_sum[left]
            ans.append(x * total % mod)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.sumAndMultiply,
            ("10203004", [[0, 7], [1, 3], [4, 6]]),
            [12340, 4, 9],
        ),
        (solution.sumAndMultiply, ("1000", [[0, 3], [1, 1]]), [1, 0]),
        (solution.sumAndMultiply, ("9876543210", [[0, 9]]), [444444137]),
        (
            solution.sumAndMultiply,
            ("0010203", [[0, 6], [2, 5], [0, 1]]),
            [123 * 6, 12 * 3, 0],
        ),
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
