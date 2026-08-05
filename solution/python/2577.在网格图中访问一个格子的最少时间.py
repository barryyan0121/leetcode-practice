"""2577. 在网格图中访问一个格子的最少时间"""


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        import heapq

        m, n = len(grid), len(grid[0])
        if m > 1 and n > 1 and grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        heap = [(0, 0, 0)]
        best = [[float("inf")] * n for _ in range(m)]
        best[0][0] = 0
        while heap:
            time, i, j = heapq.heappop(heap)
            if (i, j) == (m - 1, n - 1):
                return time
            if time != best[i][j]:
                continue
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    next_time = max(time + 1, grid[ni][nj])
                    if (next_time - time) % 2 == 0:
                        next_time += 1
                    if next_time < best[ni][nj]:
                        best[ni][nj] = next_time
                        heapq.heappush(heap, (next_time, ni, nj))
        return -1


if __name__ == "__main__":
    test_cases = [(([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]],), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumTime(*args) == expected
