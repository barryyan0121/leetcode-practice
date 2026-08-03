class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        rows, columns = len(grid), len(grid[0])
        for row in range(rows):
            for column in range(columns):
                if row + 1 < rows and grid[row][column] != grid[row + 1][column]:
                    return False
                if column + 1 < columns and grid[row][column] == grid[row][column + 1]:
                    return False
        return True


if __name__ == "__main__":
    test_cases = [([[1, 0, 1], [1, 0, 1]], True), ([[1, 1]], False)]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().satisfiesConditions(grid) == expected
