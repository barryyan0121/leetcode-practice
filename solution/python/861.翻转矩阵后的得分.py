#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        score = rows * (1 << (columns - 1))
        for column in range(1, columns):
            ones = sum(grid[row][column] == grid[row][0] for row in range(rows))
            score += max(ones, rows - ones) * (1 << (columns - column - 1))
        return score


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.matrixScore, ([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]],), 39),
        (solution.matrixScore, ([[0]],), 1),
        (solution.matrixScore, ([[1, 1], [0, 0]],), 6),
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
