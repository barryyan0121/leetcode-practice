"""2543. 判断一个点是否可以到达"""

from math import gcd


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        value = gcd(targetX, targetY)
        return value & (value - 1) == 0


if __name__ == "__main__":
    test_cases = [((4, 7), True), ((6, 9), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isReachable(*args) == expected
