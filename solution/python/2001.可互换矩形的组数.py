# @lc app=leetcode.cn id=2001 lang=python3

from math import gcd


class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        counts = {}
        result = 0
        for width, height in rectangles:
            divisor = gcd(width, height)
            ratio = (width // divisor, height // divisor)
            result += counts.get(ratio, 0)
            counts[ratio] = counts.get(ratio, 0) + 1
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.interchangeableRectangles,
            ([[4, 8], [3, 6], [10, 20], [15, 30]],),
            6,
        ),
        (solution.interchangeableRectangles, ([[4, 5], [7, 8]],), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2001 题 "可互换矩形的组数" 所有测试用例通过')
