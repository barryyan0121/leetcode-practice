"""2430. 对字符串执行操作后最大的删除次数"""


class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        lcp = [0] * (n + 1)
        for start in range(n - 1, -1, -1):
            for right in range(start + 1, n):
                if s[start] == s[right]:
                    lcp[right] = lcp[right + 1] + 1
                    length = right - start
                    if lcp[right] >= length:
                        dp[start] = max(dp[start], dp[right] + 1)
                else:
                    lcp[right] = 0
        return dp[0]
