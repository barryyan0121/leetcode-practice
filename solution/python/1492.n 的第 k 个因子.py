# @lc app=leetcode.cn id=1492 lang=python3

from math import isqrt


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []
        for factor in range(1, isqrt(n) + 1):
            if n % factor == 0:
                small.append(factor)
                if factor * factor != n:
                    large.append(n // factor)
        factors = small + large[::-1]
        return factors[k - 1] if k <= len(factors) else -1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.kthFactor, (12, 3), 3)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1492 题 "n 的第 k 个因子" 所有测试用例通过')
