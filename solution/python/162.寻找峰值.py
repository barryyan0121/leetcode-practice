#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30203
#
# [162] 寻找峰值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def is_peak(nums: List[int], idx: int) -> bool:
        left_ok = idx == 0 or nums[idx] > nums[idx - 1]
        right_ok = idx == len(nums) - 1 or nums[idx] > nums[idx + 1]
        return left_ok and right_ok

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findPeakElement, ([1, 2, 3, 1],), 2),
        (solution.findPeakElement, ([1, 2, 1, 3, 5, 6, 4],), None),
        (solution.findPeakElement, ([1],), 0),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            if expected is None:
                assert is_peak(args[0], result)
            else:
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
# [1,2,3,1]\n
# @lcpr case=end
