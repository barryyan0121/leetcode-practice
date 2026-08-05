"""3592. 硬币面值还原"""


class Solution:
    def findCoins(self, numWays: list[int]) -> list[int]:
        ways = [0] * (len(numWays) + 1)
        ways[0] = 1
        coins = []
        for coin in range(1, len(numWays) + 1):
            target = numWays[coin - 1]
            if ways[coin] > target:
                return []
            if ways[coin] < target:
                coins.append(coin)
                for amount in range(coin, len(ways)):
                    ways[amount] += ways[amount - coin]
        return coins if ways[1:] == numWays else []


if __name__ == "__main__":
    test_cases = [
        (([0, 1, 0, 2, 0, 3, 0, 4, 0, 5],), [2, 4, 6]),
        (([1, 2, 2, 3, 4],), [1, 2, 5]),
        (([1, 2, 3, 4, 15],), []),
    ]
    for _, ((numWays,), expected) in enumerate(test_cases):
        assert Solution().findCoins(numWays) == expected
