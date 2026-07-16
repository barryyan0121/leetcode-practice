#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续 1 的个数 III
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right, number in enumerate(nums):
            k -= number == 0
            if k < 0:
                k += nums[left] == 0
                left += 1
        return len(nums) - left


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.longestOnes, ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6),
        (
            solution.longestOnes,
            ([0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], 3),
            10,
        ),
        (solution.longestOnes, ([0, 0, 0], 0), 0),
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
