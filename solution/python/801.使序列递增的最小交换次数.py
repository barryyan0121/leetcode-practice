#
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] 使序列递增的最小交换次数
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        keep, swap = 0, 1
        for index in range(1, len(nums1)):
            next_keep = next_swap = float("inf")
            if nums1[index - 1] < nums1[index] and nums2[index - 1] < nums2[index]:
                next_keep = keep
                next_swap = swap + 1
            if nums1[index - 1] < nums2[index] and nums2[index - 1] < nums1[index]:
                next_keep = min(next_keep, swap)
                next_swap = min(next_swap, keep + 1)
            keep, swap = next_keep, next_swap
        return int(min(keep, swap))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minSwap, ([1, 3, 5, 4], [1, 2, 3, 7]), 1),
        (solution.minSwap, ([0, 3, 5, 8, 9], [2, 1, 4, 6, 9]), 1),
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
