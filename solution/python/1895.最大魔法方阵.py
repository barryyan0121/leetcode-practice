"""1895. 最大魔法方阵"""


class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_sum = [[0] * (cols + 1) for _ in range(rows)]
        col_sum = [[0] * (rows + 1) for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                col_sum[j][i + 1] = col_sum[j][i] + grid[i][j]
        for size in range(min(rows, cols), 0, -1):
            for top in range(rows - size + 1):
                for left in range(cols - size + 1):
                    target = row_sum[top][left + size] - row_sum[top][left]
                    if any(
                        row_sum[i][left + size] - row_sum[i][left] != target
                        for i in range(top, top + size)
                    ):
                        continue
                    if any(
                        col_sum[j][top + size] - col_sum[j][top] != target
                        for j in range(left, left + size)
                    ):
                        continue
                    if sum(grid[top + d][left + d] for d in range(size)) != target:
                        continue
                    if (
                        sum(grid[top + d][left + size - 1 - d] for d in range(size))
                        == target
                    ):
                        return size
        return 1


if __name__ == "__main__":
    assert (
        Solution().largestMagicSquare(
            [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
        )
        == 3
    )
