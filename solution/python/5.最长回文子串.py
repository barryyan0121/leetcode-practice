#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30202
#
# [5] 最长回文子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        end = 0

        def expand(left: int, right: int) -> None:
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > end - start:
                start = left
                end = right

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[start : end + 1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.longestPalindrome, ("babad",), "bab"),
        (solution.longestPalindrome, ("cbbd",), "bb"),
        (solution.longestPalindrome, ("a",), "a"),
        (solution.longestPalindrome, ("ac",), "a"),
        (solution.longestPalindrome, ("forgeeksskeegfor",), "geeksskeeg"),
        (solution.longestPalindrome, ("aaaa",), "aaaa"),
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
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#
