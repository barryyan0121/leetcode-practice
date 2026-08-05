class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)
        dp = [10**18] * (n + 1)
        dp[0] = 0
        for c, t in zip(cost, time):
            for painted in range(n, -1, -1):
                nxt = min(n, painted + t + 1)
                dp[nxt] = min(dp[nxt], dp[painted] + c)
        return dp[n]


if __name__ == "__main__":
    assert Solution().paintWalls([1, 2, 3, 2], [1, 2, 3, 2]) == 3
