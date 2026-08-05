"""2428. 沙漏的最大总和"""


class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        return max(
            sum(grid[i][j : j + 3]) + grid[i + 1][j + 1] + sum(grid[i + 2][j : j + 3])
            for i in range(len(grid) - 2)
            for j in range(len(grid[0]) - 2)
        )


if __name__ == "__main__":
    test_cases = [(([[6, 2, 1, 3], [4, 2, 1, 5], [9, 8, 7, 6], [2, 2, 1, 3]],), 35)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxSum(*args) == expected
