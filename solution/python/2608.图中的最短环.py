"""2608. 图中的最短环"""


class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        from collections import deque

        graph = [[] for _ in range(n)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        answer = 10**9
        for start in range(n):
            distance = [-1] * n
            parent = [-1] * n
            distance[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distance[neighbor] == -1:
                        distance[neighbor] = distance[node] + 1
                        parent[neighbor] = node
                        queue.append(neighbor)
                    elif parent[node] != neighbor:
                        answer = min(answer, distance[node] + distance[neighbor] + 1)
        return -1 if answer == 10**9 else answer


if __name__ == "__main__":
    test_cases = [((7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findShortestCycle(*args) == expected
