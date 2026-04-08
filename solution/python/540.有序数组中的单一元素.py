#
# @lc app=leetcode.cn id=540 lang=python3
# @lcpr version=30203
#
# [540] 有序数组中的单一元素
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.singleNonDuplicate, ([1, 1, 2, 3, 3, 4, 4, 8, 8],), 2),
        (solution.singleNonDuplicate, ([3, 3, 7, 7, 10, 11, 11],), 10),
        (solution.singleNonDuplicate, ([1],), 1),
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
# [1,1,2,3,3,4,4,8,8]\n
# @lcpr case=end
#
