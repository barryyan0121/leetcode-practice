from collections import deque


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int:
        def diameter(edges: list[list[int]]) -> int:
            graph = [[] for _ in range(len(edges) + 1)]
            for left, right in edges:
                graph[left].append(right)
                graph[right].append(left)

            def farthest(start: int) -> tuple[int, int]:
                distances = [-1] * len(graph)
                distances[start] = 0
                queue = deque([start])
                far = start
                while queue:
                    node = queue.popleft()
                    far = node
                    for neighbor in graph[node]:
                        if distances[neighbor] == -1:
                            distances[neighbor] = distances[node] + 1
                            queue.append(neighbor)
                return far, distances[far]

            far, _ = farthest(0)
            return farthest(far)[1]

        first, second = diameter(edges1), diameter(edges2)
        return max(first, second, (first + 1) // 2 + (second + 1) // 2 + 1)


if __name__ == "__main__":
    test_cases = [
        (([[0, 1], [0, 2], [0, 3]], [[0, 1]]), 3),
        (
            (
                [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
                [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
            ),
            5,
        ),
    ]
    for _, ((edges1, edges2), expected) in enumerate(test_cases):
        assert Solution().minimumDiameterAfterMerge(edges1, edges2) == expected
