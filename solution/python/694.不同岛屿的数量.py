"""694. 不同岛屿的数量"""


class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        shapes = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                stack = [(row, col)]
                grid[row][col] = 0
                shape = []
                while stack:
                    x, y = stack.pop()
                    shape.append((x - row, y - col))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
                shapes.add(tuple(sorted(shape)))
        return len(shapes)


if __name__ == "__main__":
    assert (
        Solution().numDistinctIslands(
            [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
        )
        == 1
    )
    assert (
        Solution().numDistinctIslands(
            [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
        )
        == 3
    )
