class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        dp = [0] * len(s)
        answer = 0
        for i in range(len(s)):
            for j in range(i - 1, -1, -1):
                dp[j] = dp[j - 1] + 1 if j and s[i] == s[j] else int(s[i] == s[j])
                answer = max(answer, dp[j])
        return answer


if __name__ == "__main__":
    test_cases = [("banana", 3), ("abcd", 0)]
    for _, (text, expected) in enumerate(test_cases):
        assert Solution().longestRepeatingSubstring(text) == expected
