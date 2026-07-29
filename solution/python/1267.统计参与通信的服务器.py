from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]
        return sum(
            value and (rows[row] > 1 or cols[col] > 1)
            for row, line in enumerate(grid)
            for col, value in enumerate(line)
        )


if __name__ == "__main__":
    test_cases = [([[1, 0], [1, 1]], 3), ([[1, 0], [0, 1]], 0)]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().countServers(grid) == expected
