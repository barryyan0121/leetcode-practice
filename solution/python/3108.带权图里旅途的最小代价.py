class Solution:
    def minimumCost(
        self, n: int, edges: list[list[int]], query: list[list[int]]
    ) -> list[int]:
        parent = list(range(n))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for start, end, _ in edges:
            root_start, root_end = find(start), find(end)
            if root_start != root_end:
                parent[root_end] = root_start

        component_cost = {}
        for start, end, weight in edges:
            root = find(start)
            component_cost[root] = component_cost.get(root, -1) & weight

        answer = []
        for start, end in query:
            root_start, root_end = find(start), find(end)
            answer.append(component_cost[root_start] if root_start == root_end else -1)
        return answer


if __name__ == "__main__":
    test_cases = [
        (5, [[0, 1, 7], [1, 3, 7], [1, 2, 1]], [[0, 2], [2, 4]], [1, -1]),
        (3, [[0, 2, 7], [0, 1, 15], [1, 2, 6]], [[1, 2]], [6]),
    ]
    for _, (n, edges, query, expected) in enumerate(test_cases):
        assert Solution().minimumCost(n, edges, query) == expected
