"""1908. Nim 游戏 II"""


class Solution:
    def nimGame(self, piles: list[int]) -> bool:
        value = 0
        for pile in piles:
            value ^= pile
        return value != 0


if __name__ == "__main__":
    test_cases = [([1, 2, 3], False), ([1, 1], False), ([1, 2], True)]
    for _, (piles, expected) in enumerate(test_cases):
        assert Solution().nimGame(piles) == expected
