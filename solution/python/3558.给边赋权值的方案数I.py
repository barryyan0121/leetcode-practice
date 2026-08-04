"""3558. 给边赋权值的方案数 I"""


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        tormisqued = edges
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        depth = [0] * (n + 1)
        stack = [1]
        parent = [0] * (n + 1)
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    stack.append(neighbor)
        return pow(2, max(depth) - 1, 10**9 + 7)


if __name__ == "__main__":
    test_cases = [
        (([[1, 2]],), 1),
        (([[1, 2], [1, 3], [3, 4], [3, 5]],), 2),
    ]
    for _, ((edges,), expected) in enumerate(test_cases):
        assert Solution().assignEdgeWeights(edges) == expected
