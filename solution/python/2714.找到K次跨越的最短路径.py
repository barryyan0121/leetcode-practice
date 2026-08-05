from heapq import heappop, heappush


class Solution:
    def shortestPathWithHops(
        self, n: int, edges: list[list[int]], s: int, t: int, k: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))
        dist = [[float("inf")] * (k + 1) for _ in range(n)]
        dist[s][0] = 0
        heap = [(0, s, 0)]
        while heap:
            d, u, h = heappop(heap)
            if d != dist[u][h]:
                continue
            for v, w in graph[u]:
                for nh, nd in ((h, d + w), (h + 1, d)):
                    if nh <= k and nd < dist[v][nh]:
                        dist[v][nh] = nd
                        heappush(heap, (nd, v, nh))
        return min(dist[t])


if __name__ == "__main__":
    assert (
        Solution().shortestPathWithHops(3, [[0, 1, 5], [1, 2, 5], [0, 2, 20]], 0, 2, 1)
        == 0
    )
