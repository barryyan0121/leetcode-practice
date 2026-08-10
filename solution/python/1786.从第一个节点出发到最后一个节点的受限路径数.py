from collections import defaultdict
import heapq
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        distance = [float("inf")] * (n + 1)
        distance[n] = 0
        heap = [(0, n)]
        while heap:
            dist, node = heapq.heappop(heap)
            if dist != distance[node]:
                continue
            for nxt, weight in graph[node]:
                candidate = dist + weight
                if candidate < distance[nxt]:
                    distance[nxt] = candidate
                    heapq.heappush(heap, (candidate, nxt))
        mod = 10**9 + 7
        order = sorted(range(1, n + 1), key=distance.__getitem__)
        ways = [0] * (n + 1)
        ways[n] = 1
        for node in order:
            for nxt, _ in graph[node]:
                if distance[nxt] < distance[node]:
                    ways[node] = (ways[node] + ways[nxt]) % mod
        return ways[1]


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.countRestrictedPaths(
            5,
            [
                [1, 2, 3],
                [1, 3, 3],
                [2, 3, 1],
                [1, 4, 2],
                [5, 2, 2],
                [3, 5, 1],
                [5, 4, 10],
            ],
        )
        == 3
    )
    print("1786 passed")
