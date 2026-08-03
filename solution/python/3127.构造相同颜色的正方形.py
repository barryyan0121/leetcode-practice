class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        for row in range(2):
            for column in range(2):
                black = sum(
                    grid[r][c] == "B"
                    for r in range(row, row + 2)
                    for c in range(column, column + 2)
                )
                if black != 2:
                    return True
        return False


if __name__ == "__main__":
    test_cases = [
        ([["B", "W", "B"], ["B", "W", "W"], ["B", "B", "B"]], True),
        ([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]], False),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().canMakeSquare(grid) == expected
