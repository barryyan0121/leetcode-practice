class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows, columns = len(grid), len(grid[0])
        column_sums = [0] * columns
        answer = 0
        for row in grid:
            row_sum = 0
            for column, value in enumerate(row):
                row_sum += value
                column_sums[column] += row_sum
                answer += column_sums[column] <= k
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[7, 6, 3], [6, 6, 1]], 18), 4),
        (([[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20), 6),
    ]
    for _, ((grid, k), expected) in enumerate(test_cases):
        assert Solution().countSubmatrices(grid, k) == expected
