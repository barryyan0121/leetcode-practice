#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        remaining = 1
        start = (0, 0)
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 0:
                    remaining += 1
                elif grid[row][column] == 1:
                    start = (row, column)

        def search(row, column, left):
            if grid[row][column] == 2:
                return int(left == 0)
            value = grid[row][column]
            grid[row][column] = -1
            paths = 0
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if (
                    0 <= next_row < len(grid)
                    and 0 <= next_column < len(grid[0])
                    and grid[next_row][next_column] != -1
                ):
                    paths += search(next_row, next_column, left - 1)
            grid[row][column] = value
            return paths

        return search(*start, remaining)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.uniquePathsIII, ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]],), 2),
        (solution.uniquePathsIII, ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]],), 4),
        (solution.uniquePathsIII, ([[0, 1], [2, 0]],), 0),
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
