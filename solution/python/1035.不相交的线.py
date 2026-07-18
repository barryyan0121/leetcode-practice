#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * (len(nums2) + 1)
        for first in nums1:
            previous = 0
            for index, second in enumerate(nums2, 1):
                current = dp[index]
                if first == second:
                    dp[index] = previous + 1
                else:
                    dp[index] = max(dp[index], dp[index - 1])
                previous = current
        return dp[-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxUncrossedLines, ([1, 4, 2], [1, 2, 4]), 2),
        (solution.maxUncrossedLines, ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]), 3),
        (solution.maxUncrossedLines, ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]), 2),
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
