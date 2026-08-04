from collections import deque


class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        rows, columns = len(grid), len(grid[0])
        distance = [[10**9] * columns for _ in range(rows)]
        distance[0][0] = grid[0][0]
        queue = deque([(0, 0)])
        while queue:
            row, column = queue.popleft()
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if 0 <= next_row < rows and 0 <= next_column < columns:
                    cost = distance[row][column] + grid[next_row][next_column]
                    if cost < distance[next_row][next_column]:
                        distance[next_row][next_column] = cost
                        if grid[next_row][next_column]:
                            queue.append((next_row, next_column))
                        else:
                            queue.appendleft((next_row, next_column))
        return distance[-1][-1] < health


if __name__ == "__main__":
    test_cases = [
        (([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1), True),
        (
            (
                [
                    [0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0],
                    [0, 1, 1, 1, 0, 1],
                    [0, 0, 1, 0, 1, 0],
                ],
                3,
            ),
            False,
        ),
        (([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5), True),
    ]
    for _, ((grid, health), expected) in enumerate(test_cases):
        assert Solution().findSafeWalk(grid, health) == expected
