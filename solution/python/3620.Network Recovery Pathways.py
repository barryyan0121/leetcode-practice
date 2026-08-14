from collections import deque
from typing import List


class Solution:
    def maxPathScore(
        self, n: int, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, c in edges:
            graph[u].append((v, c))
            indeg[v] += 1

        topo = []
        q = deque([i for i in range(n) if indeg[i] == 0])
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def check(threshold: int) -> bool:
            inf = 10**30
            dist = [inf] * n
            dist[0] = 0
            for u in topo:
                if dist[u] > k:
                    continue
                if u not in (0, n - 1) and not online[u]:
                    continue
                for v, c in graph[u]:
                    if c < threshold:
                        continue
                    if v not in (0, n - 1) and not online[v]:
                        continue
                    nd = dist[u] + c
                    if nd < dist[v]:
                        dist[v] = nd
            return dist[n - 1] <= k

        cand = sorted({c for _, _, c in edges})
        if not check(cand[0]):
            return -1
        lo, hi = 0, len(cand) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(cand[mid]):
                lo = mid
            else:
                hi = mid - 1
        return cand[lo]


if __name__ == "__main__":
    s = Solution()
    assert (
        s.maxPathScore(
            4,
            [[0, 1, 5], [1, 3, 10], [0, 2, 3], [2, 3, 4]],
            [True, True, True, True],
            10,
        )
        == 3
    )
    assert (
        s.maxPathScore(
            5,
            [[0, 1, 7], [1, 4, 5], [0, 2, 6], [2, 3, 6], [3, 4, 2], [2, 4, 6]],
            [True, True, True, False, True],
            12,
        )
        == 6
    )
    print("3620 ok")
