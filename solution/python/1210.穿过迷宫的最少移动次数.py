from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        size = len(grid)
        queue = deque([(0, 0, 0, 0)])
        seen = {(0, 0, 0)}
        while queue:
            row, col, direction, steps = queue.popleft()
            if (row, col, direction) == (size - 1, size - 2, 0):
                return steps
            moves = []
            if direction == 0:
                if col + 2 < size and not grid[row][col + 2]:
                    moves.append((row, col + 1, 0))
                if (
                    row + 1 < size
                    and not grid[row + 1][col]
                    and not grid[row + 1][col + 1]
                ):
                    moves.extend(((row + 1, col, 0), (row, col, 1)))
            else:
                if row + 2 < size and not grid[row + 2][col]:
                    moves.append((row + 1, col, 1))
                if (
                    col + 1 < size
                    and not grid[row][col + 1]
                    and not grid[row + 1][col + 1]
                ):
                    moves.extend(((row, col + 1, 1), (row, col, 0)))
            for state in moves:
                if state not in seen:
                    seen.add(state)
                    queue.append((*state, steps + 1))
        return -1


if __name__ == "__main__":
    test_cases = [
        (
            [
                [0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 0],
            ],
            11,
        )
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().minimumMoves(grid) == expected
