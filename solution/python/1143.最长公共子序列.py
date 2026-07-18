class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for first in text1:
            diagonal = 0
            for index, second in enumerate(text2, 1):
                previous = dp[index]
                if first == second:
                    dp[index] = diagonal + 1
                else:
                    dp[index] = max(dp[index], dp[index - 1])
                diagonal = previous
        return dp[-1]


if __name__ == "__main__":
    test_cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("bl", "yby", 1),
    ]
    for _, (text1, text2, expected) in enumerate(test_cases):
        assert Solution().longestCommonSubsequence(text1, text2) == expected
