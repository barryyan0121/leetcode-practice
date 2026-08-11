class Solution:
    def lastMarkedNodes(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def distances(start: int) -> list[int]:
            distance = [-1] * n
            distance[start] = 0
            stack = [start]
            for node in stack:
                for neighbor in graph[node]:
                    if distance[neighbor] == -1:
                        distance[neighbor] = distance[node] + 1
                        stack.append(neighbor)
            return distance

        first = max(range(n), key=distances(0).__getitem__)
        from_first = distances(first)
        second = max(range(n), key=from_first.__getitem__)
        from_second = distances(second)
        return [first if from_first[node] > from_second[node] else second for node in range(n)]


if __name__ == "__main__":
    test_cases = [
        (([[0, 1], [0, 2]],), [2, 2, 1]),
        (([[0, 1]],), [1, 0]),
    ]
    for _, ((edges,), expected) in enumerate(test_cases):
        assert Solution().lastMarkedNodes(edges) == expected
