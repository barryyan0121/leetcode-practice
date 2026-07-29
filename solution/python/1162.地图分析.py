from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        size = len(grid)
        queue = deque(
            (row, col) for row in range(size) for col in range(size) if grid[row][col]
        )
        if not queue or len(queue) == size * size:
            return -1
        distance = -1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if (
                        0 <= next_row < size
                        and 0 <= next_col < size
                        and not grid[next_row][next_col]
                    ):
                        grid[next_row][next_col] = 1
                        queue.append((next_row, next_col))
        return distance


if __name__ == "__main__":
    test_cases = [([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 2), ([[1, 1], [1, 1]], -1)]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().maxDistance(grid) == expected
