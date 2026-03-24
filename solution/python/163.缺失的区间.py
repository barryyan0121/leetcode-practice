#
# @lc app=leetcode.cn id=163 lang=python3
# @lcpr version=30202
#
# [163] 缺失的区间
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        res = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            cur = nums[i] if i < len(nums) else upper + 1
            if cur - prev >= 2:
                res.append([prev + 1, cur - 1])
            prev = cur
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findMissingRanges,
            [[0, 1, 3, 50, 75], 0, 99],
            [[2, 2], [4, 49], [51, 74], [76, 99]],
        ),
        (solution.findMissingRanges, [[], 1, 1], [[1, 1]]),
        (solution.findMissingRanges, [[1, 1, 1], 1, 1], []),
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
# [0,1,3,50,75]\n0\n99\n
# @lcpr case=end

#
