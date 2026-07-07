#
# @lc app=leetcode.cn id=646 lang=python3
# @lcpr version=30203
#
# [646] 最长数对链
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans = 0
        cur = -(10**9)
        for left, right in sorted(pairs, key=lambda pair: pair[1]):
            if left > cur:
                ans += 1
                cur = right
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findLongestChain, ([[1, 2], [2, 3], [3, 4]],), 2),
        (solution.findLongestChain, ([[1, 2], [7, 8], [4, 5]],), 3),
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
