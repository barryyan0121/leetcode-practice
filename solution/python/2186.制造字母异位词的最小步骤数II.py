#
# @lc app=leetcode.cn id=2186 lang=python3
# @lcpr version=30203
#
# [2186] 制造字母异位词的最小步骤数 II
#

import os
import sys
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        difference = Counter(s)
        difference.subtract(t)
        return sum(abs(count) for count in difference.values())


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minSteps, ("leetcode", "coats"), 7),
        (solution.minSteps, ("night", "thing"), 0),
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
