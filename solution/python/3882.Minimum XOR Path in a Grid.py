class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        max_value = max(value for row in grid for value in row)
        limit = 1 << max_value.bit_length()
        dp = [[False] * limit for _ in range(len(grid[0]))]
        dp[0][0] = True
        for i in range(len(grid)):
            new_dp = [[False] * limit for _ in range(len(grid[0]))]
            for j in range(len(grid[0])):
                for value in range(limit):
                    if dp[j][value] or (j > 0 and new_dp[j - 1][value]):
                        new_dp[j][value ^ grid[i][j]] = True
            dp = new_dp
        return next(value for value in range(limit) if dp[-1][value])


if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [3, 4]], 6),
        ([[6, 7], [5, 8]], 9),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().minCost(grid) == expected
