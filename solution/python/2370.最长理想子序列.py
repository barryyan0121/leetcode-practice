"""2370. 最长理想子序列"""


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for char in s:
            index = ord(char) - ord("a")
            best = max(dp[max(0, index - k) : min(26, index + k + 1)])
            dp[index] = best + 1
        return max(dp)

if __name__ == "__main__":
    assert Solution().longestIdealString("acfgbd", 2) == 4
