"""2852. 所有单元格的远离程度之和"""


class Solution:
    def sumRemoteness(self, grid: list[list[int]]) -> int:
        n = len(grid)
        seen = [[False] * n for _ in range(n)]
        components = []
        for row in range(n):
            for col in range(n):
                if grid[row][col] == -1 or seen[row][col]:
                    continue
                stack = [(row, col)]
                seen[row][col] = True
                total = 0
                size = 0
                while stack:
                    x, y = stack.pop()
                    total += grid[x][y]
                    size += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < n
                            and 0 <= ny < n
                            and grid[nx][ny] != -1
                            and not seen[nx][ny]
                        ):
                            seen[nx][ny] = True
                            stack.append((nx, ny))
                components.append((total, size))
        all_sum = sum(total for total, _ in components)
        return sum(size * (all_sum - total) for total, size in components)


if __name__ == "__main__":
    assert Solution().sumRemoteness([[-1, 1, -1], [5, -1, 4], [-1, 3, -1]]) == 39
    assert Solution().sumRemoteness([[-1, 3, 4], [-1, -1, -1], [3, -1, -1]]) == 13
