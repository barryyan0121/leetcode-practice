#
# @lc app=leetcode.cn id=1034 lang=python3
#
# [1034] 边界着色
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])
        original = grid[row][col]
        stack = [(row, col)]
        seen = {(row, col)}
        border = []
        while stack:
            current_row, current_column = stack.pop()
            is_border = False
            for next_row, next_column in (
                (current_row - 1, current_column),
                (current_row + 1, current_column),
                (current_row, current_column - 1),
                (current_row, current_column + 1),
            ):
                if not (0 <= next_row < rows and 0 <= next_column < columns):
                    is_border = True
                elif grid[next_row][next_column] != original:
                    is_border = True
                elif (next_row, next_column) not in seen:
                    seen.add((next_row, next_column))
                    stack.append((next_row, next_column))
            if is_border:
                border.append((current_row, current_column))
        for current_row, current_column in border:
            grid[current_row][current_column] = color
        return grid


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.colorBorder, ([[1, 1], [1, 2]], 0, 0, 3), [[3, 3], [3, 2]]),
        (
            solution.colorBorder,
            ([[1, 2, 2], [2, 3, 2]], 0, 1, 3),
            [[1, 3, 3], [2, 3, 3]],
        ),
        (
            solution.colorBorder,
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2),
            [[2, 2, 2], [2, 1, 2], [2, 2, 2]],
        ),
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
