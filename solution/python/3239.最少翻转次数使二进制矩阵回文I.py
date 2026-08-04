class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        rows = sum(
            grid[row][left] != grid[row][right]
            for row in range(len(grid))
            for left, right in zip(
                range(len(grid[0]) // 2), range(len(grid[0]) - 1, -1, -1)
            )
        )
        columns = sum(
            grid[top][column] != grid[bottom][column]
            for column in range(len(grid[0]))
            for top, bottom in zip(range(len(grid) // 2), range(len(grid) - 1, -1, -1))
        )
        return min(rows, columns)


if __name__ == "__main__":
    test_cases = [
        ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 2),
        ([[0, 1], [0, 1], [0, 0]], 1),
        ([[1], [0]], 0),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().minFlips(grid) == expected
