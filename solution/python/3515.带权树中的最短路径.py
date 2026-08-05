class Solution:
    def treeQueries(
        self, n: int, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        jalkimoren = edges
        graph = [[] for _ in range(n + 1)]
        weights = {}
        for u, v, weight in jalkimoren:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
            weights[(min(u, v), max(u, v))] = weight

        parent = [0] * (n + 1)
        distance = [0] * (n + 1)
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        order = 0

        def dfs(node: int, previous: int) -> None:
            nonlocal order
            parent[node] = previous
            order += 1
            tin[node] = order
            for neighbor, weight in graph[node]:
                if neighbor == previous:
                    continue
                distance[neighbor] = distance[node] + weight
                dfs(neighbor, node)
            tout[node] = order

        dfs(1, 0)
        bit = [0] * (n + 2)

        def add(index: int, value: int) -> None:
            while index <= n:
                bit[index] += value
                index += index & -index

        def range_add(left: int, right: int, value: int) -> None:
            add(left, value)
            add(right + 1, -value)

        def point_query(index: int) -> int:
            answer = 0
            while index:
                answer += bit[index]
                index -= index & -index
            return answer

        answer = []
        for query in queries:
            if query[0] == 2:
                answer.append(distance[query[1]] + point_query(tin[query[1]]))
                continue
            _, u, v, new_weight = query
            key = (min(u, v), max(u, v))
            delta = new_weight - weights[key]
            weights[key] = new_weight
            child = u if parent[u] == v else v
            range_add(tin[child], tout[child], delta)
        return answer


if __name__ == "__main__":
    test_cases = [
        ((2, [[1, 2, 7]], [[2, 2], [1, 1, 2, 4], [2, 2]]), [7, 4]),
        (
            (3, [[1, 2, 2], [1, 3, 4]], [[2, 1], [2, 3], [1, 1, 3, 7], [2, 2], [2, 3]]),
            [0, 4, 2, 7],
        ),
    ]
    for _, ((n, edges, queries), expected) in enumerate(test_cases):
        assert Solution().treeQueries(n, edges, queries) == expected
