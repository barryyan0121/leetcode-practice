"""1922. 统计好数字的数目"""


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = 10**9 + 7
        return pow(5, (n + 1) // 2, modulo) * pow(4, n // 2, modulo) % modulo


if __name__ == "__main__":
    assert Solution().countGoodNumbers(1) == 5
