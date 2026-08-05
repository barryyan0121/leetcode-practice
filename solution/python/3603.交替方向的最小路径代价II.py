"""3603. 交替方向的最小路径代价 II"""


class Solution:
    def minCost(self, m: int, n: int, waitCost: list[list[int]]) -> int:
        dp = [1 << 60] * n
        for i in range(m):
            for j in range(n):
                enter = (i + 1) * (j + 1)
                if i == j == 0:
                    dp[j] = enter
                else:
                    dp[j] = (min(dp[j], dp[j - 1]) if j else dp[j]) + enter
                    if i != m - 1 or j != n - 1:
                        dp[j] += waitCost[i][j]
        return dp[-1]


if __name__ == "__main__":
    test_cases = [
        ((1, 2, [[1, 2]]), 3),
        ((2, 2, [[3, 5], [2, 4]]), 9),
        ((2, 3, [[6, 1, 4], [3, 2, 5]]), 16),
    ]
    for _, ((m, n, wait_cost), expected) in enumerate(test_cases):
        assert Solution().minCost(m, n, wait_cost) == expected
