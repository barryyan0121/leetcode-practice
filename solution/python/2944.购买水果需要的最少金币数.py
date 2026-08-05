"""2944. 购买水果需要的最少金币数"""


class Solution:
    def minimumCoins(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)
        for index in range(n - 1, -1, -1):
            end = min(n, 2 * index + 2)
            dp[index] = prices[index] + min(dp[index + 1 : end + 1])
        return dp[0]


if __name__ == "__main__":
    test_cases = [(([1, 10, 1, 1],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumCoins(*args) == expected
