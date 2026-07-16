#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = current_max = nums[0]
        boundary = 0
        for index, number in enumerate(nums[1:], 1):
            current_max = max(current_max, number)
            if number < left_max:
                left_max = current_max
                boundary = index
        return boundary + 1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.partitionDisjoint, ([5, 0, 3, 8, 6],), 3),
        (solution.partitionDisjoint, ([1, 1, 1, 0, 6, 12],), 4),
        (solution.partitionDisjoint, ([1, 2],), 1),
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
