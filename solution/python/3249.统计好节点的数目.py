class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        subtree_size = [1] * n
        good_nodes = 0
        for node in reversed(order):
            child_sizes = [
                subtree_size[child] for child in graph[node] if parent[child] == node
            ]
            if not child_sizes or len(set(child_sizes)) == 1:
                good_nodes += 1
            subtree_size[node] += sum(child_sizes)
        return good_nodes


if __name__ == "__main__":
    test_cases = [
        ([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], 7),
        ([[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]], 6),
        (
            [
                [0, 1],
                [1, 2],
                [1, 3],
                [1, 4],
                [0, 5],
                [5, 6],
                [6, 7],
                [7, 8],
                [0, 9],
                [9, 10],
                [9, 12],
                [10, 11],
            ],
            12,
        ),
    ]
    for _, (edges, expected) in enumerate(test_cases):
        assert Solution().countGoodNodes(edges) == expected
