"""2291. 最大股票收益"""


class Solution:
    def maximumProfit(self, present: list[int], future: list[int], budget: int) -> int:
        dp = [0] * (budget + 1)
        for cost, value in zip(present, future):
            if value <= cost:
                continue
            profit = value - cost
            for money in range(budget, cost - 1, -1):
                dp[money] = max(dp[money], dp[money - cost] + profit)
        return dp[budget]

if __name__ == "__main__":
    assert Solution().maximumProfit([1,2,3,4], [2,5,6,8], 5) == 6
