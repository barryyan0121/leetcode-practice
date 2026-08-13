class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[10**9] * n for _ in range(n)]
        for left in range(n):
            for right in range(left + 1, n):
                length = right - left + 1
                for divisor in range(1, length):
                    if length % divisor:
                        continue
                    changes = 0
                    for offset in range(divisor):
                        positions = list(range(left + offset, right + 1, divisor))
                        for i in range(len(positions) // 2):
                            changes += s[positions[i]] != s[positions[-i - 1]]
                    cost[left][right] = min(cost[left][right], changes)
        dp = [[10**9] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for end in range(2, n + 1):
            for parts in range(1, min(k, end // 2) + 1):
                for start in range(end - 1):
                    dp[end][parts] = min(
                        dp[end][parts], dp[start][parts - 1] + cost[start][end - 1]
                    )
        return dp[n][k]


assert Solution().minimumChanges("abcac", 2) == 1
