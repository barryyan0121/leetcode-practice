class Solution:
    def numberOfRightTriangles(self, grid: list[list[int]]) -> int:
        row_counts = [sum(row) for row in grid]
        column_counts = [
            sum(grid[row][column] for row in range(len(grid)))
            for column in range(len(grid[0]))
        ]
        return sum(
            (row_counts[row] - 1) * (column_counts[column] - 1)
            for row in range(len(grid))
            for column in range(len(grid[0]))
            if grid[row][column]
        )


if __name__ == "__main__":
    test_cases = [
        ([[1, 0, 1], [1, 0, 0], [1, 0, 0], [1, 0, 1]], 8),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 0),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().numberOfRightTriangles(grid) == expected
