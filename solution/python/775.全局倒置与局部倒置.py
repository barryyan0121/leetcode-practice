#
# @lc app=leetcode.cn id=775 lang=python3
#
# [775] 全局倒置与局部倒置
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(index - value) <= 1 for index, value in enumerate(nums))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isIdealPermutation, ([1, 0, 2],), True),
        (solution.isIdealPermutation, ([1, 2, 0],), False),
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
