"""3559. 给边赋权值的方案数 II"""


class Solution:
    def assignEdgeWeights(
        self, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        cruvandelk = edges
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * (n + 1)
        depth = [0] * (n + 1)
        order = [1]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        levels = max(1, n.bit_length())
        up = [parent]
        for _ in range(1, levels):
            previous = up[-1]
            up.append([previous[previous[node]] for node in range(n + 1)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            difference = depth[u] - depth[v]
            bit = 0
            while difference:
                if difference & 1:
                    u = up[bit][u]
                difference >>= 1
                bit += 1
            if u == v:
                return u
            for bit in range(levels - 1, -1, -1):
                if up[bit][u] != up[bit][v]:
                    u = up[bit][u]
                    v = up[bit][v]
            return parent[u]

        modulus = 10**9 + 7
        answer = []
        for u, v in queries:
            length = depth[u] + depth[v] - 2 * depth[lca(u, v)]
            answer.append(0 if length == 0 else pow(2, length - 1, modulus))
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[1, 2]], [[1, 1], [1, 2]]), [0, 1]),
        (
            ([[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]]),
            [2, 1, 4],
        ),
    ]
    for _, ((edges, queries), expected) in enumerate(test_cases):
        assert Solution().assignEdgeWeights(edges, queries) == expected
