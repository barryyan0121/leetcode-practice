#
# @lc app=leetcode.cn id=639 lang=python3
# @lcpr version=30203
#
# [639] 解码方法 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7

        def one(ch: str) -> int:
            if ch == "*":
                return 9
            return 0 if ch == "0" else 1

        def two(a: str, b: str) -> int:
            if a == "*" and b == "*":
                return 15
            if a == "*":
                return 2 if b <= "6" else 1
            if b == "*":
                return 9 if a == "1" else 6 if a == "2" else 0
            return 1 if 10 <= int(a + b) <= 26 else 0

        prev2, prev1 = 1, one(s[0])
        for i in range(1, len(s)):
            cur = (one(s[i]) * prev1 + two(s[i - 1], s[i]) * prev2) % mod
            prev2, prev1 = prev1, cur
        return prev1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numDecodings, ("*",), 9),
        (solution.numDecodings, ("1*",), 18),
        (solution.numDecodings, ("2*",), 15),
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

