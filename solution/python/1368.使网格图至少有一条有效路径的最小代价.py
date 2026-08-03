# @lc app=leetcode.cn id=1368 lang=python3

from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = [[10**9] * cols for _ in range(rows)]
        distance[0][0] = 0
        queue = deque([(0, 0)])
        while queue:
            row, column = queue.popleft()
            for direction, (dr, dc) in enumerate(directions, 1):
                nr, nc = row + dr, column + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    cost = distance[row][column] + (direction != grid[row][column])
                    if cost < distance[nr][nc]:
                        distance[nr][nc] = cost
                        if direction == grid[row][column]:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
        return distance[-1][-1]


if __name__ == "__main__":
    test_cases = [
        (
            Solution().minCost,
            ([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]],),
            3,
        ),
        (Solution().minCost, ([[1, 2], [4, 3]],), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1368 题 "使网格图至少有一条有效路径的最小代价" 所有测试用例通过')
