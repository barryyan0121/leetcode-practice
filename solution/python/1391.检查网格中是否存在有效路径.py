# @lc app=leetcode.cn id=1391 lang=python3
from collections import deque
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        moves = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }
        reverse = {(0, 1): (0, -1), (0, -1): (0, 1), (1, 0): (-1, 0), (-1, 0): (1, 0)}
        rows, cols = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        seen = {(0, 0)}
        while queue:
            row, col = queue.popleft()
            if (row, col) == (rows - 1, cols - 1):
                return True
            for dr, dc in moves[grid[row][col]]:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and reverse[(dr, dc)] in moves[grid[nr][nc]]
                    and (nr, nc) not in seen
                ):
                    seen.add((nr, nc))
                    queue.append((nr, nc))
        return False


if __name__ == "__main__":
    test_cases = [
        (Solution().hasValidPath, ([[2, 4, 3], [6, 5, 2]],), True),
        (Solution().hasValidPath, ([[1, 2, 1], [1, 2, 1]],), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1391 题 "检查网格中是否存在有效路径" 所有测试用例通过')
