"""2045. 到达目的地的第二短时间"""

import heapq


class Solution:
    def secondMinimum(
        self, n: int, edges: list[list[int]], time: int, change: int
    ) -> int:
        graph = [[] for _ in range(n + 1)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        distances = [[10**30, 10**30] for _ in range(n + 1)]
        distances[1][0] = 0
        queue = [(0, 1)]
        while queue:
            current, node = heapq.heappop(queue)
            for neighbor in graph[node]:
                wait = 0
                if (current // change) % 2:
                    wait = change - current % change
                arrival = current + wait + time
                if arrival < distances[neighbor][0]:
                    distances[neighbor][0] = arrival
                    heapq.heappush(queue, (arrival, neighbor))
                elif distances[neighbor][0] < arrival < distances[neighbor][1]:
                    distances[neighbor][1] = arrival
                    heapq.heappush(queue, (arrival, neighbor))
        return distances[n][1]


if __name__ == "__main__":
    test_cases = [((5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5), 13)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().secondMinimum(*args) == expected
