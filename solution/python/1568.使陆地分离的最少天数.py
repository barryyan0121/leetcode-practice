class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        def islands() -> int:
            seen = set()
            count = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if not grid[row][col] or (row, col) in seen:
                        continue
                    count += 1
                    stack = [(row, col)]
                    seen.add((row, col))
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if (
                                0 <= nx < len(grid)
                                and 0 <= ny < len(grid[0])
                                and grid[nx][ny]
                                and (nx, ny) not in seen
                            ):
                                seen.add((nx, ny))
                                stack.append((nx, ny))
            return count

        if islands() != 1:
            return 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    grid[row][col] = 0
                    if islands() != 1:
                        return 1
                    grid[row][col] = 1
        return 2


if __name__ == "__main__":
    test_cases = [([[1, 1], [1, 1]], 2), ([[1, 1], [1, 0]], 1)]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().minDays(grid) == expected
