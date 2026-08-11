class Solution:
    def countOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        even, odd = m // 2, m - m // 2
        dp = [[0] * 2 for _ in range(k + 1)]
        dp[0][0] = odd
        dp[0][1] = even
        for _ in range(1, n):
            next_dp = [[0] * 2 for _ in range(k + 1)]
            for pairs in range(k + 1):
                next_dp[pairs][0] = (dp[pairs][0] + dp[pairs][1]) * odd % mod
                next_dp[pairs][1] = dp[pairs][0] * even % mod
                if pairs:
                    next_dp[pairs][1] = (
                        next_dp[pairs][1] + dp[pairs - 1][1] * even
                    ) % mod
            dp = next_dp
        return sum(dp[k]) % mod


if __name__ == "__main__":
    test_cases = [
        ((3, 4, 2), 8),
        ((5, 1, 0), 1),
        ((7, 7, 5), 5832),
    ]
    for _, ((n, m, k), expected) in enumerate(test_cases):
        assert Solution().countOfArrays(n, m, k) == expected
