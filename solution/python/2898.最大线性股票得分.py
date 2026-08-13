class Solution:
    def maxScore(self, prices: list[int]) -> int:
        groups = {}
        for index, price in enumerate(prices):
            key = price - index
            groups[key] = groups.get(key, 0) + price
        return max(groups.values())


assert Solution().maxScore([1, 5, 3, 7, 8]) == 20
