"""2481. 分割圆的最少切割次数"""


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        return n // 2 if n % 2 == 0 else n


if __name__ == "__main__":
    assert Solution().numberOfCuts(4) == 2 and Solution().numberOfCuts(3) == 3
