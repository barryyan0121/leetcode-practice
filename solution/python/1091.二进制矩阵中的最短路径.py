from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        size = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        directions = (-1, 0, 1)
        while queue:
            row, column, distance = queue.popleft()
            if row == size - 1 and column == size - 1:
                return distance
            for row_change in directions:
                for column_change in directions:
                    next_row = row + row_change
                    next_column = column + column_change
                    if (
                        0 <= next_row < size
                        and 0 <= next_column < size
                        and not grid[next_row][next_column]
                    ):
                        grid[next_row][next_column] = 1
                        queue.append((next_row, next_column, distance + 1))
        return -1


if __name__ == "__main__":
    test_cases = [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[0]], 1),
        ([[1]], -1),
        ([[0, 0], [0, 1]], -1),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().shortestPathBinaryMatrix(grid) == expected
