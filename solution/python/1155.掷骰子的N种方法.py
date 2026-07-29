class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10**9 + 7
        dp = [1] + [0] * target
        for _ in range(n):
            next_dp = [0] * (target + 1)
            for total in range(1, target + 1):
                next_dp[total] = sum(dp[max(0, total - k) : total]) % modulo
            dp = next_dp
        return dp[target]


if __name__ == "__main__":
    test_cases = [(1, 6, 3, 1), (2, 6, 7, 6), (30, 30, 500, 222616187)]
    for _, (n, k, target, expected) in enumerate(test_cases):
        assert Solution().numRollsToTarget(n, k, target) == expected
