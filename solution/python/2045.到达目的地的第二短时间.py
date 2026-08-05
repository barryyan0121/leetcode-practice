"""2045. 到达目的地的第二短时间"""

from collections import deque


class Solution:
    def secondMinimum(
        self, n: int, edges: list[list[int]], time: int, change: int
    ) -> int:
        graph = [[] for _ in range(n + 1)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        best = [[float("inf"), float("inf")] for _ in range(n + 1)]
        best[1][0] = 0
        queue = deque([(1, 0)])
        while queue:
            node, current = queue.popleft()
            if node == n and best[node][1] < float("inf"):
                return best[node][1]
            for neighbor in graph[node]:
                departure = current
                if departure // change % 2:
                    departure += change - departure % change
                arrival = departure + time
                if arrival < best[neighbor][0]:
                    best[neighbor][0] = arrival
                    queue.append((neighbor, arrival))
                elif best[neighbor][0] < arrival < best[neighbor][1]:
                    best[neighbor][1] = arrival
                    queue.append((neighbor, arrival))


if __name__ == "__main__":
    test_cases = [((5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5), 13)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().secondMinimum(*args) == expected
