"""2290. 到达角落需要移除障碍物的最小数目"""

from collections import deque


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        distance = [[10**9] * cols for _ in range(rows)]
        distance[0][0] = 0
        queue = deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    cost = distance[i][j] + grid[ni][nj]
                    if cost < distance[ni][nj]:
                        distance[ni][nj] = cost
                        if grid[ni][nj]:
                            queue.append((ni, nj))
                        else:
                            queue.appendleft((ni, nj))
        return distance[-1][-1]


if __name__ == "__main__":
    assert Solution().minimumObstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]]) == 2
