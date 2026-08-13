"""2472. 不重叠回文子字符串的最大数目"""


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        palindrome = [bytearray(n) for _ in range(n)]
        for end in range(n):
            dp[end + 1] = dp[end]
            for start in range(end, -1, -1):
                palindrome[start][end] = s[start] == s[end] and (
                    end - start < 2 or palindrome[start + 1][end - 1]
                )
                if end - start + 1 >= k and palindrome[start][end]:
                    dp[end + 1] = max(dp[end + 1], dp[start] + 1)
        return dp[n]

if __name__ == "__main__":
    assert Solution().maxPalindromes("abaccdbbd", 3) == 2
