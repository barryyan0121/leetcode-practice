"""2533. 好二进制字符串的数量"""


class Solution:
    def goodBinaryStrings(
        self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int
    ) -> int:
        mod = 10**9 + 7
        dp = [0] * (maxLength + 1)
        dp[0] = 1
        for length in range(1, maxLength + 1):
            if length >= oneGroup:
                dp[length] += dp[length - oneGroup]
            if length >= zeroGroup:
                dp[length] += dp[length - zeroGroup]
            dp[length] %= mod
        return sum(dp[minLength : maxLength + 1]) % mod


if __name__ == "__main__":
    test_cases = [((3, 3, 1, 1), 8)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().goodBinaryStrings(*args) == expected
