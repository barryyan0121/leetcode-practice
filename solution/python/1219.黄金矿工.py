from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def collect(row: int, col: int) -> int:
            gold = grid[row][col]
            grid[row][col] = 0
            best = 0
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col]
                ):
                    best = max(best, collect(next_row, next_col))
            grid[row][col] = gold
            return gold + best

        return max(
            (collect(row, col) for row in range(rows) for col in range(cols) if grid[row][col]),
            default=0,
        )


if __name__ == "__main__":
    test_cases = [
        ([[0, 6, 0], [5, 8, 7], [0, 9, 0]], 24),
        ([[1, 0, 7], [2, 0, 6], [3, 4, 5]], 28),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().getMaximumGold(grid) == expected
