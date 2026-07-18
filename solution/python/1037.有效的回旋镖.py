#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (first_x, first_y), (second_x, second_y), (third_x, third_y) = points
        return (second_x - first_x) * (third_y - first_y) != (second_y - first_y) * (
            third_x - first_x
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isBoomerang, ([[1, 1], [2, 3], [3, 2]],), True),
        (solution.isBoomerang, ([[1, 1], [2, 2], [3, 3]],), False),
        (solution.isBoomerang, ([[0, 0], [0, 1], [0, 2]],), False),
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
