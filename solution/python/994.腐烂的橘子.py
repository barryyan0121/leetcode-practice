#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    rotten.append((row, column))
                elif grid[row][column] == 1:
                    fresh += 1
        minutes = 0
        while rotten and fresh:
            minutes += 1
            for _ in range(len(rotten)):
                row, column = rotten.popleft()
                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    if (
                        0 <= next_row < len(grid)
                        and 0 <= next_column < len(grid[0])
                        and grid[next_row][next_column] == 1
                    ):
                        grid[next_row][next_column] = 2
                        fresh -= 1
                        rotten.append((next_row, next_column))
        return minutes if fresh == 0 else -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.orangesRotting, ([[2, 1, 1], [1, 1, 0], [0, 1, 1]],), 4),
        (solution.orangesRotting, ([[2, 1, 1], [0, 1, 1], [1, 0, 1]],), -1),
        (solution.orangesRotting, ([[0, 2]],), 0),
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
