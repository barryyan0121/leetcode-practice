#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

import sys
import os
from collections import Counter, defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        required = len(need)
        formed = 0
        left = 0
        best_left = 0
        best_len = float("inf")

        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < best_len:
                    best_left = left
                    best_len = right - left + 1

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_left : best_left + best_len]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minWindow, ("ADOBECODEBANC", "ABC"), "BANC"),
        (solution.minWindow, ("a", "a"), "a"),
        (solution.minWindow, ("a", "aa"), ""),
        (solution.minWindow, ("ab", "b"), "b"),
        (solution.minWindow, ("aa", "aa"), "aa"),
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
