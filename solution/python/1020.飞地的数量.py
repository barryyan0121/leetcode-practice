#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        stack = [
            (row, column)
            for row in range(rows)
            for column in range(columns)
            if (row in (0, rows - 1) or column in (0, columns - 1))
            and grid[row][column]
        ]
        while stack:
            row, column = stack.pop()
            if grid[row][column] == 0:
                continue
            grid[row][column] = 0
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and grid[next_row][next_column]
                ):
                    stack.append((next_row, next_column))
        return sum(map(sum, grid))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.numEnclaves,
            ([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],),
            3,
        ),
        (
            solution.numEnclaves,
            ([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],),
            0,
        ),
        (solution.numEnclaves, ([[1]],), 0),
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
