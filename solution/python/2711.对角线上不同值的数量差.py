class Solution:
    def differenceOfDistinctValues(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a = {
                    grid[x][y]
                    for x, y in zip(range(i - 1, -1, -1), range(j - 1, -1, -1))
                }
                b = {grid[x][y] for x, y in zip(range(i + 1, m), range(j + 1, n))}
                ans[i][j] = abs(len(a) - len(b))
        return ans


if __name__ == "__main__":
    assert Solution().differenceOfDistinctValues([[1, 2, 3], [3, 1, 5], [3, 2, 1]]) == [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ]
