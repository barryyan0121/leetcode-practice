#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        size = len(grid)
        areas = {}
        island = 2
        for row in range(size):
            for column in range(size):
                if grid[row][column] != 1:
                    continue
                stack = [(row, column)]
                grid[row][column] = island
                area = 0
                while stack:
                    current_row, current_column = stack.pop()
                    area += 1
                    for row_change, column_change in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = current_row + row_change
                        next_column = current_column + column_change
                        if (
                            0 <= next_row < size
                            and 0 <= next_column < size
                            and grid[next_row][next_column] == 1
                        ):
                            grid[next_row][next_column] = island
                            stack.append((next_row, next_column))
                areas[island] = area
                island += 1

        answer = max(areas.values(), default=0)
        for row in range(size):
            for column in range(size):
                if grid[row][column] != 0:
                    continue
                neighbors = {
                    grid[next_row][next_column]
                    for row_change, column_change in ((1, 0), (-1, 0), (0, 1), (0, -1))
                    if 0 <= (next_row := row + row_change) < size
                    and 0 <= (next_column := column + column_change) < size
                    and grid[next_row][next_column] > 1
                }
                answer = max(answer, 1 + sum(areas[neighbor] for neighbor in neighbors))
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.largestIsland, ([[1, 0], [0, 1]],), 3),
        (solution.largestIsland, ([[1, 1], [1, 0]],), 4),
        (solution.largestIsland, ([[1, 1], [1, 1]],), 4),
        (solution.largestIsland, ([[0]],), 1),
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
