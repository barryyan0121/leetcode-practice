"""2204. 无向图中到环的距离"""

from collections import deque


class Solution:
    def distanceToCycle(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        queue = deque(i for i in range(n) if degree[i] == 1)
        removed = [False] * n
        while queue:
            node = queue.popleft()
            removed[node] = True
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    queue.append(neighbor)
        distance = [-1] * n
        queue = deque(i for i in range(n) if not removed[i])
        for node in queue:
            distance[node] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        return distance


if __name__ == "__main__":
    assert Solution().distanceToCycle(
        7, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [6, 0]]
    ) == [0, 0, 0, 0, 0, 0, 1]
