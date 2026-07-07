#
# @lc app=leetcode.cn id=645 lang=python3
# @lcpr version=30203
#
# [645] 错误的集合
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        dup = 0
        for num in nums:
            if num in seen:
                dup = num
            seen.add(num)
        missing = next(num for num in range(1, len(nums) + 1) if num not in seen)
        return [dup, missing]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findErrorNums, ([1, 2, 2, 4],), [2, 3]),
        (solution.findErrorNums, ([1, 1],), [1, 2]),
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
