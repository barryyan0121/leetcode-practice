#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * (len(nums2) + 1)
        answer = 0
        for first in nums1:
            for j in range(len(nums2) - 1, -1, -1):
                dp[j + 1] = dp[j] + 1 if first == nums2[j] else 0
                answer = max(answer, dp[j + 1])
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findLength, ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]), 3),
        (solution.findLength, ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]), 5),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
