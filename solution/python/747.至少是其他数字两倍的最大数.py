#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        index = nums.index(largest)
        return (
            index
            if all(number == largest or largest >= 2 * number for number in nums)
            else -1
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.dominantIndex, ([3, 6, 1, 0],), 1),
        (solution.dominantIndex, ([1, 2, 3, 4],), -1),
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
