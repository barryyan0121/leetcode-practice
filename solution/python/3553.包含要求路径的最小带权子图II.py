"""3553. 包含要求路径的最小带权子图 II"""


class Solution:
    def minimumWeight(
        self, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        depth = [0] * n
        distance = [0] * n
        parent = [0] * n
        order = [0]
        for u in order:
            for v, weight in graph[u]:
                if v == parent[u] and u != 0:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                distance[v] = distance[u] + weight
                order.append(v)

        levels = max(1, n.bit_length())
        up = [parent]
        for level in range(1, levels):
            previous = up[-1]
            up.append([previous[previous[node]] for node in range(n)])

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
            for level in range(levels - 1, -1, -1):
                if up[level][u] != up[level][v]:
                    u = up[level][u]
                    v = up[level][v]
            return parent[u]

        def path_distance(u, v):
            ancestor = lca(u, v)
            return distance[u] + distance[v] - 2 * distance[ancestor]

        answer = []
        for src1, src2, dest in queries:
            answer.append(
                (
                    path_distance(src1, src2)
                    + path_distance(src1, dest)
                    + path_distance(src2, dest)
                )
                // 2
            )
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            (
                [[0, 1, 2], [1, 2, 3], [1, 3, 1]],
                [[2, 3, 0], [2, 3, 1]],
            ),
            [6, 4],
        ),
    ]
    for _, ((edges, queries), expected) in enumerate(test_cases):
        assert Solution().minimumWeight(edges, queries) == expected
