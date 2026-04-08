#
# @lc app=leetcode.cn id=541 lang=python3
# @lcpr version=30203
#
# [541] 反转字符串 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for start in range(0, len(chars), 2 * k):
            chars[start : start + k] = reversed(chars[start : start + k])
        return "".join(chars)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.reverseStr, ("abcdefg", 2), "bacdfeg"),
        (solution.reverseStr, ("abcd", 2), "bacd"),
        (solution.reverseStr, ("abcdefg", 3), "cbadefg"),
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
# "abcdefg"\n2\n
# @lcpr case=end
#
