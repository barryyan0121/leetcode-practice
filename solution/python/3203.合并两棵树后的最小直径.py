from collections import deque


class Solution:
    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        def diameter(edges: list[list[int]]) -> int:
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)

            def bfs(start: int) -> tuple[int, int]:
                q = deque([start])
                dist = [-1] * n
                dist[start] = 0
                far = start
                while q:
                    u = q.popleft()
                    far = u
                    for v in g[u]:
                        if dist[v] == -1:
                            dist[v] = dist[u] + 1
                            q.append(v)
                return far, dist[far]

            a, _ = bfs(0)
            _, d = bfs(a)
            return d

        d1 = diameter(edges1)
        d2 = diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)


if __name__ == "__main__":
    assert Solution().minimumDiameterAfterMerge([[0, 1], [0, 2], [0, 3]], [[0, 1]]) == 3
    assert Solution().minimumDiameterAfterMerge([[0, 1]], [[0, 1], [1, 2]]) == 3
