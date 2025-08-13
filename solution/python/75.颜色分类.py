#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30202
#
# [75] 颜色分类
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 注意区间的开闭，初始化时区间内应该没有元素
        # 所以我们定义 [0，p0) 是元素 0 的区间，(p2, nums.length - 1] 是 2 的区间
        p0 = 0
        p2 = len(nums) - 1
        p = 0
        # 由于 p2 是开区间，所以 p <= p2
        while p <= p2:
            if nums[p] == 0:
                self.swap(nums, p0, p)
                p0 += 1
            elif nums[p] == 2:
                self.swap(nums, p2, p)
                p2 -= 1
            elif nums[p] == 1:
                p += 1

            # 因为小于 p0 都是 0，所以 p 不要小于 p0
            if p < p0:
                p = p0

    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    nums1 = [2, 0, 2, 1, 1, 0]
    nums2 = [2, 0, 1]
    test_cases = [
        (solution.sortColors, [nums1], None),
        (lambda: nums1, (), [0, 0, 1, 1, 2, 2]),
        (solution.sortColors, [nums2], None),
        (lambda: nums2, (), [0, 1, 2]),
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
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#
