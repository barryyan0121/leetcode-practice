import heapq


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        heap = [(-grid[0][0], 0, 0)]
        visited = {(0, 0)}
        while heap:
            negative_score, row, column = heapq.heappop(heap)
            score = -negative_score
            if row == rows - 1 and column == columns - 1:
                return score
            for row_change, column_change in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row, next_column = row + row_change, column + column_change
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and (next_row, next_column) not in visited
                ):
                    visited.add((next_row, next_column))
                    next_score = min(score, grid[next_row][next_column])
                    heapq.heappush(heap, (-next_score, next_row, next_column))
        return -1


if __name__ == "__main__":
    test_cases = [
        ([[5, 4, 5], [1, 2, 6], [7, 4, 6]], 4),
        (
            [
                [2, 2, 1, 2, 2],
                [1, 2, 2, 2, 1],
                [1, 2, 2, 2, 1],
                [1, 2, 2, 2, 1],
                [1, 1, 1, 2, 2],
            ],
            2,
        ),
        ([[7]], 7),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().maximumMinimumPath(grid) == expected
