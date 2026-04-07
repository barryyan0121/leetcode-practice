#
# @lc app=leetcode.cn id=214 lang=python3
# @lcpr version=30203
#
# [214] 最短回文串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        t = s + "#" + rev
        lps = [0] * len(t)
        for i in range(1, len(t)):
            j = lps[i - 1]
            while j > 0 and t[i] != t[j]:
                j = lps[j - 1]
            if t[i] == t[j]:
                j += 1
            lps[i] = j
        return rev[: len(s) - lps[-1]] + s


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.shortestPalindrome, ["aacecaaa"], "aaacecaaa"),
        (solution.shortestPalindrome, ["abcd"], "dcbabcd"),
        (solution.shortestPalindrome, ["a"], "a"),
        (solution.shortestPalindrome, [""], ""),
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
# "aacecaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n
# @lcpr case=end

#
