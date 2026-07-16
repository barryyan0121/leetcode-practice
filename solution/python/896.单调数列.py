#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pairs = zip(nums, nums[1:])
        return all(left <= right for left, right in pairs) or all(
            left >= right for left, right in zip(nums, nums[1:])
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isMonotonic, ([1, 2, 2, 3],), True),
        (solution.isMonotonic, ([6, 5, 4, 4],), True),
        (solution.isMonotonic, ([1, 3, 2],), False),
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
