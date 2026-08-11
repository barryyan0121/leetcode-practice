#
# @lc app=leetcode.cn id=2272 lang=python3
# @lcpr version=30203
#
# [2272] 最大波动的子字符串
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def largestVariance(self, s: str) -> int:
        answer = 0
        for major in "abcdefghijklmnopqrstuvwxyz":
            for minor in "abcdefghijklmnopqrstuvwxyz":
                if major == minor:
                    continue
                remaining_minor = s.count(minor)
                major_count = minor_count = 0
                for char in s:
                    if char == major:
                        major_count += 1
                    elif char == minor:
                        minor_count += 1
                        remaining_minor -= 1
                    if minor_count:
                        answer = max(answer, major_count - minor_count)
                    if major_count < minor_count and remaining_minor:
                        major_count = minor_count = 0
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.largestVariance, ("aababbb",), 3),
        (solution.largestVariance, ("abcde",), 0),
        (solution.largestVariance, ("lripaa",), 1),
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
    print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
    sys.exit(1)
