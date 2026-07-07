#
# @lc app=leetcode.cn id=674 lang=python3
# @lcpr version=30203
#
# [674] 最长连续递增序列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = cur = 1
        for i in range(1, len(nums)):
            cur = cur + 1 if nums[i - 1] < nums[i] else 1
            ans = max(ans, cur)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findLengthOfLCIS, ([1, 3, 5, 4, 7],), 3),
        (solution.findLengthOfLCIS, ([2, 2, 2, 2, 2],), 1),
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
