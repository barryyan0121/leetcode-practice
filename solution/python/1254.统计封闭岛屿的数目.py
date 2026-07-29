from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def flood(row: int, col: int) -> None:
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                if not (0 <= row < rows and 0 <= col < cols) or grid[row][col]:
                    continue
                grid[row][col] = 1
                stack += [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ]

        for row in range(rows):
            flood(row, 0)
            flood(row, cols - 1)
        for col in range(cols):
            flood(0, col)
            flood(rows - 1, col)
        return sum(
            not grid[row][col] and not flood(row, col)
            for row in range(rows)
            for col in range(cols)
        )


if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ],
            2,
        )
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().closedIsland(grid) == expected
