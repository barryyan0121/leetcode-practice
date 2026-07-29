from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()
        return [
            products[
                bisect_left(products, searchWord[:index]) : bisect_right(
                    products, searchWord[:index] + "{"
                )
            ][:3]
            for index in range(1, len(searchWord) + 1)
        ]


if __name__ == "__main__":
    test_cases = [
        (
            (["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"),
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        )
    ]
    for _, ((products, search_word), expected) in enumerate(test_cases):
        assert Solution().suggestedProducts(products, search_word) == expected
