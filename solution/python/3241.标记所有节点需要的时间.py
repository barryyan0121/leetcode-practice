class Solution:
    def timeTaken(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        weight = [1 if node % 2 else 2 for node in range(n)]
        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        down = [0] * n
        for node in reversed(order):
            down[node] = max(
                (
                    down[child] + weight[child]
                    for child in graph[node]
                    if parent[child] == node
                ),
                default=0,
            )

        up = [0] * n
        answer = [0] * n
        for node in order:
            best = [0, 0]
            best_child = [-1, -1]
            for child in graph[node]:
                if parent[child] == node:
                    candidate = down[child] + weight[child]
                    if candidate > best[0]:
                        best[1], best_child[1] = best[0], best_child[0]
                        best[0], best_child[0] = candidate, child
                    elif candidate > best[1]:
                        best[1], best_child[1] = candidate, child

            answer[node] = max(up[node], best[0])
            for child in graph[node]:
                if parent[child] == node:
                    outside = best[1] if best_child[0] == child else best[0]
                    up[child] = weight[node] + max(up[node], outside)
        return answer


if __name__ == "__main__":
    test_cases = [
        ([[0, 1], [0, 2]], [2, 4, 3]),
        ([[0, 1]], [1, 2]),
        ([[2, 4], [0, 1], [2, 3], [0, 2]], [4, 6, 3, 5, 5]),
    ]
    for _, (edges, expected) in enumerate(test_cases):
        assert Solution().timeTaken(edges) == expected
