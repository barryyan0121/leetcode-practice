class Solution:
    def maxScore(self, prices: list[int]) -> int:
        groups = {}
        for index, price in enumerate(prices):
            key = price - index
            groups[key] = groups.get(key, 0) + price
        return max(groups.values())


if __name__ == "__main__":
    test_cases = [
        ([1, 5, 3, 7, 8], 20),
        ([4, 3, 2], 4),
    ]
    for index, (prices, expected) in enumerate(test_cases):
        assert Solution().maxScore(prices) == expected, index
