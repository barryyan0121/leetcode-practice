"""2093. 到达城市的最小费用"""

import heapq


class Solution:
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]
        for x, y, toll in highways:
            graph[x].append((y, toll))
            graph[y].append((x, toll))
        distance = [[float("inf")] * (discounts + 1) for _ in range(n)]
        distance[0][0] = 0
        queue = [(0, 0, 0)]
        while queue:
            cost, node, used = heapq.heappop(queue)
            if cost != distance[node][used]:
                continue
            if node == n - 1:
                return cost
            for neighbor, toll in graph[node]:
                if cost + toll < distance[neighbor][used]:
                    distance[neighbor][used] = cost + toll
                    heapq.heappush(queue, (cost + toll, neighbor, used))
                if used < discounts and cost + toll // 2 < distance[neighbor][used + 1]:
                    distance[neighbor][used + 1] = cost + toll // 2
                    heapq.heappush(queue, (cost + toll // 2, neighbor, used + 1))
        return -1


if __name__ == "__main__":
    test_cases = [((3, [[0, 1, 10], [1, 2, 10], [0, 2, 100]], 1), 15)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumCost(*args) == expected
