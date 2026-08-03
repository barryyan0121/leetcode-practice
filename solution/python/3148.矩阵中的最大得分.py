class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        columns = len(grid[0])
        prefix_minimum = [10**18] * columns
        answer = -(10**18)
        for row in grid:
            row_minimum = 10**18
            for column, value in enumerate(row):
                previous_minimum = min(row_minimum, prefix_minimum[column])
                answer = max(answer, value - previous_minimum)
                row_minimum = min(row_minimum, previous_minimum, value)
                prefix_minimum[column] = row_minimum
        return answer


if __name__ == "__main__":
    test_cases = [([[1, 2], [3, 4]], 3), ([[7, 5], [3, 1]], -2)]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().maxScore(grid) == expected
