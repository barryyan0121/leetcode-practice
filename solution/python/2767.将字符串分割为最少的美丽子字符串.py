class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        powers = {bin(5**i)[2:] for i in range(20)}
        for i in range(n):
            if s[i] == "0":
                continue
            for j in range(i + 1, n + 1):
                if s[i:j] in powers:
                    dp[j] = min(dp[j], dp[i] + 1)
        return -1 if dp[n] > n else dp[n]


if __name__ == "__main__":
    assert Solution().minimumBeautifulSubstrings("1011") == 2
