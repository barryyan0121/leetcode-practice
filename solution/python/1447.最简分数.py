# @lc app=leetcode.cn id=1447 lang=python3

from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        return [
            f"{numerator}/{denominator}"
            for denominator in range(2, n + 1)
            for numerator in range(1, denominator)
            if gcd(numerator, denominator) == 1
        ]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.simplifiedFractions, (3,), ["1/2", "1/3", "2/3"])]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1447 题 "最简分数" 所有测试用例通过')
