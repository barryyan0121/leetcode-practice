"""2403. 杀死所有怪物的最短时间"""

from functools import lru_cache


class Solution:
    def minimumTime(self, power: list[int]) -> int:
        n = len(power)

        @lru_cache(None)
        def dp(mask: int) -> int:
            if mask == (1 << n) - 1:
                return 0
            strength = mask.bit_count() + 1
            return min(
                (power[i] + strength - 1) // strength + dp(mask | 1 << i)
                for i in range(n)
                if not mask >> i & 1
            )

        return dp(0)


if __name__ == "__main__":
    test_cases = [(([3, 4, 1],), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumTime(*args) == expected
