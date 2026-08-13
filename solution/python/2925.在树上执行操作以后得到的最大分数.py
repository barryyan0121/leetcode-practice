class Solution:
    def maximumScoreAfterOperations(
        self, edges: list[list[int]], values: list[int]
    ) -> int:
        n = len(values)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def loss(node: int, parent: int) -> int:
            children = [child for child in graph[node] if child != parent]
            if not children:
                return values[node]
            return min(values[node], sum(loss(child, node) for child in children))

        return sum(values) - loss(0, -1)


if __name__ == "__main__":
    assert (
    Solution().maximumScoreAfterOperations(
        [[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]], [5, 2, 5, 2, 1, 1]
    )
    == 11
    )
