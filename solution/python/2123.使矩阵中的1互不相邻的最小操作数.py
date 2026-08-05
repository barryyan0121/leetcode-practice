"""2123. 使矩阵中的 1 互不相邻的最小操作数"""

from collections import deque


class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        left_nodes = [
            (r, c)
            for r in range(rows)
            for c in range(cols)
            if grid[r][c] and (r + c) % 2 == 0
        ]
        right = {
            (r, c): index
            for index, (r, c) in enumerate(
                (
                    (r, c)
                    for r in range(rows)
                    for c in range(cols)
                    if grid[r][c] and (r + c) % 2
                )
            )
        }
        graph = [[] for _ in left_nodes]
        for index, (r, c) in enumerate(left_nodes):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (r + dr, c + dc) in right:
                    graph[index].append(right[(r + dr, c + dc)])
        match = [-1] * len(right)
        answer = 0
        for start in range(len(left_nodes)):
            seen = set()

            def augment(node):
                for neighbor in graph[node]:
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    if match[neighbor] == -1 or augment(match[neighbor]):
                        match[neighbor] = node
                        return True
                return False

            answer += augment(start)
        return answer


if __name__ == "__main__":
    test_cases = [(([[1, 1, 0], [0, 1, 1], [1, 1, 1]],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumOperations(*args) == expected
