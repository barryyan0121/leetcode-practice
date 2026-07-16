#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        start = next(
            (row, column)
            for row in range(n)
            for column in range(n)
            if grid[row][column]
        )
        stack = [start]
        grid[start[0]][start[1]] = 2
        while stack:
            row, column = stack.pop()
            queue.append((row, column))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    stack.append((nr, nc))

        distance = 0
        while queue:
            for _ in range(len(queue)):
                row, column = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, column + dc
                    if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] == 2:
                        continue
                    if grid[nr][nc] == 1:
                        return distance
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
            distance += 1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.shortestBridge, ([[0, 1], [1, 0]],), 1),
        (solution.shortestBridge, ([[0, 1, 0], [0, 0, 0], [0, 0, 1]],), 2),
        (
            solution.shortestBridge,
            (
                [
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
            ),
            1,
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
