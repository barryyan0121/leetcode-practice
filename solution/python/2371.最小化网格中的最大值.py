"""2371. 最小化网格中的最大值"""


class Solution:
    def minScore(self, grid: list[list[int]]) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        row_max = [0] * rows
        col_max = [0] * cols
        cells = sorted((grid[r][c], r, c) for r in range(rows) for c in range(cols))
        answer = [[0] * cols for _ in range(rows)]
        for value, row, col in cells:
            score = max(row_max[row], col_max[col]) + 1
            answer[row][col] = score
            row_max[row] = col_max[col] = score
        return answer


if __name__ == "__main__":
    assert Solution().minScore([[1, 2], [3, 4]]) == [[1, 2], [2, 3]]
