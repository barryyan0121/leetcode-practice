class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        costs = []
        for column in range(columns):
            counts = [0] * 10
            for row in range(rows):
                counts[grid[row][column]] += 1
            costs.append([rows - count for count in counts])

        dp = costs[0]
        for column in range(1, columns):
            dp = [
                costs[column][value]
                + min(dp[other] for other in range(10) if other != value)
                for value in range(10)
            ]
        return min(dp)


if __name__ == "__main__":
    test_cases = [([[1, 0, 2], [1, 0, 2]], 0), ([[1, 1, 1], [1, 1, 1]], 2)]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().minimumOperations(grid) == expected
