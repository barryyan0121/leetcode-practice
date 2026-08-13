"""2320. 统计放置房子的方式数"""


class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 1_000_000_007
        one, two = 1, 2
        for _ in range(2, n + 1):
            one, two = two, (one + two) % mod
        return two * two % mod

if __name__ == "__main__":
    assert Solution().countHousePlacements(1) == 4
