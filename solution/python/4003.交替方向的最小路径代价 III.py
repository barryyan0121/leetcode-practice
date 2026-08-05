"""4003. 交替方向的最小路径代价 III"""

import heapq


class Solution:
    def minCost(self, m: int, n: int, penalty: list[list[int]]) -> int:
        infinity = 10**30
        distance = [[[infinity] * n for _ in range(m)] for _ in range(2)]
        distance[1][0][0] = 1
        queue = [(1, 0, 0, 1)]
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 0))
        while queue:
            cost, row, column, turn = heapq.heappop(queue)
            if cost != distance[turn][row][column]:
                continue
            if row == m - 1 and column == n - 1:
                return cost
            for dr, dc in moves:
                next_row, next_column = row + dr, column + dc
                if not (0 <= next_row < m and 0 <= next_column < n):
                    continue
                allowed = (turn == 1 and (dr, dc) in ((0, 1), (1, 0))) or (
                    turn == 0 and (dr, dc) in ((0, -1), (-1, 0))
                )
                next_cost = cost + penalty[row][column] if (dr, dc) == (0, 0) else cost
                if (dr, dc) != (0, 0):
                    next_cost += (next_row + 1) * (next_column + 1)
                    if not allowed:
                        next_cost += penalty[row][column]
                next_turn = 1 - turn
                if next_cost < distance[next_turn][next_row][next_column]:
                    distance[next_turn][next_row][next_column] = next_cost
                    heapq.heappush(queue, (next_cost, next_row, next_column, next_turn))
        return -1


if __name__ == "__main__":
    test_cases = [((2, 2, [[5, 3], [1, 4]]), 8)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
