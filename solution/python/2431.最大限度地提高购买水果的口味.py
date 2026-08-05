"""2431. 最大限度地提高购买水果的口味"""


class Solution:
    def maxTastiness(
        self,
        price: list[int],
        tastiness: list[int],
        maxAmount: int,
        maxCoupons: int,
    ) -> int:
        dp = [[0] * (maxAmount + 1) for _ in range(maxCoupons + 1)]
        for cost, taste in zip(price, tastiness):
            for coupons in range(maxCoupons, -1, -1):
                for amount in range(maxAmount, -1, -1):
                    if amount >= cost:
                        dp[coupons][amount] = max(
                            dp[coupons][amount], dp[coupons][amount - cost] + taste
                        )
                    if coupons and amount >= cost // 2:
                        dp[coupons][amount] = max(
                            dp[coupons][amount],
                            dp[coupons - 1][amount - cost // 2] + taste,
                        )
        return dp[maxCoupons][maxAmount]


if __name__ == "__main__":
    test_cases = [(([10, 20, 20], [5, 8, 8], 20, 1), 13)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxTastiness(*args) == expected
