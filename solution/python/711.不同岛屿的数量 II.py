"""711. 不同岛屿的数量 II"""


class Solution:
    def numDistinctIslands2(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        shapes = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                stack = [(row, col)]
                grid[row][col] = 0
                points = []
                while stack:
                    x, y = stack.pop()
                    points.append((x - row, y - col))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
                forms = []
                for swap in (False, True):
                    for sx, sy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                        form = []
                        for x, y in points:
                            a, b = (y, x) if swap else (x, y)
                            form.append((a * sx, b * sy))
                        min_x = min(x for x, _ in form)
                        min_y = min(y for _, y in form)
                        forms.append(
                            tuple(sorted((x - min_x, y - min_y) for x, y in form))
                        )
                shapes.add(min(forms))
        return len(shapes)


if __name__ == "__main__":
    assert (
        Solution().numDistinctIslands2(
            [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]
        )
        == 1
    )
