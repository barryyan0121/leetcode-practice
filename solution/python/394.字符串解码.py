#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30203
#
# [394] 字符串解码
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((curr, num))
                curr = []
                num = 0
            elif ch == "]":
                prev, repeat = stack.pop()
                curr = prev + curr * repeat
            else:
                curr.append(ch)

        return "".join(curr)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.decodeString, ("3[a]2[bc]",), "aaabcbc"),
        (solution.decodeString, ("3[a2[c]]",), "accaccacc"),
        (solution.decodeString, ("2[abc]3[cd]ef",), "abcabccdcdcdef"),
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
# "3[a2[c]]"\n
# @lcpr case=end
