"""2257. 统计网格图中没有被保卫的格子数"""


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, j in walls:
            grid[i][j] = 2
        for i, j in guards:
            grid[i][j] = 2
        for i, j in guards:
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                while 0 <= x < m and 0 <= y < n and grid[x][y] != 2:
                    grid[x][y] = 1
                    x += di
                    y += dj
        return sum(cell == 0 for row in grid for cell in row)
