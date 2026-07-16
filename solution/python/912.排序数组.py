#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sortArray, ([5, 2, 3, 1],), [1, 2, 3, 5]),
        (solution.sortArray, ([5, 1, 1, 2, 0, 0],), [0, 0, 1, 1, 2, 5]),
        (solution.sortArray, ([-1],), [-1]),
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
