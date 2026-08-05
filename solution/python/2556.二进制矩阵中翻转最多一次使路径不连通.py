"""2556. 二进制矩阵中翻转最多一次使路径不连通"""


class Solution:
    def isPossibleToCutPath(self, grid: list[list[int]]) -> bool:
        def walk():
            m, n = len(grid), len(grid[0])
            if grid[0][0] == 0:
                return False
            stack = [(0, 0)]
            while stack:
                i, j = stack.pop()
                if i == m - 1 and j == n - 1:
                    return True
                if grid[i][j] == 0:
                    continue
                if (i, j) not in ((0, 0), (m - 1, n - 1)):
                    grid[i][j] = 0
                for ni, nj in ((i + 1, j), (i, j + 1)):
                    if ni < m and nj < n and grid[ni][nj]:
                        stack.append((ni, nj))
            return False

        if not walk():
            return True
        return not walk()


if __name__ == "__main__":
    test_cases = [(([[1, 1, 0], [0, 1, 1], [0, 0, 1]],), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isPossibleToCutPath(*args) == expected
