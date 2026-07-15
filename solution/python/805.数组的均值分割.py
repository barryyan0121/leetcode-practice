#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        size = len(nums)
        if size < 2:
            return False
        transformed = [number * size - sum(nums) for number in nums]
        middle = size // 2
        left, right = transformed[:middle], transformed[middle:]

        left_sums = set()
        left_proper_sums = set()
        for mask in range(1, 1 << len(left)):
            subset_sum = sum(
                left[index] for index in range(len(left)) if mask >> index & 1
            )
            if subset_sum == 0:
                return True
            left_sums.add(subset_sum)
            if mask != (1 << len(left)) - 1:
                left_proper_sums.add(subset_sum)

        for mask in range(1, 1 << len(right)):
            subset_sum = sum(
                right[index] for index in range(len(right)) if mask >> index & 1
            )
            if subset_sum == 0:
                return True
            candidates = (
                left_proper_sums if mask == (1 << len(right)) - 1 else left_sums
            )
            if -subset_sum in candidates:
                return True
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.splitArraySameAverage, ([1, 2, 3, 4, 5, 6, 7, 8],), True),
        (solution.splitArraySameAverage, ([3, 1],), False),
        (solution.splitArraySameAverage, ([1, 1],), True),
        (solution.splitArraySameAverage, ([1],), False),
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
