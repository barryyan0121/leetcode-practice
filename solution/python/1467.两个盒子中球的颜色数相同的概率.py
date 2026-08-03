# @lc app=leetcode.cn id=1467 lang=python3

from functools import lru_cache
from math import comb


class Solution:
    def getProbability(self, balls: list[int]) -> float:
        total = sum(balls)
        half = total // 2

        @lru_cache(None)
        def count(color: int, used: int, first_colors: int, second_colors: int) -> int:
            if color == len(balls):
                return int(used == half and first_colors == second_colors)
            result = 0
            for first_count in range(balls[color] + 1):
                second_count = balls[color] - first_count
                if used + first_count > half:
                    break
                result += comb(balls[color], first_count) * count(
                    color + 1,
                    used + first_count,
                    first_colors + (first_count > 0),
                    second_colors + (second_count > 0),
                )
            return result

        favorable = count(0, 0, 0, 0)
        return favorable / comb(total, half)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.getProbability, ([1, 1],), 1.0)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert abs(func(*args) - expected) < 1e-9
    print('第 1467 题 "两个盒子中球的颜色数相同的概率" 所有测试用例通过')
