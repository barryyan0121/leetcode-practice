from collections import deque
from typing import List


class Solution:
    def findSpecialNodes(self, n: int, edges: List[List[int]]) -> str:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def farthest(start: int) -> list[int]:
            dist = [-1] * n
            dist[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if dist[v] < 0:
                        dist[v] = dist[u] + 1
                        queue.append(v)
            best = max(dist)
            return [i for i, d in enumerate(dist) if d == best]

        left = farthest(0)
        right = farthest(left[0])
        special = set(left) | set(right)
        return "".join("1" if i in special else "0" for i in range(n))


if __name__ == "__main__":
    solution = Solution()
    assert solution.findSpecialNodes(3, [[0, 1], [1, 2]]) == "101"
    assert (
        solution.findSpecialNodes(7, [[0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [1, 6]])
        == "1000111"
    )
    assert solution.findSpecialNodes(2, [[0, 1]]) == "11"
