"""2029. 石子游戏 IX"""


class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        counts = [0, 0, 0]
        for stone in stones:
            counts[stone % 3] += 1
        zero, one, two = counts
        if one == 0 or two == 0:
            return zero % 2 == 1 and one + two > 2
        return zero % 2 == 0 or abs(one - two) > 2


if __name__ == "__main__":
    test_cases = [(([2, 1],), True), (([2],), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().stoneGameIX(*args) == expected
