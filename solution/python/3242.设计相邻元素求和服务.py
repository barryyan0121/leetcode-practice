class NeighborSum:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.positions = {
            value: (row, column)
            for row, line in enumerate(grid)
            for column, value in enumerate(line)
        }

    def adjacentSum(self, value: int) -> int:
        row, column = self.positions[value]
        return sum(
            self.grid[next_row][next_column]
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            )
            if 0 <= next_row < len(self.grid) and 0 <= next_column < len(self.grid)
        )

    def diagonalSum(self, value: int) -> int:
        row, column = self.positions[value]
        return sum(
            self.grid[next_row][next_column]
            for next_row, next_column in (
                (row - 1, column - 1),
                (row - 1, column + 1),
                (row + 1, column - 1),
                (row + 1, column + 1),
            )
            if 0 <= next_row < len(self.grid) and 0 <= next_column < len(self.grid)
        )


if __name__ == "__main__":
    test_cases = [
        (
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
            [
                ("adjacentSum", 1, 6),
                ("adjacentSum", 4, 16),
                ("diagonalSum", 4, 16),
                ("diagonalSum", 8, 4),
            ],
        )
    ]
    for _, (grid, calls) in enumerate(test_cases):
        service = NeighborSum(grid)
        for method, value, expected in calls:
            assert getattr(service, method)(value) == expected
