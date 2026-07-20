class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        columns = len(grid[0])
        values = [value for row in grid for value in row]
        k %= len(values)
        values = values[-k:] + values[:-k]
        return [
            values[index : index + columns] for index in range(0, len(values), columns)
        ]


if __name__ == "__main__":
    test_cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            1,
            [[9, 1, 2], [3, 4, 5], [6, 7, 8]],
        ),
        (
            [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
            4,
            [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
        ),
        ([[1, 2, 3]], 3, [[1, 2, 3]]),
    ]
    for _, (grid, k, expected) in enumerate(test_cases):
        assert Solution().shiftGrid(grid, k) == expected
