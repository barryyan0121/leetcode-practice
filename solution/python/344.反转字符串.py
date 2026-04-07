#
# @lc app=leetcode.cn id=344 lang=python3
# @lcpr version=30203
#
# [344] 反转字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    chars1 = ["h", "e", "l", "l", "o"]
    chars2 = ["H", "a", "n", "n", "a", "h"]

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.reverseString, (chars1,), ["o", "l", "l", "e", "h"]),
        (solution.reverseString, (chars2,), ["h", "a", "n", "n", "a", "H"]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            func(*args)
            result = args[0]
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
# ["h","e","l","l","o"]\n
# @lcpr case=end
