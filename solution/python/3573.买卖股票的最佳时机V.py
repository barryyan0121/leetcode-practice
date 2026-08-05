"""3573. 买卖股票的最佳时机 V"""


class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        negative = -(10**30)
        flat = [negative] * (k + 1)
        long = [negative] * (k + 1)
        short = [negative] * (k + 1)
        flat[0] = 0
        for price in prices:
            next_flat, next_long, next_short = flat[:], long[:], short[:]
            for completed in range(k + 1):
                next_long[completed] = max(
                    next_long[completed], flat[completed] - price
                )
                next_short[completed] = max(
                    next_short[completed], flat[completed] + price
                )
                if completed < k:
                    next_flat[completed + 1] = max(
                        next_flat[completed + 1],
                        long[completed] + price,
                        short[completed] - price,
                    )
            flat, long, short = next_flat, next_long, next_short
        return max(flat)


if __name__ == "__main__":
    test_cases = [
        (([1, 7, 9, 8, 2], 2), 14),
        (([12, 16, 19, 19, 8, 1, 19, 13, 9], 3), 36),
    ]
    for _, ((prices, k), expected) in enumerate(test_cases):
        assert Solution().maximumProfit(prices, k) == expected
