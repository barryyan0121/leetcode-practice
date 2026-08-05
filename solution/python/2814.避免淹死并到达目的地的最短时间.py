from collections import deque


class Solution:
    def minimumSeconds(self, land: list[list[str]]) -> int:
        n, m = len(land), len(land[0])
        inf = 10**9
        flood = [[inf] * m for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if land[i][j] == "*":
                    flood[i][j] = 0
                    queue.append((i, j))
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            i, j = queue.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < n
                    and 0 <= nj < m
                    and land[ni][nj] not in "XD"
                    and flood[ni][nj] == inf
                ):
                    flood[ni][nj] = flood[i][j] + 1
                    queue.append((ni, nj))
        start = next((i, j) for i in range(n) for j in range(m) if land[i][j] == "S")
        target = next((i, j) for i in range(n) for j in range(m) if land[i][j] == "D")
        dist = [[-1] * m for _ in range(n)]
        dist[start[0]][start[1]] = 0
        queue = deque([start])
        while queue:
            i, j = queue.popleft()
            if (i, j) == target:
                return dist[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                nd = dist[i][j] + 1
                if (
                    0 <= ni < n
                    and 0 <= nj < m
                    and land[ni][nj] != "X"
                    and dist[ni][nj] < 0
                    and nd < flood[ni][nj]
                ):
                    dist[ni][nj] = nd
                    queue.append((ni, nj))
        return -1


if __name__ == "__main__":
    assert (
        Solution().minimumSeconds([["D", ".", "*"], [".", ".", "."], [".", "S", "."]])
        == 3
    )
