"""2556. 二进制矩阵中翻转最多一次使路径不连通"""


class Solution:
    def isPossibleToCutPath(self, grid: list[list[int]]) -> bool:
        def walk() -> bool:
            m, n = len(grid), len(grid[0])
            parent = [[None] * n for _ in range(m)]
            stack = [(0, 0)]
            parent[0][0] = (0, 0)
            while stack:
                row, column = stack.pop()
                if row == m - 1 and column == n - 1:
                    current = (row, column)
                    while current != (0, 0):
                        if current != (m - 1, n - 1):
                            grid[current[0]][current[1]] = 0
                        current = parent[current[0]][current[1]]
                    return True
                for next_row, next_column in ((row + 1, column), (row, column + 1)):
                    if (
                        next_row < m
                        and next_column < n
                        and grid[next_row][next_column]
                        and parent[next_row][next_column] is None
                    ):
                        parent[next_row][next_column] = (row, column)
                        stack.append((next_row, next_column))
            return False

        if not grid[0][0] or not walk():
            return True
        return not walk()


if __name__ == "__main__":
    test_cases = [(([[1, 1, 0], [0, 1, 1], [0, 0, 1]],), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isPossibleToCutPath(*args) == expected
