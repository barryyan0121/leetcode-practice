#
# @lc app=leetcode.cn id=564 lang=python3
# @lcpr version=30203
#
# [564] 寻找最近的回文数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == "1":
            return "0"

        length = len(n)
        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

        candidates = {
            str(10 ** (length - 1) - 1),
            str(10**length + 1),
        }

        def build(value: int) -> str:
            s = str(value)
            if length % 2 == 0:
                return s + s[::-1]
            return s + s[-2::-1]

        for delta in (-1, 0, 1):
            value = prefix + delta
            if value > 0:
                candidates.add(build(value))

        candidates.discard(n)

        target = int(n)
        best = None
        for candidate in candidates:
            current = int(candidate)
            diff = abs(current - target)
            if (
                best is None
                or diff < best[0]
                or (diff == best[0] and current < best[1])
            ):
                best = (diff, current)

        return str(best[1])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.nearestPalindromic, ("123",), "121"),
        (solution.nearestPalindromic, ("1",), "0"),
        (solution.nearestPalindromic, ("10",), "9"),
        (solution.nearestPalindromic, ("99",), "101"),
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
# 123\n
# @lcpr case=end
#
