#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for num in nums:
            if write < 2 or num != nums[write - 2]:
                nums[write] = num
                write += 1
        return write


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    nums1 = [1, 1, 1, 2, 2, 3]
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    test_cases = [
        (solution.removeDuplicates, [nums1], 5),
        (lambda: nums1[:5], (), [1, 1, 2, 2, 3]),
        (solution.removeDuplicates, [nums2], 7),
        (lambda: nums2[:7], (), [0, 0, 1, 1, 2, 3, 3]),
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
# [1,1,1,2,2,3]\n
# @lcpr case=end
