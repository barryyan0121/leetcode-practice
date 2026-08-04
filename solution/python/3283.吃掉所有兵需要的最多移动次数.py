from collections import deque
from functools import cache


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: list[list[int]]) -> int:
        points = [(kx, ky), *(tuple(position) for position in positions)]
        moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        distances = [[0] * len(points) for _ in points]
        for source, (start_x, start_y) in enumerate(points):
            distance = [[-1] * 50 for _ in range(50)]
            distance[start_x][start_y] = 0
            queue = deque([(start_x, start_y)])
            while queue:
                x, y = queue.popleft()
                for dx, dy in moves:
                    next_x, next_y = x + dx, y + dy
                    if (
                        0 <= next_x < 50
                        and 0 <= next_y < 50
                        and distance[next_x][next_y] == -1
                    ):
                        distance[next_x][next_y] = distance[x][y] + 1
                        queue.append((next_x, next_y))
            for target, (x, y) in enumerate(points):
                distances[source][target] = distance[x][y]

        count = len(positions)
        full_mask = (1 << count) - 1

        @cache
        def search(mask: int, current: int) -> int:
            if mask == full_mask:
                return 0
            choices = [
                distances[current][next_pawn]
                + search(mask | (1 << (next_pawn - 1)), next_pawn)
                for next_pawn in range(1, count + 1)
                if not mask >> (next_pawn - 1) & 1
            ]
            return max(choices) if mask.bit_count() % 2 == 0 else min(choices)

        return search(0, 0)


if __name__ == "__main__":
    test_cases = [
        ((1, 1, [[0, 0]]), 4),
        ((0, 2, [[1, 1], [2, 2], [3, 3]]), 8),
        ((0, 0, [[1, 2], [2, 4]]), 3),
    ]
    for _, ((kx, ky, positions), expected) in enumerate(test_cases):
        assert Solution().maxMoves(kx, ky, positions) == expected
