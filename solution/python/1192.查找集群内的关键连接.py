import sys
from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for left, right in connections:
            graph[left].append(right)
            graph[right].append(left)

        sys.setrecursionlimit(n + 10)
        order = [0] * n
        low = [0] * n
        bridges = []
        time = 0

        def visit(node: int, parent: int) -> None:
            nonlocal time
            time += 1
            order[node] = low[node] = time
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not order[neighbor]:
                    visit(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > order[node]:
                        bridges.append([node, neighbor])
                else:
                    low[node] = min(low[node], order[neighbor])

        visit(0, -1)
        return bridges


if __name__ == "__main__":
    test_cases = [(4, [[0, 1], [1, 2], [2, 0], [1, 3]], [[1, 3]])]
    for _, (n, connections, expected) in enumerate(test_cases):
        assert Solution().criticalConnections(n, connections) == expected
