#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        previous = matrix[0]
        for row in matrix[1:]:
            previous = [
                value + min(previous[max(0, column - 1) : column + 2])
                for column, value in enumerate(row)
            ]
        return min(previous)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minFallingPathSum, ([[2, 1, 3], [6, 5, 4], [7, 8, 9]],), 13),
        (solution.minFallingPathSum, ([[-19, 57], [-40, -5]],), -59),
        (solution.minFallingPathSum, ([[5]],), 5),
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
