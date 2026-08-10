"""2812. 找出最安全路径"""

from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        distance = [[-1] * n for _ in range(n)]
        queue = deque()
        for row in range(n):
            for column in range(n):
                if grid[row][column]:
                    distance[row][column] = 0
                    queue.append((row, column))
        while queue:
            row, column = queue.popleft()
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if 0 <= next_row < n and 0 <= next_column < n:
                    if distance[next_row][next_column] == -1:
                        distance[next_row][next_column] = distance[row][column] + 1
                        queue.append((next_row, next_column))
        heap = [(-distance[0][0], 0, 0)]
        seen = {(0, 0)}
        while heap:
            safety, row, column = heapq.heappop(heap)
            safety = -safety
            if (row, column) == (n - 1, n - 1):
                return safety
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if 0 <= next_row < n and 0 <= next_column < n:
                    if (next_row, next_column) not in seen:
                        seen.add((next_row, next_column))
                        next_safety = min(safety, distance[next_row][next_column])
                        heapq.heappush(heap, (-next_safety, next_row, next_column))
        return 0


if __name__ == "__main__":
    assert Solution().maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0
