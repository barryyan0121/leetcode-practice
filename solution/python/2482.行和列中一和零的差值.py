"""2482. 行和列中一和零的差值"""


class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        rows = [sum(row) for row in grid]
        cols = [sum(grid[row][col] for row in range(len(grid))) for col in range(len(grid[0]))]
        total_rows = len(grid[0])
        total_cols = len(grid)
        return [
            [2 * (rows[row] + cols[col]) - total_rows - total_cols for col in range(len(cols))]
            for row in range(len(rows))
        ]
