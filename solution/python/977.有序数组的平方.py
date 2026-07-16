#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        return result[::-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sortedSquares, ([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100]),
        (solution.sortedSquares, ([-7, -3, 2, 3, 11],), [4, 9, 9, 49, 121]),
        (solution.sortedSquares, ([-1],), [1]),
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
