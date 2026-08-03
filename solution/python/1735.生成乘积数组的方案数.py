# @lc app=leetcode.cn id=1735 lang=python3


class Solution:
    def waysToFillArray(self, queries: list[list[int]]) -> list[int]:
        modulus = 10**9 + 7
        result = []
        for length, value in queries:
            ways = 1
            factor = 2
            remaining = value
            while factor * factor <= remaining:
                exponent = 0
                while remaining % factor == 0:
                    remaining //= factor
                    exponent += 1
                if exponent:
                    ways = (
                        ways
                        * self._combination(length + exponent - 1, exponent, modulus)
                        % modulus
                    )
                factor += 1
            if remaining > 1:
                ways = ways * length % modulus
            result.append(ways)
        return result

    @staticmethod
    def _combination(n: int, k: int, modulus: int) -> int:
        result = 1
        for value in range(1, k + 1):
            result = result * (n - k + value) % modulus
            result = result * pow(value, modulus - 2, modulus) % modulus
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.waysToFillArray, ([[2, 6], [5, 1], [73, 660]],), [4, 1, 50734910]),
        (solution.waysToFillArray, ([[1, 1], [1, 2], [2, 4]],), [1, 1, 3]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1735 题 "生成乘积数组的方案数" 所有测试用例通过')
