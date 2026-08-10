"""2189. 建造纸牌屋的方法数"""


class Solution:
    def houseOfCards(self, n: int) -> int:
        ways = [0] * (n + 1)
        ways[0] = 1
        for cards in range(2, n + 1, 3):
            for total in range(n, cards - 1, -1):
                ways[total] += ways[total - cards]
        return ways[n]


if __name__ == "__main__":
    assert Solution().houseOfCards(16) == 2
