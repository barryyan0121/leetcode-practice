#
# @lc app=leetcode.cn id=350 lang=python3
# @lcpr version=30203
#
# [350] 两个数组的交集 II
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(nums: List[int]) -> List[int]:
        return sorted(nums)

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.intersect, ([1, 2, 2, 1], [2, 2]), [2, 2]),
        (solution.intersect, ([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end
