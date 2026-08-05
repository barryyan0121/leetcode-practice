"""2513. 最小化两个数组中的最大值"""

from math import lcm


class Solution:
    def minimizeSet(
        self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int
    ) -> int:
        common = lcm(divisor1, divisor2)

        def possible(limit: int) -> bool:
            both = limit - limit // divisor1 - limit // divisor2 + limit // common
            only_first = limit // divisor2 - limit // common
            only_second = limit // divisor1 - limit // common
            return (
                only_first + both >= uniqueCnt1
                and only_second + both >= uniqueCnt2
                and only_first + only_second + both >= uniqueCnt1 + uniqueCnt2
            )

        left, right = 1, 2 * (uniqueCnt1 + uniqueCnt2) + 1
        while left < right:
            middle = (left + right) // 2
            if possible(middle):
                right = middle
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    test_cases = [((2, 7, 1, 3), 4), ((3, 5, 2, 1), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimizeSet(*args) == expected
