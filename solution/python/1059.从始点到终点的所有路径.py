class Solution:
    def leadsToDestination(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
        state = [0] * n

        def dfs(node):
            if not graph[node]:
                return node == destination
            if state[node]:
                return state[node] == 2
            state[node] = 1
            if not all(dfs(next_node) for next_node in graph[node]):
                return False
            state[node] = 2
            return True

        return dfs(source)


if __name__ == "__main__":
    test_cases = [(4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3, True)]
    for _, (n, edges, source, destination, expected) in enumerate(test_cases):
        assert Solution().leadsToDestination(n, edges, source, destination) == expected
