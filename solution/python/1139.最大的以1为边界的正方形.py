class Solution:
    def largest1BorderedSquare(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        left = [[0] * columns for _ in range(rows)]
        up = [[0] * columns for _ in range(rows)]
        best = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]:
                    left[row][column] = 1 + (left[row][column - 1] if column else 0)
                    up[row][column] = 1 + (up[row - 1][column] if row else 0)
                    side = min(left[row][column], up[row][column])
                    while side > best:
                        if (
                            up[row][column - side + 1] >= side
                            and left[row - side + 1][column] >= side
                        ):
                            best = side
                        side -= 1
        return best * best


if __name__ == "__main__":
    test_cases = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 9),
        ([[1, 1, 0, 0]], 1),
        ([[0, 0], [0, 0]], 0),
        ([[1]], 1),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().largest1BorderedSquare(grid) == expected
