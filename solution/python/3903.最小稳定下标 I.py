#
# @lc app=leetcode.cn id=3903 lang=python3
#
# [3903] 最小稳定下标 I
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        suffix_min = nums[:]
        for index in range(len(nums) - 2, -1, -1):
            suffix_min[index] = min(suffix_min[index], suffix_min[index + 1])

        prefix_max = nums[0]
        for index, num in enumerate(nums):
            prefix_max = max(prefix_max, num)
            if prefix_max - suffix_min[index] <= k:
                return index
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.firstStableIndex, ([5, 0, 1, 4], 3), 3),
        (solution.firstStableIndex, ([1, 2, 3], 0), 0),
        (solution.firstStableIndex, ([10, 1, 9], 5), 2),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: args = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: args = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
