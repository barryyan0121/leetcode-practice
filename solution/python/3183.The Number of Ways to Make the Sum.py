class Solution:
    def numberOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        for coin in (1, 2, 6):
            for total in range(coin, n + 1):
                dp[total] = (dp[total] + dp[total - coin]) % mod
        for extra in (4, 8):
            if n >= extra:
                dp[n] = (dp[n] + dp[n - extra]) % mod
        return dp[n]


if __name__ == "__main__":
    assert Solution().numberOfWays(4) == 4
    assert Solution().numberOfWays(0) == 1
