from math import gcd


class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        dp = [0] * (1 << n)
        dp[0] = 1
        for mask in range(1 << n):
            position = mask.bit_count() + 1
            if position > n:
                continue
            for value in range(1, n + 1):
                bit = 1 << (value - 1)
                if not mask & bit and gcd(value, position) == 1:
                    dp[mask | bit] += dp[mask]
        return dp[-1]


if __name__ == "__main__":
    assert Solution().selfDivisiblePermutationCount(1) == 1
    assert Solution().selfDivisiblePermutationCount(2) == 1
    assert Solution().selfDivisiblePermutationCount(3) == 3
