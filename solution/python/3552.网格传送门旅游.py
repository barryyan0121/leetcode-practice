"""3552. 网格传送门旅游"""

from collections import defaultdict, deque


class Solution:
    def minMoves(self, matrix: list[str]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        portals = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value.isupper():
                    portals[value].append((i, j))

        queue = deque([(0, 0)])
        distance = [[-1] * cols for _ in range(rows)]
        distance[0][0] = 0
        used = set()
        while queue:
            i, j = queue.popleft()
            current = distance[i][j]
            if (i, j) == (rows - 1, cols - 1):
                return current
            value = matrix[i][j]
            if value.isupper() and value not in used:
                used.add(value)
                for ni, nj in portals[value]:
                    if distance[ni][nj] == -1 or distance[ni][nj] > current:
                        distance[ni][nj] = current
                        queue.appendleft((ni, nj))
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < rows and 0 <= nj < cols:
                    if matrix[ni][nj] != "#" and (
                        distance[ni][nj] == -1 or distance[ni][nj] > current + 1
                    ):
                        distance[ni][nj] = current + 1
                        queue.append((ni, nj))
        return -1


if __name__ == "__main__":
    test_cases = [
        ((["A..", ".A.", "..."],), 2),
        (([".#...", ".#.#.", ".#.#.", "...#."],), 13),
        (([".#", ".."],), 2),
    ]
    for _, ((matrix,), expected) in enumerate(test_cases):
        assert Solution().minMoves(matrix) == expected
