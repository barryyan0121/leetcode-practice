"""2328. 网格图中递增路径的数目"""


class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        mod = 1_000_000_007
        rows, cols = len(grid), len(grid[0])
        cells = sorted((grid[i][j], i, j) for i in range(rows) for j in range(cols))
        dp = [[1] * cols for _ in range(rows)]
        for _, i, j in cells:
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] > grid[i][j]:
                    dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % mod
        return sum(map(sum, dp)) % mod

if __name__ == "__main__":
    assert Solution().countPaths([[1,1],[3,4]]) == 8
