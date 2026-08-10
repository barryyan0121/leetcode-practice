class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        text = word1 + word2
        n = len(text)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if text[i] == text[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 if j > i + 1 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        split = len(word1)
        return max(
            (
                dp[i + 1][j - 1] + 2
                for i in range(split)
                for j in range(split, n)
                if text[i] == text[j]
            ),
            default=0,
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestPalindrome("cacb", "cbba") == 5
    assert solution.longestPalindrome("ab", "ab") == 3
    print("1771 passed")
