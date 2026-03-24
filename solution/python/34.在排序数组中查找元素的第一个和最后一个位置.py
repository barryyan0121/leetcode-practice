#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30202
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound() -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper_bound() -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        left = lower_bound()
        right = upper_bound() - 1
        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.searchRange, ([5, 7, 7, 8, 8, 10], 8), [3, 4]),
        (solution.searchRange, ([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
        (solution.searchRange, ([], 0), [-1, -1]),
        (solution.searchRange, ([1], 1), [0, 0]),
        (solution.searchRange, ([2, 2], 2), [0, 1]),
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


#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

