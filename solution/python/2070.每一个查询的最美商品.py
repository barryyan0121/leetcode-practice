"""2070. 每一个查询的最美商品"""

from bisect import bisect_right


class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()
        prices, beauties = [], []
        for price, beauty in items:
            if prices and prices[-1] == price:
                beauties[-1] = max(beauties[-1], beauty)
            else:
                prices.append(price)
                beauties.append(max(beauties[-1], beauty) if beauties else beauty)
        return [
            (
                beauties[bisect_right(prices, query) - 1]
                if bisect_right(prices, query)
                else 0
            )
            for query in queries
        ]


if __name__ == "__main__":
    test_cases = [(([[1, 2], [3, 2], [2, 4]], [1, 2, 3]), [2, 4, 4])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumBeauty(*args) == expected
