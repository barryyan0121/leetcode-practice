class Solution:
    def maxScore(self, a: list[int], b: list[int]) -> int:
        negative_infinity = -(10**30)
        dp = [
            0,
            negative_infinity,
            negative_infinity,
            negative_infinity,
            negative_infinity,
        ]
        for value in b:
            for count in range(4, 0, -1):
                dp[count] = max(dp[count], dp[count - 1] + a[count - 1] * value)
        return dp[4]


if __name__ == "__main__":
    test_cases = [
        (([3, 2, 5, 6], [2, -6, 4, -5, -3, 2, -7]), 26),
        (([-1, 4, 5, -2], [-5, -1, -3, -2, -4]), -1),
    ]
    for _, ((a, b), expected) in enumerate(test_cases):
        assert Solution().maxScore(a, b) == expected
