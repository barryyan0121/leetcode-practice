class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        dp = [[None] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = [0] * 26
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                current = [
                    max(dp[left + 1][right][c], dp[left][right - 1][c])
                    for c in range(26)
                ]
                if s[left] == s[right]:
                    char = ord(s[left]) - ord("a")
                    current[char] = max(current[char], 2)
                    if length > 2:
                        inner = dp[left + 1][right - 1]
                        largest = max(inner)
                        if inner[char] == largest:
                            largest = max(
                                (inner[c] for c in range(26) if c != char), default=0
                            )
                        current[char] = max(current[char], largest + 2)
                dp[left][right] = current
        return max(dp[0][n - 1])


if __name__ == "__main__":
    test_cases = [("bbabab", 4), ("dcbccacdb", 4), ("a", 0), ("aaaa", 2)]
    for index, (s, expected) in enumerate(test_cases):
        assert Solution().longestPalindromeSubseq(s) == expected, index
