from heapq import heappop, heappush


class Solution:
    def minimumDistance(
        self, n: int, edges: list[list[int]], s: int, marked: list[int]
    ) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        dist = [float("inf")] * n
        dist[s] = 0
        heap = [(0, s)]
        while heap:
            d, u = heappop(heap)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heappush(heap, (dist[v], v))
        ans = min(dist[i] for i in marked)
        return -1 if ans == float("inf") else ans


if __name__ == "__main__":
    assert Solution().minimumDistance(3, [[0, 1, 2], [1, 2, 3]], 0, [2]) == 5
