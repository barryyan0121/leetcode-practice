#
# @lc app=leetcode.cn id=624 lang=python3
# @lcpr version=30203
#
# [624] 数组列表中的最大距离
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        ans = 0
        for arr in arrays[1:]:
            ans = max(ans, abs(arr[-1] - min_value), abs(max_value - arr[0]))
            min_value = min(min_value, arr[0])
            max_value = max(max_value, arr[-1])
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxDistance, ([[1, 2, 3], [4, 5], [1, 2, 3]],), 4),
        (solution.maxDistance, ([[1], [1]],), 0),
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

