# @lc app=leetcode.cn id=1387 lang=python3
from functools import lru_cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(value):
            return (
                0
                if value == 1
                else 1 + power(value // 2 if value % 2 == 0 else 3 * value + 1)
            )

        return sorted(range(lo, hi + 1), key=lambda value: (power(value), value))[k - 1]


if __name__ == "__main__":
    test_cases = [
        (Solution().getKth, (12, 15, 2), 13),
        (Solution().getKth, (1, 1, 1), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1387 题 "将整数按权重排序" 所有测试用例通过')
