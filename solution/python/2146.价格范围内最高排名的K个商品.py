"""2146. 价格范围内最高排名的 K 个商品"""

from collections import deque
import heapq


class Solution:
    def highestRankedKItems(
        self, grid: list[list[int]], pricing: list[int], start: list[int], k: int
    ) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        low, high = pricing
        queue = deque([(start[0], start[1], 0)])
        seen = {tuple(start)}
        heap = []
        while queue:
            row, col, distance = queue.popleft()
            value = grid[row][col]
            if low <= value <= high:
                heapq.heappush(heap, (distance, value, row, col))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc]
                    and (nr, nc) not in seen
                ):
                    seen.add((nr, nc))
                    queue.append((nr, nc, distance + 1))
        return [[row, col] for _, _, row, col in sorted(heap)[:k]]


if __name__ == "__main__":
    test_cases = [
        (
            ([[1, 2, 0], [1, 3, 4], [0, 5, 6]], [2, 5], [0, 0], 3),
            [[0, 1], [1, 1], [1, 2]],
        )
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().highestRankedKItems(*args) == expected
