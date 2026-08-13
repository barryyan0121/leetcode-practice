from collections import deque
from typing import List


class Solution:
    def specialNodes(
        self, n: int, edges: List[List[int]], x: int, y: int, z: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def distances(start):
            dist = [-1] * n
            dist[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for nxt in graph[node]:
                    if dist[nxt] < 0:
                        dist[nxt] = dist[node] + 1
                        queue.append(nxt)
            return dist

        dx, dy, dz = distances(x), distances(y), distances(z)
        return sum(
            (a := sorted((dx[i], dy[i], dz[i])))[0] ** 2 + a[1] ** 2 == a[2] ** 2
            for i in range(n)
        )


if __name__ == "__main__":
    assert Solution().specialNodes(4, [[0, 1], [0, 2], [0, 3]], 1, 2, 3) == 3
