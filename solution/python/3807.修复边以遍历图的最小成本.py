from collections import deque
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        weights = sorted(w for _, _, w in edges)

        def reachable(limit: int) -> bool:
            graph = [[] for _ in range(n)]
            for u, v, w in edges:
                if w <= limit:
                    graph[u].append(v)
                    graph[v].append(u)
            dist = [-1] * n
            dist[0] = 0
            queue = deque([0])
            while queue:
                u = queue.popleft()
                if u == n - 1:
                    return dist[u] <= k
                if dist[u] == k:
                    continue
                for v in graph[u]:
                    if dist[v] < 0:
                        dist[v] = dist[u] + 1
                        queue.append(v)
            return False

        if not reachable(weights[-1]):
            return -1
        lo, hi = 0, len(weights) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if reachable(weights[mid]):
                hi = mid
            else:
                lo = mid + 1
        return weights[lo]


if __name__ == "__main__":
    s = Solution()
    assert s.minCost(3, [[0, 1, 10], [1, 2, 10], [0, 2, 100]], 1) == 100
    assert s.minCost(6, [[0, 2, 5], [2, 3, 6], [3, 4, 7], [4, 5, 5], [0, 1, 10], [1, 5, 12], [0, 3, 9], [1, 2, 8], [2, 4, 11]], 2) == 12
    assert s.minCost(3, [[0, 1, 1]], 1) == -1
