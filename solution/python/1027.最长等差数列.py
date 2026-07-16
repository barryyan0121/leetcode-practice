#
# @lc app=leetcode.cn id=1027 lang=python3
#
# [1027] 最长等差数列
#

import os
import sys
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [defaultdict(lambda: 1) for _ in nums]
        result = 2
        for right in range(1, len(nums)):
            for left in range(right):
                difference = nums[right] - nums[left]
                dp[right][difference] = max(
                    dp[right][difference], dp[left][difference] + 1
                )
                result = max(result, dp[right][difference])
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.longestArithSeqLength, ([3, 6, 9, 12],), 4),
        (solution.longestArithSeqLength, ([9, 4, 7, 2, 10],), 3),
        (solution.longestArithSeqLength, ([20, 1, 15, 3, 10, 5, 8],), 4),
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
