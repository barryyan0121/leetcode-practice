class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        size = len(grid)
        middle = size // 2
        y_cells = []
        other_cells = []
        for row in range(size):
            for column in range(size):
                is_y = (row <= middle and column in (row, size - 1 - row)) or (
                    row > middle and column == middle
                )
                (y_cells if is_y else other_cells).append(grid[row][column])
        return min(
            len(y_cells)
            + len(other_cells)
            - y_cells.count(y_value)
            - other_cells.count(other_value)
            for y_value in range(3)
            for other_value in range(3)
            if y_value != other_value
        )


if __name__ == "__main__":
    test_cases = [
        ([[1, 2, 2], [1, 1, 0], [0, 1, 0]], 3),
        (
            [
                [0, 1, 0, 1, 0],
                [2, 1, 0, 1, 2],
                [2, 2, 2, 0, 1],
                [2, 2, 2, 2, 2],
                [2, 1, 2, 2, 2],
            ],
            12,
        ),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().minimumOperationsToWriteY(grid) == expected
