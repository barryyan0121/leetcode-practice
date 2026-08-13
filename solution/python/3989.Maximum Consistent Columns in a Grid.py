"""3989. Maximum Consistent Columns in a Grid"""


class Solution:
    def maxColumns(self, grid: list[list[int]], limit: int) -> int:
        columns = len(grid[0])
        dp = [1] * columns
        for right in range(columns):
            for left in range(right):
                if all(abs(row[right] - row[left]) <= limit for row in grid):
                    dp[right] = max(dp[right], dp[left] + 1)
        return max(dp)


if __name__ == "__main__":
    test_cases = [
        ((([[-2, 0, 3]], 2)), 2),
        ((([[1, -1, 1], [2, 2, 2]], 1)), 2),
        ((([[-5, 5]], 9)), 1),
        ((([[1, 2, 3], [1, 2, 3]], 1)), 3),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxColumns(*args) == expected
