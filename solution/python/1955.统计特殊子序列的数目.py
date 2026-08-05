"""1955. 统计特殊子序列的数目"""


class Solution:
    def countSpecialSubsequences(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        dp = [0, 0, 0]
        for value in nums:
            if value == 0:
                dp[0] = (2 * dp[0] + 1) % mod
            elif value == 1:
                dp[1] = (2 * dp[1] + dp[0]) % mod
            else:
                dp[2] = (2 * dp[2] + dp[1]) % mod
        return dp[2]


if __name__ == "__main__":
    test_cases = [(([0, 1, 2, 2],), 3), (([0, 1, 2, 0, 1, 2],), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countSpecialSubsequences(*args) == expected
