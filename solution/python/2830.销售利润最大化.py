class Solution:
    def maximizeTheProfit(self, n: int, offers: list[list[int]]) -> int:
        by_end = [[] for _ in range(n)]
        for start, end, gold in offers:
            by_end[end].append((start, gold))
        dp = [0] * (n + 1)
        for end in range(n):
            dp[end + 1] = dp[end]
            for start, gold in by_end[end]:
                dp[end + 1] = max(dp[end + 1], dp[start] + gold)
        return dp[n]


if __name__ == "__main__":
    assert Solution().maximizeTheProfit(5, [[0, 0, 1], [0, 2, 2], [1, 3, 2]]) == 3
