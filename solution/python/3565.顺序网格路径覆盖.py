"""3565. 顺序网格路径覆盖"""


class Solution:
    def findPath(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        path = []
        seen = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def search(row, col, previous):
            seen.add((row, col))
            path.append([row, col])
            if len(path) == rows * cols:
                return True
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                    value = grid[nr][nc]
                    if (
                        value == 0
                        and search(nr, nc, previous)
                        or value == previous + 1
                        and search(nr, nc, value)
                    ):
                        return True
            seen.remove((row, col))
            path.pop()
            return False

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] in (0, 1) and search(row, col, grid[row][col]):
                    return path
        return []


if __name__ == "__main__":
    test_cases = [
        (([[0, 0, 0], [0, 1, 2]], 2), [[0, 0], [1, 0], [1, 1], [1, 2], [0, 2], [0, 1]]),
        (([[1, 0, 4], [3, 0, 2]], 4), []),
    ]
    for _, ((grid, k), expected) in enumerate(test_cases):
        result = Solution().findPath(grid, k)
        assert result == expected or (expected and len(result) == len(expected))
