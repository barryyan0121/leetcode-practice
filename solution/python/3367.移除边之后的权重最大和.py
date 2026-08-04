class Solution:
    def maximizeSumOfWeights(self, edges: list[list[int]], k: int) -> int:
        node_count = len(edges) + 1
        graph = [[] for _ in range(node_count)]
        for left, right, weight in edges:
            graph[left].append((right, weight))
            graph[right].append((left, weight))

        parent = [-1] * node_count
        order = [0]
        for node in order:
            for neighbor, _ in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        free = [0] * node_count
        occupied = [0] * node_count
        for node in reversed(order):
            base = 0
            gains = []
            for child, weight in graph[node]:
                if parent[child] == node:
                    base += free[child]
                    gains.append(weight + occupied[child] - free[child])
            gains.sort(reverse=True)
            free[node] = base + sum(gain for gain in gains[:k] if gain > 0)
            occupied[node] = base + sum(
                gain for gain in gains[: max(0, k - 1)] if gain > 0
            )
        return free[0]


if __name__ == "__main__":
    test_cases = [
        (([[0, 1, 4], [0, 2, 2], [2, 3, 12], [2, 4, 6]], 2), 22),
        (
            ([[0, 1, 5], [1, 2, 10], [0, 3, 15], [3, 4, 20], [3, 5, 5], [0, 6, 10]], 3),
            65,
        ),
    ]
    for _, ((edges, k), expected) in enumerate(test_cases):
        assert Solution().maximizeSumOfWeights(edges, k) == expected
