from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for first, second in paths:
            graph[first - 1].append(second - 1)
            graph[second - 1].append(first - 1)
        colors = [0] * n
        for garden, neighbors in enumerate(graph):
            used = {colors[neighbor] for neighbor in neighbors}
            colors[garden] = next(color for color in range(1, 5) if color not in used)
        return colors


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (3, [[1, 2], [2, 3], [3, 1]], [1, 2, 3]),
        (4, [[1, 2], [2, 3], [3, 4]], [1, 2, 1, 2]),
    ]
    for _, (n, paths, expected) in enumerate(test_cases):
        assert solution.gardenNoAdj(n, paths) == expected
