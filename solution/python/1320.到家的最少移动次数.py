# @lc app=leetcode.cn id=1320 lang=python3

from functools import lru_cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        positions = {
            chr(ord("A") + index): (index // 6, index % 6) for index in range(26)
        }

        def distance(first: str, second: str) -> int:
            if not first or not second:
                return 0
            a, b = positions[first], positions[second]
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        @lru_cache(None)
        def dp(index: int, other: str) -> int:
            if index == len(word):
                return 0
            current = word[index]
            previous = word[index - 1]
            move_current = distance(previous, current)
            use_other = distance(other, current)
            return min(
                move_current + dp(index + 1, other), use_other + dp(index + 1, previous)
            )

        return dp(1, "") if len(word) > 1 else 0


if __name__ == "__main__":
    test_cases = [
        (Solution().minimumDistance, ("CAKE",), 3),
        (Solution().minimumDistance, ("HAPPY",), 6),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1320 题 "到家的最少移动次数" 所有测试用例通过')
