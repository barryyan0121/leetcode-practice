from collections import deque


class Solution:
    def constructGridLayout(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        def distances(start: int) -> list[int]:
            result = [-1] * n
            result[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if result[neighbor] == -1:
                        result[neighbor] = result[node] + 1
                        queue.append(neighbor)
            return result

        if n == 1:
            return [[0]]
        endpoints = [node for node in range(n) if len(graph[node]) == 1]
        if len(endpoints) == 2:
            start = endpoints[0]
            previous = -1
            row = []
            while start != -1:
                row.append(start)
                next_nodes = [
                    neighbor for neighbor in graph[start] if neighbor != previous
                ]
                previous, start = start, next_nodes[0] if next_nodes else -1
            return [row]

        corners = [node for node in range(n) if len(graph[node]) == 2]
        first_corner = corners[0]
        first_distances = distances(first_corner)
        opposite = max(corners, key=lambda node: first_distances[node])
        adjacent = [
            node for node in corners if node != first_corner and node != opposite
        ]
        second_corner = adjacent[0]
        third_corner = adjacent[1]
        height = first_distances[second_corner] + 1
        width = first_distances[third_corner] + 1
        second_distances = distances(second_corner)

        grid = [[-1] * width for _ in range(height)]
        for node in range(n):
            row = (first_distances[node] - second_distances[node] + height - 1) // 2
            column = first_distances[node] - row
            grid[row][column] = node
        return grid


if __name__ == "__main__":
    test_cases = [
        ((4, [[0, 1], [1, 2], [2, 3]]), [[0, 1, 2, 3]]),
        ((4, [[0, 1], [0, 2], [1, 3], [2, 3]]), [[0, 1], [2, 3]]),
    ]
    for _, ((n, edges), expected) in enumerate(test_cases):
        result = Solution().constructGridLayout(n, edges)
        assert {node for row in result for node in row} == set(range(n))
