"""2518. 好分区的数目"""


class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        total = sum(nums)
        if total < 2 * k:
            return 0
        dp = [0] * k
        dp[0] = 1
        for value in nums:
            for amount in range(k - 1, value - 1, -1):
                dp[amount] = (dp[amount] + dp[amount - value]) % mod
        bad = sum(dp) % mod
        return (pow(2, len(nums), mod) - 2 * bad) % mod


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4], 4), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countPartitions(*args) == expected
