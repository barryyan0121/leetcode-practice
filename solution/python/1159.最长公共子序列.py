class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for char1 in text1:
            previous = 0
            for index, char2 in enumerate(text2, 1):
                current = dp[index]
                if char1 == char2:
                    dp[index] = previous + 1
                else:
                    dp[index] = max(dp[index], dp[index - 1])
                previous = current
        return dp[-1]


if __name__ == "__main__":
    test_cases = [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0)]
    for _, (text1, text2, expected) in enumerate(test_cases):
        assert Solution().longestCommonSubsequence(text1, text2) == expected
