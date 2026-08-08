class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: list[list[int]]
    ) -> list[list[int]]:
        edges = [edge + [i] for i, edge in enumerate(edges)]
        edges.sort(key=lambda edge: edge[2])

        def mst(skip: int = -1, force: int = -1) -> int:
            parent = list(range(n))

            def find(x: int) -> int:
                while x != parent[x]:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            cost = count = 0
            if force != -1:
                u, v, weight, _ = edges[force]
                parent[find(u)] = find(v)
                cost, count = weight, 1
            for i, (u, v, weight, _) in enumerate(edges):
                if i == skip:
                    continue
                root_u, root_v = find(u), find(v)
                if root_u != root_v:
                    parent[root_u] = root_v
                    cost += weight
                    count += 1
            return cost if count == n - 1 else float("inf")

        base = mst()
        critical, pseudo_critical = [], []
        for i, edge in enumerate(edges):
            if mst(skip=i) > base:
                critical.append(edge[3])
            elif mst(force=i) == base:
                pseudo_critical.append(edge[3])
        return [critical, pseudo_critical]


if __name__ == "__main__":
    test_cases = [
        (
            5,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
            [[0, 1], [2, 3, 4, 5]],
        ),
        (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]], [[], [0, 1, 2, 3]]),
    ]
    for _, (n, edges, expected) in enumerate(test_cases):
        assert Solution().findCriticalAndPseudoCriticalEdges(n, edges) == expected
