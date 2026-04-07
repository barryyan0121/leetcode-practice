#
# @lc app=leetcode.cn id=324 lang=python3
# @lcpr version=30203
#
# [324] 摆动排序 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        half = (len(nums) + 1) // 2
        small = nums[:half][::-1]
        large = nums[half:][::-1]
        nums[::2] = small
        nums[1::2] = large
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    nums1 = [1, 5, 1, 1, 6, 4]
    nums2 = [1, 3, 2, 2, 3, 1]
    test_cases = [
        (solution.wiggleSort, [nums1], None),
        (lambda: nums1, (), [1, 6, 1, 5, 1, 4]),
        (solution.wiggleSort, [nums2], None),
        (lambda: nums2, (), [2, 3, 1, 3, 1, 2]),
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
# [1,5,1,1,6,4]\n
# @lcpr case=end

#
